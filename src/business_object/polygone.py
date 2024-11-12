import sys
import os

parent_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
    )

sys.path.append(parent_directory)

from business_object.point import Point # NOQA
from business_object.segment import Segment # NOQA


class Polygone:
    """Classe représentant un polygone
    Parameters
    ----------
    liste_points: list[Point]
        liste des points formant le polygone
    """
    def __init__(self, liste_points: list[Point]):
        self.liste_points = liste_points

    def polygone_contient_point(self, point: Point):
        """Ray-casting qui permet de déterminer si un point se trouve dans un
        polygone."""

        intersections = 0
        n = len(self.liste_points)

        for i in range(n):
            point1 = self.liste_points[i]
            point2 = self.liste_points[(i + 1) % n]
            segment = Segment(point1, point2)
            intersections += segment.coupe_a_droite(point)
        return intersections % 2 == 1

######

    def __str__(self):
        return (
            f"(Polygones comportant {self.liste_points})"
        )

    def __repr__(self):
        return (
            f"({self.liste_points})"
        )
