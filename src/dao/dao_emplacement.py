import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.emplacement import Emplacement


class Dao_emplacement(metaclass=Singleton):

    # ############################################# Créations

    # @log
    def creer(self, emplacement: Emplacement) -> bool:
        """Création d'un emplacement dans la base de données
            Parameters
            ----------
            emplacement : Emplacement

            Returns
            -------
            created : bool
                True si la création est un succès
                False sinon
            """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_2A.emplacement(   "
                        "nom_emplacement, niveau, code) VALUES               "
                        "(%(nom_emplacement)s, %(niveau)s, %(code)s)"
                        "RETURNING id_emplacement;                           ",
                        {
                            "nom_emplacement": emplacement.nom_emplacement,
                            "niveau": emplacement.niveau,
                            "code": emplacement.code,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_emplacement"]

    # @log
    def creer_association_emplacement_contour(self,
                                              id_emplacement, annee: int,
                                              id_contour, nombre_habitants: int):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_2A.association_emplacement_contour(       "
                        "id_emplacement, annee, id_contour, nombre_habitants) VALUES     "
                        "(%(id_emplacement)s, %(annee)s, %(id_contour)s,     "
                        "%(nombre_habitants)s)                                           ",
                        {
                            "id_emplacement": id_emplacement,
                            "annee": annee,
                            "id_contour": id_contour,
                            "nombre_habitants": nombre_habitants,
                        },
                    )
        except Exception as e:
            logging.info(e)

    # @log
    def creer_entierement_emplacement(self, emplacement: Emplacement,
                                      id_contour):

        id_emplacement = Dao_emplacement().creer(emplacement)

        Dao_emplacement().creer_association_emplacement_contour(
            id_emplacement, emplacement.annee, id_contour,
            emplacement.nombre_habitants)

    # ############################################# Obtenir informations

    @log
    def obtenir_nom(self, id_emplacement) -> str:
        """trouver le nom d'un emplacement grace à son id

        Parameters
        ----------
        id_emplacement : int
            numéro id de l'emplacement que l'on souhaite trouver

        Returns
        -------
        nom : str
            renvoie le nom que l'on cherche
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_emplacement                             "
                        "FROM projet_2A.emplacement                                   "
                        "WHERE id_emplacement = %(id_emplacement)i;         ",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        return res["nom_emplacement"]

    @log
    def obtenir_informations(self, id_emplacement) -> str:
        """trouver un emplacement grace à son id

        Parameters
        ----------
        id_emplacement : int
            numéro id de l'emplacement que l'on souhaite trouver

        Returns
        -------
        nom : str
            renvoie les informations que l'on veut
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                           "
                        "  FROM projet_2A.emplacement                                 "
                        " WHERE id_emplacement = %(id_emplacement)i;        ",
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        return res

    @log
    def obtenir_id_emplacements_selon_niveau_annee(self, niveau, annee):
        """Trouve tous les emplacements selon l'année et le niveau

        Parameters
        ----------

        Returns

        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_emplacement                              "
                        "FROM projet_2A.emplacement                                   "
                        "JOIN projet_2A.association_emplacement_contour               "
                        "USING(id_emplacement)                              "
                        "WHERE emplacement.niveau = %(niveau)s AND          "
                        "association_emplacement_contour.annee = %(annee)s; ",
                        {
                            "niveau": niveau,
                            "annee": annee,
                        }
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_id_emplacements = []

        for i in range(res):
            liste_id_emplacements.append(res["id_emplacement"][i])

        return liste_id_emplacements

    # ############################################# Modifications&Suppressions

    @log
    def modifier_emplacement(self, id_emplacement, nouveau_nom,
                             nouveau_niveau, nouveau_code) -> bool:
        """Modification d'un emplacement dans la base de données

        Parameters
        ----------


        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE projet_2A.emplacement                                 "
                        "   SET niveau      = %(niveau)s,                   "
                        "       nom         = %(nom)s,                      "
                        "       code         = %(code)s,                    "
                        " WHERE id_emplacement = %(id_emplacement)s;        ",
                        {
                            "niveau": nouveau_niveau,
                            "nom": nouveau_nom,
                            "code": nouveau_code,
                            "id_emplacement": id_emplacement,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    @log
    def supprimer_emplacement(self, id_emplacement) -> bool:
        """Suppression d'un emplacement dans la base de données

        Parameters
        ----------


        Returns
        -------
            True si l'emplacement a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer l'emplacement
                    cursor.execute(
                        "DELETE FROM projet_2A.emplacement                            "
                        " WHERE id_emplacement=%(id_emplacement)s           ",
                        {"id_emplacement": id_emplacement},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
