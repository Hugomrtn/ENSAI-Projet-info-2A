from utils.log_decorator import log
from dao.dao_point import Dao_point
from business_object.point import Point


class PointService:
    @log
    def creer(self, x: float, y: float) -> Point:
        point = Point(x, y)
        return point if Dao_point().creer(point) else None

    @log
    def lister_tous(self) -> list[Point]:
        points = []
        for id_point in Dao_point().obtenir_id_selon_point(None):
            points.append(Dao_point().obtenir_point_selon_id(id_point))
        return points

    @log
    def trouver_par_id(self, id_point: int) -> Point:
        return Dao_point().obtenir_point_selon_id(id_point)

    @log
    def modifier(self, point: Point) -> Point:
        return point if Dao_point().modifier(point.x, point.y) else None

    @log
    def supprimer(self, id_point: int) -> bool:
        return Dao_point().supprimer(id_point)