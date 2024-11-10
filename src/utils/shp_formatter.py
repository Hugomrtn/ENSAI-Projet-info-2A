import fiona
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from business_object.emplacement import Emplacement  # NOQA
from business_object.contour import Contour  # NOQA
from business_object.polygone import Polygone  # NOQA
from business_object.point import Point  # NOQA


def open_shp(path):
    data = fiona.open(path, "r")
    n = len(data)  # Nombres de features
    return data, n


def reconnaissance_polygon(data, i):
    """
    Reconnait si on travaille avec un polygon ou un multipolygon.
    Facilite la prise en charge et le transfert des donnees vers la BDD.

    ---------------
    Parameters :
        path : str, le chemin du fichier.shp à traiter

    ---------------
    Returns :
        bool : True si un polygon, False si un multipolygon

    """
    b = True  # On initialise le booleen a True
    if len(data[i]["geometry"]["coordinates"]) == 1:
        return b
    else:
        b = False
        return b


def data_to_list(path):
    """
    Extrait les données du .shp vers une bdd
    ----------------
    Parameters:
        path : str, le chemin du fichier.shp à traiter

    ----------------
    Returns:
        Liste_Poly : list, Liste des polygones
        Liste_X : list, Liste des points X formant les polygones
        Liste_Y : list, Liste des points Y formant les polygones
    """

    data, n = open_shp(path)
    emplacements = []
    contours = []
    polygones = []
    points = []

    for i in range(n):

        # Emplacement
        population, code_insee, nom = get_info(path, i)
        niveau = get_niveau(path)
        annee = get_annee(path)
        emplacement = Emplacement(
            niveau=niveau,
            nom_emplacement=nom,
            code=code_insee,
            nombre_habitants=population,
            annee=annee,
        )
        emplacements.append(emplacement)

        # Polygones
        geometry = data[i]["geometry"]["coordinates"]
        poly_composants = []
        poly_enclaves = []

        # Contour
        contour = Contour(
            polygones_composants=poly_composants,
            polygones_enclaves=poly_enclaves
        )
        contours.append(contour)

        if reconnaissance_polygon(data, i):  # Polygone simple
            points_for_polygon = [
                (x := pt[0], y := pt[1]) for pt in geometry[0]  # NOQA
            ]
            polygone = Polygone(points_for_polygon)
            poly_composants.append(polygone)
            points.extend(points_for_polygon)
        else:  # Multi-Polygon
            for multi_polygon in geometry:
                points_for_multi_polygon = []
                for pt in multi_polygon[0]:
                    if isinstance(pt, tuple) is False:
                        continue
                    else:
                        x = pt[0]
                        y = pt[1]
                    points_for_multi_polygon.append(Point(x, y))
                polygone = Polygone(points_for_multi_polygon)
                poly_enclaves.append(polygone)
                points.extend(points_for_multi_polygon)

        # Ajout des polygones aux contours
        contour.polygones_composants = poly_composants
        contour.polygones_enclaves = poly_enclaves
        polygones.append(poly_composants + poly_enclaves)

    return emplacements, contours, polygones, points


def get_annee(path):
    """
    Recupere l'annee du chemin.
    -----------------
    Parameters:
        path : str, le chemin du fichier

    -----------------
    Returns :
        annee : int, l'annee des differentes informations
    """
    return path[20:24]


def get_niveau(path):
    """
    Recupere le niveau du chemin.
    -----------------
    Parameters:
        path : str, le chemin du fichier

    -----------------
    Returns :
        niveau : str, le niveau des differentes informations
    """
    n = len(path)
    return path[70:n - 4]


def get_info(path, i):
    """
    Extrait les données du .shp afin de les transférer selon chaque ligne
    ----------------
    Parameters:
        path : str, le chemin du fichier.shp à traiter

    ----------------
    Returns:
        Population : int, le nombre d'habitants suivant le niveau, -1 sinon
        Code_INSEE : int, le code insee suivant le niveau, -1 sinon
    """
    niveau = get_niveau(path)
    data, n = open_shp(path)
    prop = data[i]["properties"]

    if "POPULATION" in prop:
        Population = prop["POPULATION"]
    else:
        Population = -1

    if "INSEE_" + niveau[:3] in prop:
        Code_INSEE = int(prop["INSEE_" + niveau[:3]])
    else:
        Code_INSEE = -1

    if "NOM_M" in prop:
        Nom = prop["NOM_M"]
    else:
        Nom = "Pas de Nom"

    return Population, Code_INSEE, Nom
