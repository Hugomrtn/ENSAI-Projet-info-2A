import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from business_object.contour import Contour # NOQA
from business_object.polygone import Polygone # NOQA
from business_object.point import Point # NOQA


@pytest.fixture
def polygone_composant():
    points = [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)]
    return Polygone(points)


@pytest.fixture
def polygone_enclave():
    points = [Point(0.25, 0.75), Point(0.75, 0.25)]
    return Polygone(points)


def test_contour_initialization(polygone_composant, polygone_enclave):
    polygones_composants = [polygone_composant]
    polygones_enclaves = [polygone_enclave]
    contour = Contour(polygones_composants=polygones_composants,
                      polygones_enclaves=polygones_enclaves)

    assert contour.polygones_composants == polygones_composants
    assert contour.polygones_enclaves == polygones_enclaves


def test_contour_with_empty_lists():
    contour = Contour(polygones_composants=[], polygones_enclaves=[])

    assert contour.polygones_composants == []
    assert contour.polygones_enclaves == []
