import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from business_object.point import Point # NOQA
from business_object.polygone import Polygone # NOQA


@pytest.fixture
def square_polygone():
    points = [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)]
    return Polygone(points)


def test_point_inside(square_polygone):
    point_inside = Point(0.5, 0.5)

    assert square_polygone.polygone_contient_point(point_inside) is True


def test_point_outside(square_polygone):
    point_outside = Point(1.5, 1.5)

    assert square_polygone.polygone_contient_point(point_outside) is False


def test_point_on_edge(square_polygone):
    point_on_edge = Point(1, 0.5)

    assert square_polygone.polygone_contient_point(point_on_edge) is True
