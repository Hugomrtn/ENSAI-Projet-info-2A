import fiona


def open_shp(path):
    data = fiona.open(path, 'r')
    n = len(data)  # Nombres de features
    return data, n


def data_to_list(path):
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
        Poly_i = data[i]['geometry']['coordinates']
        k = len(Poly_i)
        Liste_Polygone.append(Poly_i)
        if len(Poly_i) == 2:
            Liste_X.append(Poly_i[0])
            Liste_Y.append(Poly_i[1])
        else:
            for j in range(k):
                print(Poly_i)
                Liste_X.append(Poly_i[j][0])
                Liste_Y.append(Poly_i[j][1])
    return Liste_Polygone, Liste_X, Liste_Y

# La fonction marche elle ressort les bons trucs et comme elle traite
# Les trucs dans l'ordre je pense qu'il y a pas de soucis mais on peut
# Toujours faire le lien avec la DAO en rajoutant des fonction existe etc,
# tu me diras quand je pourrai les implementer

# print(
    # data_to_list(
    #     "1_DONNEES_LIVRAISON_2024-09-00118"
    #     + "/ADE_3-2_SHP_UTM22RGFG95_GUF-ED2024-09-18/CHFLIEU_COMMUNE.shp")
    # )
