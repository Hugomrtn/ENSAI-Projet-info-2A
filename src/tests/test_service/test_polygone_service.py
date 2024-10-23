# test_polygone_service.py

from unittest.mock import MagicMock
import pytest

from service.polygone_service import PolygoneService
from dao.dao_polygone import Dao_polygone
from business_object.polygone import Polygone
from business_object.point import Point

liste_polygones = [
    Polygone([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]),
    Polygone([Point(2, 2), Point(3, 2), Point(3, 3), Point(2, 3)]),
]


def test_creer_polygone_ok():
    liste_points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    Dao_polygone().creer = MagicMock(return_value=True)
    polygone = PolygoneService().creer(liste_points)
    assert polygone.liste_points == liste_points


def test_creer_polygone_echec():
    liste_points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    Dao_polygone().creer = MagicMock(return_value=False)
    polygone = PolygoneService().creer(liste_points)
    assert polygone is None


def test_lister_tous_polygones():
    Dao_polygone().lister_tous = MagicMock(return_value=liste_polygones)
    res = PolygoneService().lister_tous()
    assert len(res) == 2


def test_trouver_par_id_polygone_ok():
    id_polygone = 1
    Dao_polygone().trouver_par_id = MagicMock(return_value=liste_polygones[0])
    polygone = PolygoneService().trouver_par_id(id_polygone)
    assert polygone.liste_points[0].x == 0
    assert polygone.liste_points[0].y == 0


def test_trouver_par_id_polygone_echec():
    id_polygone = 1
    Dao_polygone().trouver_par_id = MagicMock(return_value=None)
    polygone = PolygoneService().trouver_par_id(id_polygone)
    assert polygone is None


if __name__ == "__main__":
    pytest.main([__file__])