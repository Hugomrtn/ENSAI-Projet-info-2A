import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection
from business_object.contour import Contour


class Dao_contour(metaclass=Singleton):
    def creer(self, contour: Contour):

        """Création d'un contour dans la base de données
            Parameters
            ----------

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
                        "INSERT INTO contour(id_contour) VALUES    "
                        "(%(id_contour)s)                "
                        "RETURNING id_contour;                      ",
                        {
                            "id_contour": contour.id_contour,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            contour.id_contour = res["id_contour"]
            created = True

        return created

    def modifier(self):
        pass
    # pour l'instant on fait pas, car on préfère supprimer puis ajouter plutôt que modifier

    def supprimer(self, id_contour):
        """Suppression d'un contour dans la base de données

        Parameters
        ----------


        Returns
        -------
            True si le contour a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le contour
                    cursor.execute(
                        "DELETE FROM contour                  "
                        " WHERE id_contour=%(id_contour)s      ",
                        {"id_contour": id_contour},
                    )
                    # supprime aussi toutes les assocations entre un polygone et un contour
                    cursor.execute(
                        " DELETE FROM association_contour_polygones"
                        " WHERE id_contour=%(id_contour)s      ",
                        {"id_contour": id_contour},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0


    @log
    def obtenir_id_contour_selon_id_emplacement_annne(self, id_emplacement,
                                                      annee):
        """Trouve tous les contours selon l'année et l'emplacement

        Parameters
        ----------

        Returns

        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_contour                                  "
                        "FROM association_emplacement_contour               "
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
