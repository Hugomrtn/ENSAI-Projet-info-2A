import pytest
from src.business_object.emplacement import Emplacement
from src.business_object.contour import Contour
from src.business_object.polygone import Polygone
from src.business_object.point import Point
from src.utils.shp_formatter import data_to_list


@pytest.fixture
def shp_file_path():
    return "1_DONNEES_LIVRAISON_2024-09-00118/ADE_3-2_SHP_UTM22RGFG95_GUF-ED2024-09-18/COMMUNE.shp" # NOQA


def test_data_to_list(shp_file_path):
    emplacements, contours, polygones, points = data_to_list(shp_file_path)

    assert len(emplacements) > 0, "No Emplacement objects created."
    for emplacement in emplacements:
        assert isinstance(emplacement, Emplacement)
        assert isinstance(
            emplacement.nom, str), "Emplacement.nom should be a string."
        assert isinstance(
            emplacement.niveau, str), "Emplacement.niveau should be a string."
        assert isinstance(
            emplacement.pop, int), "Emplacement.pop should be an integer."
        assert isinstance(
            emplacement.annee, int), "Emplacement.annee should be an integer."
        assert isinstance(
            emplacement.code, int), "Emplacement.code should be an integer."

    assert len(contours) > 0, "No Contour objects created."
    for contour in contours:
        assert isinstance(contour, Contour)
        assert isinstance(contour.polygones_composants, list)
        assert isinstance(contour.polygones_enclaves, list)

    assert len(polygones) > 0, "No Polygone objects created."
    for poly_list in polygones:
        for polygone in poly_list:
            assert isinstance(polygone, Polygone)
            assert isinstance(polygone.liste_points, list)
            assert all(
                isinstance(pt, Point) for pt in polygone.liste_points
                ), \
                "All items in Polygone.liste_points should be Point instances."

    assert len(points) > 0, "No Point objects created."
    for point in points:
        assert isinstance(point, Point)
        assert isinstance(
            point.x, (int, float)), "Point.x should be an int or float."
        assert isinstance(
            point.y, (int, float)), "Point.y should be an int or float."
