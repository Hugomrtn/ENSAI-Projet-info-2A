import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from business_object.point import Point # noqa


def test_point_initialisation():
    point = Point(1.5, 2.5)

    assert point.x == 1.5
    assert point.y == 2.5


def test_point_initialisation_erreur():
    pass


def test_point_repr():
    point = Point(1.5, 2.5)
    assert repr(point) == "(1.5, 2.5)"
