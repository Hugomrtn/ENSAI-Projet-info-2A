from business_object.point import Point


class Segment:
    """Classe représentant un segment
    Attributs
    ----------
    point1: Point
    point2: Point
    """
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def coupe_a_droite(self, point: Point) -> int:
        """Retourne 1 si le segment coupe le rayon à droite du point donné,
        sinon 0."""

        if self.point1.x == self.point2.x:
            if (
                point.x < self.point1.x and (
                    (min(self.point1.y, self.point2.y) < point.y <= max(
                        self.point1.y, self.point2.y)
                     )
                    )
            ):
                return 1
            if point.x == self.point1.x and (
                point.y > max(self.point1.y, self.point2.y)
            ):
                return 1
            return 0

        if self.point1.y == self.point2.y:
            if (
                point.y < self.point1.y and (
                    (min(self.point1.x, self.point2.x) <= point.x <= max(
                        self.point1.x, self.point2.x)
                     )
                    )
            ):
                return 1
            if point.y == self.point1.y and (
                point.x > max(self.point1.x, self.point2.x)
            ):
                return 1
            return 0

        intersection = 0
        if (
            (
                min(self.point1.y, self.point2.y) < point.y <= max(
                    self.point1.y, self.point2.y
                    )
                ) and (
                    point.x <= max(self.point1.x, self.point2.x)
                    )
        ):
            if self.point1.y != self.point2.y:
                intersection_x = (
                    (point.y - self.point1.y) * (
                        self.point2.x - self.point1.x) / (
                            self.point2.y - self.point1.y
                            ) + self.point1.x
                                  )
                if point.x <= intersection_x:
                    intersection = 1

        return intersection

    def __str__(self):
        return (
             "Le segment est dirigé" +
             f" par les points {self.point1}, {self.point2}"
            )
