# ON PEUT STOCKER TOUS LES POINTS INDIVIDUELLEMENT
# ET POUR STOCKER UNE LISTE, ON POURRA JUSTE STOCKER A LA SUITE DANS UN
# MEME INT PAR EX TOUS LES ID DES POINTS DANS LE BON ORDRE

# Associe les polygones qui forment un contour et ceux à soustraire

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.contour import Contour


class Dao_contour(metaclass=Singleton):
    def creer(self):
        pass

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
