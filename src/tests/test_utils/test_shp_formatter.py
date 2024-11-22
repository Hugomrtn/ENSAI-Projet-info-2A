import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from utils.shp_formatter import (
    open_shp,
    reconnaissance_polygon,
    data_to_list,
    get_annee,
    get_niveau,
    get_info,
)

TEST_FILE_PATH = "1_DONNEES_LIVRAISON_2024-10-00105\ADE_3-2_SHP_LAMB93_FXX-ED2024-10-16\REGION.shp"  # NOQA


def test_open_shp():
    data, n = open_shp(TEST_FILE_PATH)
    assert n > 0  # Vérifie qu'il y a des features dans le fichier
    assert data is not None  # Vérifie que l'objet data est bien chargé


def test_reconnaissance_polygon():
    data, n = open_shp(TEST_FILE_PATH)
    is_polygon = reconnaissance_polygon(data, 0)
    assert isinstance(is_polygon, bool)


def test_data_to_list():
    """
    Test que data_to_list ne renvoie pas des objets vides.
    """
    emplacements, contours, polygones, points = data_to_list(TEST_FILE_PATH)
    assert len(emplacements) > 0
    assert len(contours) > 0
    assert len(polygones) > 0
    assert len(points) > 0


def test_data_to_list_data_integrity():
    """
    Test que la data dans emplacements, contours, polygones, et
    points retourne les bonnes informations du shp.
    """

    emplacements, contours, _, _ = data_to_list(TEST_FILE_PATH)

    for emplacement in emplacements:
        assert isinstance(emplacement.niveau, str)
        assert isinstance(emplacement.nom_emplacement, str)
        assert isinstance(emplacement.code, (int, str))
        assert isinstance(emplacement.nombre_habitants, int)
        assert isinstance(emplacement.annee, str)

    for contour in contours:
        assert isinstance(contour.polygones_composants, list)
        assert isinstance(contour.polygones_enclaves, list)


def test_data_to_list_points_coordinates():
    """
    Test pour être sur que les points sont des bonnes coordonées.
    """
    _, _, _, points = data_to_list(TEST_FILE_PATH)

    for point in points:
        assert isinstance(point.x, (int, float))
        assert isinstance(point.y, (int, float))


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
