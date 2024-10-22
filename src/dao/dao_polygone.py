# associe les points avec un ordre pour refaire un polygone

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection
from dao.dao_point import Dao_point

from business_object.polygone import Polygone


class Dao_polygone(metaclass=Singleton):

    @log
    def creer(self):

        """Création d'un polygone dans la base de données
        Sans dire les points qui le constitue (donc juste creation de l'ID)
            Parameters
            ----------

            Returns
            -------
            id_polygone : int
                ID du polygone cree (ID cree automatiquement)
            """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO polygone DEFAULT VALUES"
                        "RETURNING id_polygone;",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_polygone"]

    def creer_association_polygone_point(self, id_polygone, id_point,
                                         ordre):
        """Création d'un lien entre un polygone et un point
            (un polygone pourra avoir plusieurs liens) dans la base de données
            Parameters
            ----------
            id_polygone : int
                ID du polygone a associer
            id_point : int
                ID du point a associer
            ordre : int
                Numero pour savoir le rang du polygone
                (1 signifie que c'est le polygone principal
                2 ou plus signifie que c'est une enclave a l'interieur
                du polygone principal)

            Returns
            -------
            """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO association_polygone_points(        "
                        "id_polygone, id_point, ordre) VALUES        "
                        "(%(id_polygone)s, %(id_point)s, %(ordre)s)  ",
                        {
                            "id_polygone": id_polygone,
                            "id_point": id_point,
                            "ordre": ordre,
                        },
                    )
        except Exception as e:
            logging.info(e)

    def creer_entierement_polygone(self, polygone: Polygone):
        """Création complete d'un polygone dans la base de données
        (avec les points qui le composent)
            Parameters
            ----------
            Returns
            -------
            id_polygone
            """
        id_polygone = Dao_polygone.creer()

        for i in range(polygone.liste_points):
            id_point = Dao_point.creer(polygone.liste_points[i])
            Dao_polygone.creer_association_polygone_point(
                id_polygone, id_point, i
            )

        return id_polygone

# ############################ existence pas sur

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

    # #######################################

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

        for i in range(res):
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

        for i in range(res):
            liste_id_polygones_enclaves.append(res["id_polygone"][i])

        return liste_id_polygones_enclaves
