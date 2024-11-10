from src.utils.shp_formatter import (
    open_shp,
    reconnaissance_polygon,
    data_to_list,
    get_annee,
    get_niveau,
    get_info,
)

# Remplacez par le chemin réel vers votre fichier de test
TEST_FILE_PATH = "1_DONNEES_LIVRAISON_2024-10-00105/ADE_3-2_SHP_LAMB93_FXX-ED2024-10-16/REGION.shp"  # NOQA


def test_open_shp():
    data, n = open_shp(TEST_FILE_PATH)
    assert n > 0  # Vérifie qu'il y a des features dans le fichier
    assert data is not None  # Vérifie que l'objet data est bien chargé


def test_reconnaissance_polygon():
    data, n = open_shp(TEST_FILE_PATH)
    is_polygon = reconnaissance_polygon(data, 0)
    assert isinstance(is_polygon, bool)


def test_data_to_list():
    emplacements, contours, polygones, points = data_to_list(TEST_FILE_PATH)
    assert len(emplacements) > 0
    assert len(contours) > 0
    assert len(polygones) > 0
    assert len(points) > 0


def test_get_annee():
    assert get_annee(TEST_FILE_PATH) == "2024"


def test_get_niveau():
    path = "1_DONNEES_LIVRAISON_2024-10-00105/ADE_3-2_SHP_LAMB93_FXX-ED2024-10-16/REGION.shp"  # NOQA
    assert get_niveau(path) == "REGION"


def test_get_info():
    data, n = open_shp(TEST_FILE_PATH)
    population, code_insee, nom = get_info(TEST_FILE_PATH, 0)
    assert isinstance(population, int)
    assert isinstance(code_insee, int)
    assert isinstance(nom, str)
