import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.point import Point


class Dao_point(metaclass=Singleton):

    # ############################################# Créations

    def creer(self, point: Point) -> bool:
        """
        Crée un point dans la base de données.

        Parameters
        ----------
        point : Point
            L'objet Point à insérer dans la base de données

        Returns
        -------
        bool
            Si le point existe déjà, retourne l'ID du point existant.
            Sinon, retourne l'ID du nouveau point créé dans la base de données
        """

        existe = Dao_point().existe(point)
        if existe[0]:
            return existe[1]

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_2A.points(x, y) VALUES          "
                        "(%(x)s, %(y)s)                                     "
                        "RETURNING id_point;                                ",
                        {
                            "x": point.x,
                            "y": point.y,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_point"]

    # ############################################# Existence

    def existe(self, point: Point):
        """
        Vérifie si un point existe déjà dans la base de données

        Parameters
        ----------
        point : Point

        Returns
        -------
        existe : bool
            [True, id_point] s'il existe
            [False, None] sinon
        """
        existe = False
        id_point = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_point FROM projet_2A.points              "
                        "WHERE x = %(x)s AND y = %(y)s;                     ",
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

    # ############################################# Obtenir informations

    @log
    def obtenir_points_ordonnes_selon_id_polygone(self, id_polygone):
        """
        Récupère tous les points ordonnés associés à un polygone

        Parameters
        ----------
        id_polygone : int
            L'ID du polygone pour lequel on veut obtenir les points

        Returns
        -------
        liste_points : list of Point
            Liste ordonnée des points
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT points.x, points.y                          "
                        "FROM projet_2A.points                              "
                        "JOIN projet_2A.association_polygone_points         "
                        "USING(id_point)                                    "
                        "WHERE id_polygone = %(id_polygone)s                "
                        "ORDER BY association_polygone_points.ordre         ",
                        {
                            "id_polygone": id_polygone,
                        }
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_points = []
        for i in range(len(res)):
            liste_points.append(Point(res[i]["x"], res[i]["y"]))

        return liste_points

    @log
    def obtenir_id_selon_point(self, point: Point):
        """
        Récupère l'ID du point si celui-ci existe déjà dans la base de données.

        Parameters
        ----------
        point : Point
            L'objet Point pour lequel on veut récupérer l'ID dans la base de
            données

        Returns
        -------
        id_point : int
            L'ID du point si celui-ci existe dans la base de données,
            sinon None
        """

        informations_existence = Dao_point.existe(point)
        if informations_existence[0]:
            return informations_existence[1]

    @log
    def obtenir_point_selon_id(self, id_point):
        """
        Récupère les coordonnées (x, y) d'un point en utilisant son identifiant

        Parameters
        ----------
        id_point : int
            L'identifiant du point pour lequel on souhaite récupérer les
            coordonnées

        Returns
        -------
        point : Point
            L'objet Point si l'ID existe. None sinon
        """

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT x, y FROM projet_2A.point                   "
                        "WHERE id_point = %(id_point)s                      ",
                        {
                            "id_point": id_point,
                        },
                    )
                    res = cursor.fetchone()
                    if res:
                        return Point(res["x"], res["y"])

        except Exception as e:
            logging.info(e)
