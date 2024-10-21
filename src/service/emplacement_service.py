from tabulate import tabulate
from utils.log_decorator import log
from business_object.emplacement import Emplacement
from dao.dao_emplacement import Dao_emplacement


class EmplacementService:
    """Classe contenant les méthodes de service des Emplacements"""

    @log
    def creer(self, niveau, nom, code) -> Emplacement:
        """Création d'un emplacement à partir de ses attributs"""

        nouveau_emplacement = Emplacement(
            niveau=niveau,
            nom=nom,
            code=code,
        )

        return nouveau_emplacement if Dao_emplacement().creer(nouveau_emplacement) else None

    @log
    def lister_tous(self) -> list[Emplacement]:
        """Lister tous les emplacements"""
        return Dao_emplacement().lister_tous()

    @log
    def trouver_par_id(self, id_emplacement) -> Emplacement:
        """Trouver un emplacement à partir de son id"""
        return Dao_emplacement().trouver_par_id(id_emplacement)

    @log
    def modifier(self, emplacement) -> Emplacement:
        """Modification d'un emplacement"""

        return emplacement if Dao_emplacement().modifier(emplacement) else None

    @log
    def supprimer(self, emplacement) -> bool:
        """Supprimer un emplacement"""
        return Dao_emplacement().supprimer(emplacement)

    @log
    def afficher_tous(self) -> str:
        """Afficher tous les emplacements
        Sortie : Une chaine de caractères mise sous forme de tableau
        """
        entetes = ["niveau", "nom", "code"]

        emplacements = Dao_emplacement().lister_tous()

        emplacements_as_list = [e.as_list() for e in emplacements]

        str_emplacements = "-" * 100
        str_emplacements += "\nListe des emplacements \n"
        str_emplacements += "-" * 100
        str_emplacements += "\n"
        str_emplacements += tabulate(
            tabular_data=emplacements_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_emplacements += "\n"

        return str_emplacements
