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

    def association_polygone_points(id_polygone, liste: list):
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
                    for i in range(len(liste)):
                        cursor.execute(
                            "INSERT INTO association_polygone_points(       "
                            "id_polygone, id_point, ordre) VALUES           "                       "
                            "(%(id_polygone)s, %(id_point)s, %(ordre)s)     "                                "
                            #"RETURNING ???;                            ",
                            {
                                "id_polygone": id_polygone,
                                "id_point": liste[i],
                                "ordre": i
                            },
                        )
        except Exception as e:
            logging.info(e)
