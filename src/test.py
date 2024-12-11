from random import randint
from dao.dao_contour import Dao_contour
from dao.dao_emplacement import Dao_emplacement
from dao.dao_point import Dao_point
from dao.dao_polygone import Dao_polygone

from business_object.point import Point
from business_object.polygone import Polygone
from business_object.contour import Contour
from business_object.emplacement import Emplacement

from dao.db_connection import DBConnection
from utils.reset_database import ResetDatabase

from utils.shp_formatter import data_to_list, creer_bdd_par_niveau
from service.service_utilisateur import Service_utilisateur

import time

path_region = "1_DONNEES_LIVRAISON_2024-10-00106/ADE_3-2_SHP_WGS84G_FRA-ED2024-10-16/REGION.shp"
path_commune = "1_DONNEES_LIVRAISON_2024-10-00106/ADE_3-2_SHP_WGS84G_FRA-ED2024-10-16/COMMUNE.shp"


def initialiser_bdd(path):
    start_time = time.time()
    print("début")
    print(time.ctime())
    creer_bdd_par_niveau(path)
    print("--- %s seconds ---" % (time.time() - start_time))


def fonc1():
    start_time = time.time()
    point1 = Point(2.285868743450239, 48.861019721989436)  # long lat
    print("point1")
    print(Service_utilisateur().fonction2_obtenir_emplacement_selon_point_niveau_annee(
        "REGION", 2024, point1))
    print("--- %s seconds ---" % (time.time() - start_time))


def fonc2():
    start_time = time.time()
    emplacements, contours, polygones, points = data_to_list(path_region)
    for i in range(len(contours)):
        print(emplacements[i].nom_emplacement)
        print(i)
        print(len(contours[i].polygones_composants))
        print(len(contours[i].polygones_enclaves))
    print("--- %s seconds ---" % (time.time() - start_time))


fonc1()
