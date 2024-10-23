from utils.log_decorator import log
from business_object.polygone import Polygone
from dao.dao_polygone import Dao_polygone


class PolygoneService:
    """Classe contenant les méthodes de service des Polygones"""

    @log
    def creer(self, liste_points) -> Polygone:
        """Création d'un polygone à partir de ses attributs"""

        nouveau_polygone = Polygone(
            liste_points=liste_points,
        )

        return nouveau_polygone if Dao_polygone().creer(nouveau_polygone) else None

    @log
    def lister_tous(self) -> list[Polygone]:
        """Lister tous les polygones"""
        return Dao_polygone().lister_tous()

    @log
    def trouver_par_id(self, id_polygone) -> Polygone:
        """Trouver un polygone à partir de son id"""
        return Dao_polygone().trouver_par_id(id_polygone)

    @log
    def modifier(self, polygone) -> Polygone:
        """Modification d'un polygone"""

        return polygone if Dao_polygone().modifier(polygone) else None

    @log
    def supprimer(self, polygone) -> bool:
        """Supprimer un polygone"""
        return Dao_polygone().supprimer(polygone)