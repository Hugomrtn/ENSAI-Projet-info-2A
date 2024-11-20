import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection
from dao.dao_polygone import Dao_polygone

from business_object.contour import Contour


class Dao_contour(metaclass=Singleton):

    # ############################################# Créations

    # @log
    def creer(self):
        """
        Création d'un nouveau contour dans la base de données

        Parameters
        ----------

        Returns
        -------
        int
            L'identifiant du contour créé si l'insertion a réussi,
            None en cas d'échec
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_2A.contour DEFAULT VALUES "
                        "RETURNING id_contour;",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_contour"]

    # @log
    def creer_association_polygone_contour(self, id_contour, id_polygone,
                                           appartient):
        """
        Création d'une association entre un contour et un polygone
        dans la base de données

        Parameters
        ----------
        id_contour : int
            L'identifiant du contour
        id_polygone : int
            L'identifiant du polygone
        appartient : bool
            Indique si le polygone appartient au contour (True) ou est
            enclavé (False)

        Returns
        -------
        None
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO projet_2A.association_contours_polygones(
                            id_contour, id_polygone, appartient
                        ) VALUES (
                            %(id_contour)s, %(id_polygone)s, %(appartient)s
                        )
                        """,
                        {
                            "id_contour": id_contour,
                            "id_polygone": id_polygone,
                            "appartient": appartient,
                        },
                    )
        except Exception as e:
            logging.info(e)

    # @log
    def creer_entierement_contour(self, contour: Contour):
        """
        Création complète d'un contour dans la base de données

        Parameters
        ----------
        contour : Contour
            Contour à ajouter dans la base de données

        Returns
        -------
        int
            L'identifiant du contour créé
        """
        id_contour = Dao_contour().creer()

        for polygone in contour.polygones_composants:
            id_polygones_composants = \
                Dao_polygone().creer_entierement_polygone(polygone)
            Dao_contour().creer_association_polygone_contour(
                id_contour, id_polygones_composants, True)

        for polygone in contour.polygones_enclaves:
            id_polygones_enclaves = \
                Dao_polygone().creer_entierement_polygone(polygone)
            Dao_contour().creer_association_polygone_contour(
                id_contour, id_polygones_enclaves, False)

        return id_contour

    # ############################################# Obtenir informations

    @log
    def obtenir_id_contour_selon_id_emplacement_annne(self, id_emplacement,
                                                      annee):
        """
        Trouve tous les contours selon l'année et l'id de l'emplacement

        Parameters
        ----------
        id_emplacement : int
            L'identifiant de l'emplacement
        annee : int
            L'année pour laquelle le contour est recherché

        Returns
        -------
        int
            L'identifiant du contour correspondant si trouvé, lève une
            exception en cas d'erreur
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_contour                                  "
                        "FROM projet_2A.association_emplacement_contour     "
                        "WHERE id_emplacement = %(id_emplacement)s          "
                        "AND annee = %(annee)s;                             ",
                        {
                            "id_emplacement": id_emplacement,
                            "annee": annee,
                        }
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        id_contour = res["id_contour"]

        return id_contour

    # ############################################# Modifications&Suppressions

    @log
    def supprimer(self, id_contour):
        """
        Suppression d'un contour et de ses associations avec des polygones
        dans la base de données

        Parameters
        ----------
        id_contour : int
            L'identifiant du contour à supprimer

        Returns
        -------
        bool
            True si le contour et ses associations ont bien été supprimés,
            False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le contour
                    cursor.execute(
                        "DELETE FROM projet_2A.contour                  "
                        " WHERE id_contour=%(id_contour)s      ",
                        {"id_contour": id_contour},
                    )
                    # supprime aussi toutes les assocations entre un polygone
                    # et un contour
                    cursor.execute(
                        " DELETE FROM projet_2A.association_contour_polygones"
                        " WHERE id_contour=%(id_contour)s      ",
                        {"id_contour": id_contour},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

# #############

    def existe(self, contour: Contour):
        """
        Vérifie l'existence d'un contour dans la base de données

        Parameters
        ----------
        contour : Contour
            Le contour à vérifier

        Returns
        -------
        list
            [True, id_contour] si le contour existe et est identifié dans la
            base de données, [False, None] si le contour n'existe pas.
        """

        id_contour = None
        existence_contour = True

        # existence de tous les polygones composants
        liste_id_polygones_composants = []
        for polygone in contour.polygones_composants:
            existence_polygone = Dao_polygone().existe(polygone)
            liste_id_polygones_composants.append(existence_polygone[1])
            if not existence_polygone[0]:
                existence_polygone = False
                break
        if not existence_contour:
            return [False, id_contour]

        # existence de tous les polygones enclaves
        liste_id_polygones_enclaves = []
        for polygone in contour.polygones_enclaves:
            existence_polygone = Dao_polygone().existe(polygone)
            liste_id_polygones_enclaves.append(existence_polygone[1])
            if not existence_polygone[0]:
                existence_polygone = False
                break
        if not existence_contour:
            return [False, id_contour]

        # polygones composants
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_contour, id_polygone, appartient "
                        "FROM projet_2A.association_contours_polygones "
                        "WHERE appartient=TRUE",
                    )
                    liste_polynomes_composants = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        contour = {}
        for ligne in liste_polynomes_composants:
            id_contour_courant = ligne['id_contour']
            id_polygone = ligne['id_polygone']

            if id_polygone not in contour:
                contour[id_polygone] = []

            contour[id_polygone].append(id_contour_courant)

        for id_contour_courant, id_polygone_courant in contour.items():
            if liste_id_polygones_composants == id_polygone_courant:
                existe_composants = [True, id_contour_courant]
                break

        # polygones enclaves
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_contour, id_polygone, appartient "
                        "FROM projet_2A.association_contours_polygones "
                        "WHERE appartient=FALSE",
                    )
                    liste_polynomes_enclaves = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        contour = {}
        for ligne in liste_polynomes_enclaves:
            id_contour_courant = ligne['id_contour']
            id_polygone = ligne['id_polygone']

            if id_polygone not in contour:
                contour[id_polygone] = []

            contour[id_polygone].append(id_contour_courant)

        for id_contour_courant, id_polygone_courant in contour.items():
            if liste_id_polygones_enclaves == id_polygone_courant:
                existe_enclaves = [True, id_contour_courant]
                break

        if existe_composants and existe_enclaves:
            if (existe_composants[0] and existe_enclaves[0]):
                if (existe_composants[1] == existe_enclaves[1]):
                    return [True, existe_composants[1]]

        return [False, None]

    def existe2(self, contour: Contour):
        """
        Vérifie l'existence d'un contour dans la base de données

        Parameters
        ----------
        contour : Contour
            Le contour à vérifier

        Returns
        -------
        list
            [True, id_contour] si le contour existe et est identifié dans la
            base de données, [False, None] si le contour n'existe pas.
        """

        id_contour = None # noqa
        existence_contour = True # noqa

        # existence de tous les polygones composants
        # OK
        liste_id_polygones_composants = []
        for polygone in contour.polygones_composants:
            existence_polygone = Dao_polygone().existe(polygone)
            liste_id_polygones_composants.append(existence_polygone[1])
            if not existence_polygone[0]:
                return [False, None]

        # existence de tous les polygones enclaves
        # OK
        liste_id_polygones_enclaves = []
        for polygone in contour.polygones_enclaves:
            existence_polygone = Dao_polygone().existe(polygone)
            liste_id_polygones_enclaves.append(existence_polygone[1])
            if not existence_polygone[0]:
                return [False, None]

        # ##################################
        # POUR LES POLYGONES COMPOSANTS
        existe_composants = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_contour, id_polygone, appartient "
                        "FROM projet_2A.association_contours_polygones "
                        "WHERE appartient=TRUE",
                    )
                    liste_polynomes_composants = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        contour = {}
        for ligne in liste_polynomes_composants:
            id_contour_courant = ligne['id_contour']
            id_polygone = ligne['id_polygone']

            if id_polygone not in contour:
                contour[id_polygone] = []

            contour[id_polygone].append(id_contour_courant)

        for id_contour_courant, id_polygone_courant in contour.items():
            if liste_id_polygones_composants == id_polygone_courant:
                existe_composants = [True, id_contour_courant]
                break

        return existe_composants

###############
    def instancier_contour_selon_id_contour(self, id_contour):
        """
        Instancie un objet Contour

        Parameters
        ----------
        id_contour : int
            L'identifiant du contour dans la base de données.

        Returns
        -------
        Contour
            Un objet Contour associé à l'identifiant de contour donné
        """

        liste_polygones_composants = []
        liste_polygones_enclaves = []

        liste_id_polygones_composants = Dao_polygone().\
            obtenir_id_polygones_composants_selon_id_contour(id_contour)
        liste_id_polygones_enclaves = Dao_polygone().\
            obtenir_id_polygones_enclaves_selon_id_contour(id_contour)

        for id_polygone_composant in liste_id_polygones_composants:
            liste_polygones_composants.append(
                Dao_polygone().instancier_polygone_selon_id_polygone(
                    id_polygone_composant))

        for id_polygone_enclave in liste_id_polygones_enclaves:
            liste_polygones_enclaves.append(
                Dao_polygone().instancier_polygone_selon_id_polygone(
                    id_polygone_enclave))

        return Contour(liste_polygones_composants, liste_polygones_enclaves)
