import fiona
from src.dao.dao_emplacement import Dao_emplacement
from src.dao.dao_contour import Dao_contour
from src.dao.dao_polygone import Dao_polygone
from src.dao.dao_point import Dao_point


def open_shp(path):
    data = fiona.open(path, 'r')
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
    Extrait les données du .shp vers une liste
    afin de les transférer dans une bdd
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
    EmplacementDAO = Dao_emplacement()
    ContourDAO = Dao_contour()
    PolygoneDAO = Dao_polygone()
    PointDAO = Dao_point()
    for i in range(n):
        Population, Code_Insee, Nom = get_info(path, i)
        Emplacement = [
            Nom,
            get_niveau(path),
            Population,
            get_annee(path),
            Code_Insee
            ]
        emplacement_id = EmplacementDAO.creer(Emplacement)
        Emplacement = [
            emplacement_id,
            Nom,
            get_niveau(path),
            Population,
            get_annee(path),
            Code_Insee
            ]
        contour_id = ContourDAO.creer()
        Contour = [contour_id]
        geometry = data[i]["geometry"]["coordinates"]
        Points = []
        Poly_Composant = []
        Poly_Enclave = []
        Polygones = [Poly_Composant, Poly_Enclave]
        if reconnaissance_polygon(data, i):     # Un Polygone simple
            id_poly = PolygoneDAO.creer()
            Poly = [id_poly, geometry[0]]
            Poly_Composant.append(Poly)
            for point in geometry[0]:
                PointDAO = Dao_point()
                X = point[0]
                Y = point[1]
                Point_id = PointDAO.creer([X, Y])
                Point = [Point_id, X, Y]
                Points.append(Point)
        else:       # Un Multi-Polygone
            for multi_polygon in geometry:
                for polygon in multi_polygon[0]:
                    id_poly = PolygoneDAO.creer()
                    Poly = [id_poly, polygon]
                    Poly_Enclave.append(Poly)
                    for point in multi_polygon[0]:
                        X = point[0]
                        Y = point[1]
                        Point_id = PointDAO.creer([X, Y])
                        Point = [Point_id, X, Y]
                        Points.append(Point)
    return Emplacement, Contour, Polygones, Points


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
    return path[75: n - 4]


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
        Code_INSEE = prop["INSEE_" + niveau[:3]]
    else:
        Code_INSEE = -1
    if "NOM_M" in prop:
        Nom = prop["NOM_M"]
    else:
        Nom = "Pas de Nom"

    return Population, Code_INSEE, Nom


path = ("1_DONNEES_LIVRAISON_2024-09-00118/ADE_3-2_SHP_UTM22RGFG95_" +
        "GUF-ED2024-09-18/REGION.shp")
Emplacement, Contour, Polygones, Points = data_to_list(path)
print(Emplacement)
