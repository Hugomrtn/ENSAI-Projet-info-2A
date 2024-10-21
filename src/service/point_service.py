from tabulate import tabulate
from utils.log_decorator import log
from business_object.point import Point
from dao.dao_point import Dao_point


class PointService:
    """Classe contenant les méthodes de service des Points"""

    @log
    def creer(self, x, y) -> Point:
        """Création d'un point à partir de ses attributs"""

        nouveau_point = Point(
            x=x,
            y=y,
        )

        return nouveau_point if Dao_point().creer(nouveau_point) else None

    @log
    def lister_tous(self) -> list[Point]:
        """Lister tous les points"""
        return Dao_point().lister_tous()

    @log
    def trouver_par_id(self, id_point) -> Point:
        """Trouver un point à partir de son id"""
        return Dao_point().trouver_par_id(id_point)

    @log
    def modifier(self, point) -> Point:
        """Modification d'un point"""

        return point if Dao_point().modifier(point) else None

    @log
    def supprimer(self, point) -> bool:
        """Supprimer un point"""
        return Dao_point().supprimer(point)