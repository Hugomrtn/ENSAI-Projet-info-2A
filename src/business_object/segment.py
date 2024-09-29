from src.business_object.point import Point


class Segment:
    """Classe représentant un segment
    Attributs
    ----------
    x: Point
    y: Point
    """
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def coupe_a_droite(self, point: Point) -> int:
        intersection = 0
        if ((min(self.point1.y, self.point2.y) < point.y <= max(self.point1.y,
                                                                self.point2.y))
                and point.x <= max(self.point1.x, self.point2.x)):
            if self.point1.y != self.point2.y:
                if (self.point1.x == self.point2.x or
                    point.x <= ((point.y - self.point1.y) * (self.point2.x -
                                                             self.point1.x)
                                / (self.point2.y - self.point1.y)
                                + self.point1.x)):
                    intersection += 1
