from src.business_object.point import Point
from src.business_object.point import Segment


class geometrie:

    def est_dans_polygone(polygone: list, point: Point):
        """Ray-casting qui permet de déterminer si un point se trouve dans un
        polygone."""

        # initialisations
        intersections = 0

        for i in range(len(polygone)):
            point1 = Point(polygone[i])
            point2 = Point(polygone[(i + 1) % len(polygone)])
            segment = Segment(point1, point2)
            intersections += segment.coupe_a_droite(point)

        return intersections % 2 == 1

    def est_dans_liste_polygones(liste_polygones: list, point: list):
        b = False
        for i in range(liste_polygones):
            b = geometrie.est_dans_polygone(liste_polygones[i], point)
            if b:
                break
        return b
