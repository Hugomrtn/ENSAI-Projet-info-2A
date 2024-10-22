# associe les points avec un ordre pour refaire un polygone

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.point import Point


class Dao_point(metaclass=Singleton):

    @log
    def creer(self, point: Point) -> bool:
        """Création d'un point dans la base de données
            Parameters
            ----------
            point : Point

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
                        "INSERT INTO points(id_point,                   "
                        "x, y) VALUES                                   "
                        "(%(x)s, %(y)s)                                 "
                        "RETURNING id_point;                            ",
                        {
                            "x": point.x,
                            "y": point.y,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            point.id_point = res["id_point"]
            created = True

        return created

    @log
    def association_polygone_points(id_polygone, liste_id_point: list):
        """Création de la table d'association dans la base de données
        entre polygone et les points avec ordre
        Parameters
        ----------
        liste : list of (IDs)

        Returns
        -------
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    for i in range(len(liste_id_point)):
                        cursor.execute(
                            "INSERT INTO association_polygone_points(       "
                            "id_polygone, id_point, ordre) VALUES           "
                            "(%(id_polygone)s, %(id_point)s, %(ordre)s);    ",
                            {
                                "id_polygone": id_polygone,
                                "id_point": liste_id_point[i],
                                "ordre": i
                            },
                        )
        except Exception as e:
            logging.info(e)
# ############################@ pas sûr

    @log
    def existe_polygone(liste_id_point: list) -> bool:
        """Vérifie si un polygone avec cette table d'association existe déjà
        Parameters
        ----------
        liste_id_point : list of int
            Liste des ID de points associés au polygone

        Returns
        -------
        exists : bool
            True si le polygone existe, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Requête pour vérifier l'existence de la même association
                    cursor.execute(
                        """
                        SELECT id_polygone
                        FROM association_polygone_points
                        WHERE id_point = ANY(%(liste_id_point)s)
                        GROUP BY id_polygone
                        HAVING array_agg(ordre ORDER BY ordre) =
                        array_agg(%(liste_id_point)s ORDER
                        BY %(liste_id_point)s);
                        """,
                        {"liste_id_point": liste_id_point}
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            return False

        return res is not None


#######################################

    @log
    def obtenir_id_polygones_composants_selon_id_contour(self, id_contour):
        """Trouve tous les polygones qui appartiennent à un contour

        Parameters
        ----------
        id_contour : int
            ID d'un contour

        Returns
        liste_id_polygones_composants : list of int
            Liste des ID des polygones composants
            (polygone qui delimite l'exterieur de l'emplacement
            et polygones qui delimitent des enclaves a l'exterieur)
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_polygone                                 "
                        "FROM association_contours_polygones                "
                        "WHERE id_contour = %(id_contour)s                  "
                        "AND appartient = TRUE                              ",
                        {
                            "id_contour": id_contour,
                        }
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_id_polygones_composants = []

        for i in range(liste_id_polygones_composants):
            liste_id_polygones_composants.append(res["id_polygone"][i])

        return liste_id_polygones_composants

    @log
    def obtenir_id_polygones_enclaves_selon_id_contour(self, id_contour):
        """Trouve tous les polygones qui appartiennent à un contour

        Parameters
        ----------

        Returns

        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_polygone                                 "
                        "FROM association_contours_polygones                "
                        "WHERE id_contour = %(id_contour)s                  "
                        "AND appartient = FALSE                             ",
                        {
                            "id_contour": id_contour,
                        }
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_id_polygones_enclaves = []

        for i in range(liste_id_polygones_enclaves):
            liste_id_polygones_enclaves.append(res["id_polygone"][i])

        return liste_id_polygones_enclaves
