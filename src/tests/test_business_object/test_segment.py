import pytest
import sys
import os

parent_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
    )

sys.path.append(parent_directory)

from business_object.point import Point # NOQA 
from business_object.segment import Segment # NOQA


@pytest.fixture
def segment_horizontal():
    point1 = Point(0, 0)
    point2 = Point(5, 0)
    return Segment(point1, point2)


@pytest.fixture
def segment_vertical():
    point1 = Point(2, -1)
    point2 = Point(2, 3)
    return Segment(point1, point2)


def test_segment_vertical():
    segment = Segment(Point(2, 1), Point(2, 3))
    assert segment.coupe_a_droite(Point(1, 2)) == 0  # gauche
    assert segment.coupe_a_droite(Point(3, 2)) == 0  # droite
    assert segment.coupe_a_droite(Point(2, 4)) == 0  # au dessus
    assert segment.coupe_a_droite(Point(2, 0)) == 0  # sous


def test_segment_horizontal():
    segment = Segment(Point(1, 2), Point(3, 2))
    assert segment.coupe_a_droite(Point(2, 1)) == 1  # dessous
    assert segment.coupe_a_droite(Point(2, 3)) == 0  # au dessus
    assert segment.coupe_a_droite(Point(4, 2)) == 1  # droite
    assert segment.coupe_a_droite(Point(0, 2)) == 0  # gauche
