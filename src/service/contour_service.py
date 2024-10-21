from tabulate import tabulate
from utils.log_decorator import log
from business_object.contour import Contour
from dao.dao_contour import Dao_contour


class ContourService:
    """Classe contenant les méthodes de service des Contours"""

    @log
    def creer(self, polygones_composants, polygones_enclaves) -> Contour:
        """Création d'un contour à partir de ses attributs"""

        nouveau_contour = Contour(
            polygones_composants=polygones_composants,
            polygones_enclaves=polygones_enclaves,
        )

        return nouveau_contour if Dao_contour().creer(nouveau_contour) else None

    @log
    def lister_tous(self) -> list[Contour]:
        """Lister tous les contours"""
        return Dao_contour().lister_tous()

    @log
    def trouver_par_id(self, id_contour) -> Contour:
        """Trouver un contour à partir de son id"""
        return Dao_contour().trouver_par_id(id_contour)

    @log
    def modifier(self, contour) -> Contour:
        """Modification d'un contour"""

        return contour if Dao_contour().modifier(contour) else None

    @log
    def supprimer(self, contour) -> bool:
        """Supprimer un contour"""
        return Dao_contour().supprimer(contour)