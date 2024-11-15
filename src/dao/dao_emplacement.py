import logging

from utils.singleton import Singleton
from utils.log_decorator import log # NOQA

from dao.db_connection import DBConnection

from business_object.emplacement import Emplacement


class Dao_emplacement(metaclass=Singleton):

    # ############################################# Créations

    @log
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

        existe = Dao_emplacement().existe(emplacement)
        if existe[0]:
            return existe[1]

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
                                              id_contour,
                                              nombre_habitants: int):
        """
        Crée une association entre un emplacement et un contour dans la base de données.

        Cette méthode insère une nouvelle association dans la table `association_emplacement_contour`,
        reliant un emplacement et un contour pour une année spécifique, et enregistre le nombre d'habitants.

        Parameters
        ----------
        id_emplacement : int
            L'identifiant unique de l'emplacement dans la base de données.
        annee : int
            L'année de l'association.
        id_contour : int
            L'identifiant unique du contour dans la base de données.
        nombre_habitants : int
            Le nombre d'habitants associé à cet emplacement et ce contour pour l'année donnée.

        Returns
        -------
        None

        Raises
        ------
        Exception
            En cas d'erreur lors de l'insertion, l'exception est journalisée et levée.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO                                        "
                        "projet_2A.association_emplacement_contour(         "
                        "id_emplacement, annee, id_contour,                 "
                        "nombre_habitants) VALUES                           "
                        "(%(id_emplacement)s, %(annee)s, %(id_contour)s,    "
                        "%(nombre_habitants)s)                              ",
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
        """
        Crée un emplacement dans la base de données et associe ce dernier à un contour.

        Cette méthode effectue deux opérations :
        1. Elle crée un nouvel emplacement dans la base de données via la méthode `creer` de `Dao_emplacement`.
        2. Elle crée une association entre l'emplacement nouvellement créé et un contour spécifique, en enregistrant également l'année et le nombre d'habitants de l'emplacement.

        Parameters
        ----------
        emplacement : Emplacement
            L'objet Emplacement contenant les informations de l'emplacement à créer,
            incluant l'année et le nombre d'habitants.
        id_contour : int
            L'identifiant du contour auquel l'emplacement sera associé.

        Returns
        -------
        None
        """
        id_emplacement = Dao_emplacement().creer(emplacement)

        Dao_emplacement().creer_association_emplacement_contour(
            id_emplacement, emplacement.annee, id_contour,
            emplacement.nombre_habitants)

    # ############################################# Existence

    def existe(self, emplacement: Emplacement):
        """
        Vérifie si un emplacement existe déjà dans la base de données en fonction de ses attributs.

        Cette méthode recherche un emplacement dans la base de données en utilisant les critères suivants :
        - Le nom de l'emplacement
        - Le niveau de l'emplacement
        - Le code de l'emplacement

        Si un emplacement correspondant est trouvé, la méthode retourne un indicateur de son existence et son identifiant.
        Sinon, elle retourne un indicateur indiquant que l'emplacement n'existe pas.

        Parameters
        ----------
        emplacement : Emplacement
            L'objet Emplacement contenant les informations à vérifier dans la base de données.

        Returns
        -------
        List[bool, int or None]
            - Un booléen `True` si l'emplacement existe, `False` sinon.
            - L'identifiant de l'emplacement si trouvé, sinon `None`.
        """
        existe = False
        id_emplacement = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_emplacement FROM projet_2A.emplacement   "
                        "WHERE nom_emplacement = %(nom_emplacement)s        "
                        "AND niveau = %(niveau)s                            "
                        "AND code = %(code)s;                               ",
                        {
                            "nom_emplacement": emplacement.nom_emplacement,
                            "niveau": emplacement.niveau,
                            "code": emplacement.code,
                        },
                    )
                    res = cursor.fetchone()
                    if res:
                        id_emplacement = res["id_emplacement"]
                        existe = True
        except Exception as e:
            logging.info(e)

        return [existe, id_emplacement]

    # ############################################# Obtenir informations

    # @log
    def obtenir_emplacement_selon_id_et_annee(self, id_emplacement, annee):
        """Renvoie les informations d'un emplacement selon son ID et l'année
        spécifiée.

        Parameters
        ----------
        id_emplacement : int
            L'identifiant de l'emplacement à rechercher.
        annee : int
            L'année pour laquelle les informations sont demandées.

        Returns
        -------
        Emplacement
            Une instance de la classe Emplacement avec les données de
            l'emplacement, ou None si aucun emplacement n'est trouvé.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_emplacement, niveau, code, annee,       "
                        "nombre_habitants FROM projet_2A.emplacement        "
                        "JOIN projet_2A.association_emplacement_contour     "
                        "USING(id_emplacement)                              "
                        "WHERE id_emplacement = %(id_emplacement)s          "
                        "AND annee = %(annee)s;                            ",
                        {
                            "id_emplacement": id_emplacement,
                            "annee": annee,
                        },
                    )
                    res = cursor.fetchone()
                    if res:
                        return Emplacement(**res)
        except Exception as e:
            logging.info(e)
        return None

    # @log
    def obtenir_id_selon_code(self, code):
        """Renvoie l'ID d'un emplacement selon son code (INSEE).

        Parameters
        ----------
        code : int
            Le code INSEE de l'emplacement.

        Returns
        -------
        int
            L'identifiant de l'emplacement, ou None si aucun
            emplacement n'est trouvé.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_emplacement FROM projet_2A.emplacement   "
                        "WHERE code = %(code)s                              ",
                        {
                            "code": code,
                        },
                    )
                    res = cursor.fetchone()
                    if res:
                        return res["id_emplacement"]
        except Exception as e:
            logging.info(e)
        return None

    # @log
    def obtenir_id_emplacements_selon_niveau_annee(self, niveau, annee):
        """
        Trouve tous les emplacements selon l'année et le niveau

        Parameters
        ----------
        niveau : str
            Le niveau de l'emplacement à rechercher (par exemple, "commune", "département", etc.).

        annee : int
            L'année associée aux emplacements à rechercher.

        Returns
        -------
        List[int]
            Une liste contenant les identifiants des emplacements correspondant aux critères.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_emplacement                              "
                        "FROM projet_2A.emplacement                         "
                        "JOIN projet_2A.association_emplacement_contour     "
                        "USING(id_emplacement)                              "
                        "WHERE emplacement.niveau = %(niveau)s AND          "
                        "association_emplacement_contour.annee = %(annee)s; ",
                        {
                            "niveau": niveau,
                            "annee": annee,
                        },
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_id_emplacements = []

        for i in range(len(res)):
            liste_id_emplacements.append(res[i]["id_emplacement"])

        return liste_id_emplacements

    # ############################################# Modifications&Suppressions

    # @log
    def modifier_emplacement(self, id_emplacement, nouveau_nom,
                             nouveau_niveau, nouveau_code) -> bool:
        """
        Modifie un emplacement dans la base de données.

        Cette méthode permet de mettre à jour les informations d'un emplacement spécifié, en fonction
        de son identifiant. Les attributs modifiables sont le nom, le niveau et le code de l'emplacement.

        Parameters
        ----------
        id_emplacement : int
            L'identifiant unique de l'emplacement à modifier.

        nouveau_nom : str
            Le nouveau nom de l'emplacement.

        nouveau_niveau : str
            Le nouveau niveau de l'emplacement (par exemple, "commune", "département").

        nouveau_code : str
            Le nouveau code associé à l'emplacement.

        Returns
        -------
        bool
            True si la modification est un succès (exactement une ligne mise à jour),
            False sinon (aucune ligne n'a été mise à jour ou une erreur est survenue).
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE projet_2A.emplacement                       "
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

    # @log
    def supprimer_emplacement(self, id_emplacement) -> bool:
        """
        Supprime un emplacement dans la base de données.

        Cette méthode permet de supprimer un emplacement existant en fonction de son identifiant.

        Parameters
        ----------
        id_emplacement : int
            L'identifiant de l'emplacement à supprimer.

        Returns
        -------
        bool
            True si l'emplacement a bien été supprimé
            False sinon
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer l'emplacement
                    cursor.execute(
                        "DELETE FROM projet_2A.emplacement                  "
                        " WHERE id_emplacement=%(id_emplacement)s           ",
                        {"id_emplacement": id_emplacement},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
