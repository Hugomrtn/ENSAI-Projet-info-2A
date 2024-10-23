from utils.log_decorator import log
from dao.dao_polygone import Dao_polygone
from business_object.polygone import Polygone
from dao.dao_point import Dao_point
from business_object.point import Point


class PolygoneService:
    @log
    def creer(self, liste_points: list[Point]) -> Polygone:
        polygone = Polygone(liste_points)
        return polygone if Dao_polygone().creer_entierement_polygone(polygone) else None

    @log
    def lister_tous(self) -> list[Polygone]:
        polygones = []
        for (
            id_polygone
        ) in Dao_polygone().obtenir_id_polygones_composants_selon_id_contour(None):
            points = Dao_point().obtenir_points_ordonnes_selon_id_polygone(id_polygone)
            polygones.append(Polygone(points))
        return polygones

    @log
    def trouver_par_id(self, id_polygone: int) -> Polygone:
        points = Dao_point().obtenir_points_ordonnes_selon_id_polygone(id_polygone)
        return Polygone(points)

    @log
    def modifier(self, polygone: Polygone) -> Polygone:
        return (
            polygone
            if Dao_polygone().supprimer(polygone.id_polygone)
            and Dao_polygone().creer_entierement_polygone(polygone)
            else None
        )

    @log
    def supprimer(self, id_polygone: int) -> bool:
        return Dao_polygone().supprimer(id_polygone)
