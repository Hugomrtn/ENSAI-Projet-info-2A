import logging

from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.dao_point import Dao_point

from business_object.polygone import Polygone


class Dao_polygone(metaclass=Singleton):

    def creer(self):
        """
        Création d'un polygone dans la base de données (seulement l'ID)
        Parameters
        ----------

        Returns
        -------
        id_polygone : int
            ID du polygone
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_2A.polygone DEFAULT VALUES "
                        "RETURNING id_polygone;",
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        return res["id_polygone"]

    def creer_association_polygone_point(self, id_polygone, id_point,
                                         ordre):
        """Création d'un lien entre un polygone et un point dans la bdd

            Parameters
            ----------
            id_polygone : int
                ID du polygone
            id_point : int
                ID du point
            ordre : int
                Numéro qui indique l'ordre des points dans le polygone

            Returns
            -------
            """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO projet_2A.association_polygone_points(
                            id_polygone, id_point, ordre
                        ) VALUES (
                            %(id_polygone)s, %(id_point)s, %(ordre)s
                        )
                        """,
                        {
                            "id_polygone": id_polygone,
                            "id_point": id_point,
                            "ordre": ordre,
                        },
                    )
        except Exception as e:
            logging.info(e)

    def creer_entierement_polygone(self, polygone: Polygone):
        """
        Création complete d'un polygone dans la base de données

        Parameters
        ----------
        polygone : Polygone
            Polygone à créer.

        Returns
        -------
        id_polygone : int
            L'identifiant du polygone créé ou existant dans la base de données.
        """

        """existe = Dao_polygone().existe(polygone)
        if existe[0]:
            id_polygone = existe[1]
        else:
            id_polygone = Dao_polygone().creer()"""
        id_polygone = Dao_polygone().creer()  # a supprimer si on veut existe
        for i in range(len(polygone.liste_points)):
            id_point = Dao_point().creer(polygone.liste_points[i])
            Dao_polygone().creer_association_polygone_point(
                id_polygone, id_point, i
            )

        return id_polygone

# ############################ Existence

    def existe(self, polygone: Polygone):
        """
        Vérifie l'existence d'un polygone dans la base de données

        Parameters
        ----------
        polygone : Polygone

        Returns
        -------
        list
            Une liste où le premier élément est un booléen indiquant si
            le polygone existe dans la base de données, et le deuxième élément
            est l'identifiant du polygone si trouvé
        """

        id_polygone = None

        liste_id_points = []
        for point in polygone.liste_points:
            existence_point = Dao_point().existe(point)
            liste_id_points.append(existence_point[1])
            if not existence_point[0]:
                return [False, id_polygone]

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_polygone, id_point, ordre "
                        "FROM projet_2A.association_polygone_points "
                        "ORDER BY id_polygone, ordre",
                    )
                    liste = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        polygones = {}
        for ligne in liste:
            id_polygone = ligne['id_polygone']
            id_point = ligne['id_point']

            if id_polygone not in polygones:
                polygones[id_polygone] = []

            polygones[id_polygone].append(id_point)

        for id_polygone, polygon_point_ids in polygones.items():
            if liste_id_points == polygon_point_ids:
                return [True, id_polygone]

        return [False, None]

    # #######################################

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
                        "FROM projet_2A.association_contours_polygones      "
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

        for i in range(len(res)):
            liste_id_polygones_composants.append(res[i]["id_polygone"])

        return liste_id_polygones_composants

    def obtenir_id_polygones_enclaves_selon_id_contour(self, id_contour):
        """Trouve tous les polygones qui sont enclavés par rapport à un contour

        Parameters
        ----------
        id_contour : int
            ID d'un contour

        Returns
        liste_id_polygones_enclaves : list of int
            Liste des ID des polygones enclavés
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_polygone                                 "
                        "FROM projet_2A.association_contours_polygones      "
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

        for i in range(len(res)):
            liste_id_polygones_enclaves.append(res[i]["id_polygone"])

        return liste_id_polygones_enclaves

    def instancier_polygone_selon_id_polygone(self, id_polygone):
        """
        Instancie un object Polygone depuis son id.

        Parameters
        ----------
        id_polygone : int
            L'identifiant du polygone à instancier

        Returns
        -------
        Polygone
        """
        liste_points = Dao_point().\
            obtenir_points_ordonnes_selon_id_polygone(id_polygone)
        return Polygone(liste_points)
