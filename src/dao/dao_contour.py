import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection
from dao.dao_polygone import Dao_polygone

from business_object.contour import Contour


class Dao_contour(metaclass=Singleton):

    # ############################################# Créations

    @log
    def creer(self):
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO contour DEFAULT VALUES"
                        "RETURNING id_contour;",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_contour"]

    @log
    def creer_association_polygone_contour(self, id_contour, id_polygone,
                                           appartient):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO association_contours_polygones(        "
                        "id_contour, id_polygone, appartient) VALUES        "
                        "(%(id_contour)s, %(id_polygone)s, %(appartient)s)  ",
                        {
                            "id_contour": id_contour,
                            "id_polygone": id_polygone,
                            "appartient": appartient,
                        },
                    )
        except Exception as e:
            logging.info(e)

    @log
    def creer_entierement_contour(self, contour: Contour):
        id_contour = Dao_contour.creer()

        for polygone in contour.polygones_composants:
            id_polygones_composants = \
                Dao_polygone.creer_entierement_polygone(polygone)
            Dao_contour.creer_association_polygone_contour(
                id_contour, id_polygones_composants, True)

        for polygone in contour.polygones_enclaves:
            id_polygones_enclaves = \
                Dao_polygone.creer_entierement_polygone(polygone)
            Dao_contour.creer_association_polygone_contour(
                id_contour, id_polygones_enclaves, False)

        return id_contour

    # ############################################# Obtenir informations

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

    # ############################################# Modifications&Suppressions

    @log
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
                    # supprime aussi toutes les assocations entre un polygone
                    # et un contour
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
