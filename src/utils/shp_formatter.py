import fiona


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


def data_to_list_poly_point(path):
    """
    Extrait les données du .shp vers une liste de float
    afin de les transférer plus tard dans une bdd
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
    print(data)
    Liste_Polygone = []
    Liste_X = []
    Liste_Y = []
    for i in range(n):
        geometry = data[i]["geometry"]["coordinates"]

        if reconnaissance_polygon(data, i):
            Liste_Polygone.append(geometry)
            for point in geometry[0]:
                Liste_X.append(point[0])
                Liste_Y.append(point[1])
        else:
            for multi_polygon in geometry:
                for polygon in multi_polygon[0]:
                    Liste_Polygone.append(polygon)
                    for point in multi_polygon[0]:
                        Liste_X.append(point[0])
                        Liste_Y.append(point[1])
    return Liste_Polygone, Liste_X, Liste_Y


P, X, Y = data_to_list_poly_point("1_DONNEES_LIVRAISON_2024-09-00118/ADE_3-2_SHP_RGAF09UTM20_GLP-ED2024-09-18/CANTON.shp")

