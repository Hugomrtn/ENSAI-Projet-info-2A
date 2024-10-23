from utils.log_decorator import log
from dao.dao_emplacement import Dao_emplacement
from business_object.emplacement import Emplacement


class EmplacementService:
    @log
    def creer(self, niveau: str, nom: str, code: int, pop: int, annee: int) -> Emplacement:
        emplacement = Emplacement(niveau, nom, code, pop, annee)
        return emplacement if Dao_emplacement().creer(entierement_emplacement=emplacement) else None

    @log
    def lister_tous(self) -> list[Emplacement]:
        return Dao_emplacement().obtenir_informations(id_emplacement=None)

    @log
    def trouver_par_id(self, id_emplacement: int) -> Emplacement:
        informations = Dao_emplacement().obtenir_informations(id_emplacement)
        if informations:
            return Emplacement(**informations)
        return None

    @log
    def modifier(self, emplacement: Emplacement) -> Emplacement:
        return emplacement if Dao_emplacement().modifier_emplacement(emplacement.id_emplacement, emplacement.nom, emplacement.niveau, emplacement.code) else None

    @log
    def supprimer(self, id_emplacement: int) -> bool:
        return Dao_emplacement().supprimer_emplacement(id_emplacement)