import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.point import Point


class Dao_point(metaclass=Singleton):

    @log
    def existe(self, point: Point) -> bool:
        """Vérifie si un point existe déjà dans la base de données
            Parameters
            ----------
            point : Point

            Returns
            -------
            existe : bool
                True si le point existe
                False sinon
            """
        existe = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_point FROM points WHERE x = %(x)s    "
                        "AND y = %(y)s;                                 ",
                        {
                            "x": point.x,
                            "y": point.y,
                        },
                    )
                    res = cursor.fetchone()
                    if res:
                        id_point = res["id_point"]
                        existe = True
        except Exception as e:
            logging.info(e)

        return [existe, id_point]

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

        existe = Dao_point.existe(point)
        if existe[0]:
            return existe[0]

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

        return res["id_point"]

    def creer_liste_de_points(liste: list):
        """Appliquer la fonction creer sur une liste de points
            Parameters
            ----------
            liste : list of Point

            Returns
            -------
            res: list (des IDs)
            """
        res = []
        for i in range(len(liste)):
            res.append(Dao_point.creer(liste[i]))
        return res

    @log
    def obtenir_points_ordonnes_selon_id_polygone(self, id_polygone):
        """Trouve tous les points qui appartiennent à un polygones de manière
        ordonnée
        -----------
        Parameters:
        --------
        Returns:
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT point.latitude, point.longitude             "
                        "FROM point JOIN association_polygone_point         "
                        "USING(id_point)                                    "
                        "WHERE id_polygone = %(id_polygone)s                "
                        "ORDER BY association_polygone_point.ordre          ",
                        {
                            "id_polygone": id_polygone,
                        }
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_points = []

        for i in range(res):
            liste_points.append(Point(res["latitude"][i], res["longitude"][i]))

        return liste_points
