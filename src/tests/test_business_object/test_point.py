from src.business_object.point import Point


def test_point_initialization():
    point = Point(1.5, 2.5)

    assert point.x == 1.5
    assert point.y == 2.5


def test_point_negative_coordinates():
    point = Point(-1.5, -2.5)

    assert point.x == -1.5
    assert point.y == -2.5
