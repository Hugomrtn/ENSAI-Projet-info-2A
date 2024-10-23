from src.utils.log_decorator import log
from src.dao.dao_contour import Dao_contour
from src.business_object.contour import Contour
from src.business_object.polygone import Polygone
from src.dao.dao_polygone import Dao_polygone


class ContourService:
    @log
    def creer(
        self, polygones_composants: list[Polygone], polygones_enclaves: list[Polygone]
    ) -> Contour:
        contour = Contour(polygones_composants, polygones_enclaves)
        return contour if Dao_contour().creer_entierement_contour(contour) else None

    @log
    def lister_tous(self) -> list[Contour]:
        contours = []
        for id_contour in Dao_contour().obtenir_id_contour_selon_id_emplacement_annne(
            None, None
        ):
            polygones_composants = [
                Polygone(
                    Dao_polygone().obtenir_id_polygones_composants_selon_id_contour(
                        id_contour
                    )
                )
            ]
            polygones_enclaves = [
                Polygone(
                    Dao_polygone().obtenir_id_polygones_enclaves_selon_id_contour(
                        id_contour
                    )
                )
            ]
            contours.append(Contour(polygones_composants, polygones_enclaves))
        return contours

    @log
    def trouver_par_id(self, id_contour: int) -> Contour:
        polygones_composants = (
            Dao_polygone().obtenir_id_polygones_composants_selon_id_contour(id_contour)
        )
        polygones_enclaves = (
            Dao_polygone().obtenir_id_polygones_enclaves_selon_id_contour(id_contour)
        )
        return Contour(polygones_composants, polygones_enclaves)

    @log
    def modifier(self, contour: Contour) -> Contour:
        return (
            contour
            if Dao_contour().supprimer(contour.id_contour)
            and Dao_contour().creer_entierement_contour(contour)
            else None
        )

    @log
    def supprimer(self, id_contour: int) -> bool:
        return Dao_contour().supprimer(id_contour)
