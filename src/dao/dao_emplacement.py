import logging

from utils.singleton import Singleton
# from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.emplacement import Emplacement


class Dao_emplacement(metaclass=Singleton):

    def creer(self, emplacement: Emplacement) -> bool:
        """Creation d'un emplacement dans la base de données
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
                        "INSERT INTO emplacement(id_emplacement,        "
                        "nom_emplacement, niveau, pop, annee) VALUES    "
                        "(%(id_emplacement)s, %(nom_emplacement)s,      "
                        "%(niveau)s, %(pop)s, %(annee)s)                "
                        "RETURNING id_emplacement;                      ",
                        {
                            "id_emplacement": emplacement.id_emplacement,
                            "nom_emplacement": emplacement.nom_emplacement,
                            "niveau": emplacement.niveau,
                            "pop": emplacement.pop,
                            "annee": emplacement.annee,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            emplacement.id_emplacement = res["id_emplacement"]
            created = True

        return created

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
                        "  FROM emplacement                                 "
                        " WHERE id_emplacement = %(id_emplacement)i;        ",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        return res["nom_emplacement"]

    def obtenir_informations(self, id_emplacement) -> str:
        """trouver un joueur grace à son id

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
                        "  FROM emplacement                                 "
                        " WHERE id_emplacement = %(id_emplacement)i;        ",
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        return res
