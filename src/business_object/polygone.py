from src.business_object.point import Point
from src.business_object.segment import Segment


class Polygone:
    """Classe représentant un polygone
    Attributs
    ----------
    liste_points: list[Point]
        liste des points formant le polygone
    """
    def __init__(self, liste_points: list[Point]):
        self.liste_points = liste_points

    def est_dans_polygone(self, point: Point):
        """Ray-casting qui permet de déterminer si un point se trouve dans un
        polygone."""

        intersections = 0

        for i in range(len(self.liste_points)):
            point1 = Point(self.liste_points[i])
            point2 = Point(self.liste_points[(i + 1) % len(self.liste_points)])
            segment = Segment(point1, point2)
            intersections += segment.coupe_a_droite(point)

        return intersections % 2 == 1
