# test_point_service.py

from unittest.mock import MagicMock
import pytest

from service.point_service import PointService
from dao.dao_point import Dao_point
from business_object.point import Point

liste_points = [
    Point(0, 0),
    Point(1, 0),
    Point(1, 1),
    Point(0, 1),
]


def test_creer_point_ok():
    x, y = 10, 20
    Dao_point().creer = MagicMock(return_value=True)
    point = PointService().creer(x, y)
    assert point.x == x
    assert point.y == y


def test_creer_point_echec():
    x, y = 10, 20
    Dao_point().creer = MagicMock(return_value=False)
    point = PointService().creer(x, y)
    assert point is None


def test_lister_tous_points():
    Dao_point().lister_tous = MagicMock(return_value=liste_points)
    res = PointService().lister_tous()
    assert len(res) == 4


def test_trouver_par_id_point_ok():
    id_point = 1
    Dao_point().trouver_par_id = MagicMock(return_value=liste_points[0])
    point = PointService().trouver_par_id(id_point)
    assert point.x == 0
    assert point.y == 0


def test_trouver_par_id_point_echec():
    id_point = 1
    Dao_point().trouver_par_id = MagicMock(return_value=None)
    point = PointService().trouver_par_id(id_point)
    assert point is None


if __name__ == "__main__":
    pytest.main([__file__])