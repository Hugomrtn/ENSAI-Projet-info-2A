import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.point import Point

# dans creer penser à retourner l'id du point et aussi
# vérifier qu'il n'existe pas déjà auquel cas renvoyer l'id existant


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
                        point.id_point = res["id_point"]
                        existe = True
        except Exception as e:
            logging.info(e)

        return existe
