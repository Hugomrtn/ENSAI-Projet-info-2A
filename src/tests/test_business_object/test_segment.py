import pytest
from src.business_object.point import Point
from src.business_object.segment import Segment


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


def test_segment_coupe_a_droite_horizontal(segment_horizontal):
    point_below = Point(2, -1)  # Sous le segment
    point_above = Point(2, 1)    # Au dessus du segment
    point_on_segment = Point(2, 0)  # Sur le segment

    assert segment_horizontal.coupe_a_droite(point_below) == 1
    assert segment_horizontal.coupe_a_droite(point_above) == 0
    assert segment_horizontal.coupe_a_droite(point_on_segment) == 0


def test_segment_coupe_a_droite_vertical(segment_vertical):
    point_left = Point(1, 1)   # a gauche du segment
    point_right = Point(3, 1)   # a droite du segment
    point_on_segment = Point(2, 0)  # Sous le segment
    point_on_segment_above = Point(2, 2)  # Au dessus du segment

    assert segment_vertical.coupe_a_droite(point_left) == 1
    assert segment_vertical.coupe_a_droite(point_right) == 0
    assert segment_vertical.coupe_a_droite(point_on_segment) == 0
    assert segment_vertical.coupe_a_droite(point_on_segment_above) == 1

