import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.emplacement import Emplacement


class Dao_emplacement(metaclass=Singleton):

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

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO emplacement(id_emplacement,       "
                        "nom_emplacement, niveau, pop, annee) VALUES    "
                        "(%(id_emplacement)s, %(nom_emplacement)s,      "
                        "%(niveau)s, %(code)s)                "
                        "RETURNING id_emplacement;                      ",
                        {
                            "id_emplacement": emplacement.id_emplacement,
                            "nom_emplacement": emplacement.nom_emplacement,
                            "niveau": emplacement.niveau,
                            "code": emplacement.code,
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
                        "  FROM emplacement                                "
                        " WHERE id_emplacement = %(id_emplacement)i;        ",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        return res["nom_emplacement"]

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
                        "  FROM emplacement                                "
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
                        "FROM emplacement                                  "
                        "JOIN association_emplacement_contour               "
                        "USING(id_emplacement)                              "
                        "WHERE emplacement.niveau = %(niveau)s              "
                        "AND association_emplacement_contour.annee = %(annee)s;   ",
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

    def modifier_emplacement(self, id_emplacement, nouveau_nom, nouveau_niveau, nouveau_code) -> bool:
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
                        "UPDATE emplacement                                      "
                        "   SET niveau      = %(niveau)s,                   "
                        "       nom         = %(nom)s,                      "
                        "       code         = %(code)s,                      "
                        " WHERE id_emplacement = %(id_emplacement)s;                  ",
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
                        "DELETE FROM emplacement                  "
                        " WHERE id_emplacement=%(id_emplacement)s      ",
                        {"id_emplacement": id_emplacement},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
