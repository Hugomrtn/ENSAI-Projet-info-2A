import pytest

from service.segment_service import SegmentService
from business_object.point import Point
from business_object.segment import Segment


def test_creer_segment_ok():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    segment = SegmentService().creer(point1, point2)
    assert segment.point1 == point1
    assert segment.point2 == point2


def test_coupe_a_droite_true():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    point = Point(0.5, 0.5)
    segment = Segment(point1, point2)
    intersections = SegmentService().coupe_a_droite(segment, point)
    assert intersections == 1


def test_coupe_a_droite_false():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    point = Point(2, 2)
    segment = Segment(point1, point2)
    intersections = SegmentService().coupe_a_droite(segment, point)
    assert intersections == 0


if __name__ == "__main__":
    pytest.main([__file__])