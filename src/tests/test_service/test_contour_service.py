from unittest.mock import MagicMock
import pytest

from service.contour_service import ContourService
from dao.dao_contour import Dao_contour
from business_object.contour import Contour
from business_object.polygone import Polygone
from business_object.point import Point

liste_contours = [
    Contour([Polygone([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])], []),
    Contour([Polygone([Point(2, 2), Point(3, 2), Point(3, 3), Point(2, 3)])], [])
]


def test_creer_contour_ok():
    polygones_composants = [Polygone([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])]
    polygones_enclaves = []
    Dao_contour().creer = MagicMock(return_value=True)
    contour = ContourService().creer(polygones_composants, polygones_enclaves)
    assert contour.polygones_composants == polygones_composants
    assert contour.polygones_enclaves == polygones_enclaves


def test_creer_contour_echec():
    polygones_composants = [Polygone([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])]
    polygones_enclaves = []
    Dao_contour().creer = MagicMock(return_value=False)
    contour = ContourService().creer(polygones_composants, polygones_enclaves)
    assert contour is None


def test_lister_tous_contours():
    Dao_contour().lister_tous = MagicMock(return_value=liste_contours)
    res = ContourService().lister_tous()
    assert len(res) == 2


def test_trouver_par_id_contour_ok():
    id_contour = 1
    Dao_contour().trouver_par_id = MagicMock(return_value=liste_contours[0])
    contour = ContourService().trouver_par_id(id_contour)
    assert contour.polygones_composants[0].liste_points[0].x == 0
    assert contour.polygones_enclaves == []


def test_trouver_par_id_contour_echec():
    id_contour = 1
    Dao_contour().trouver_par_id = MagicMock(return_value=None)
    contour = ContourService().trouver_par_id(id_contour)
    assert contour is None


if __name__ == "__main__":
    pytest.main([__file__])