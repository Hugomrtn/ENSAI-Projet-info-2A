# from dao.dao_emplacement import Dao_emplacement


class Emplacement:
    """Classe représentant un emplacement
    Attributs
    ----------


    """

    def __init__(self, niveau: str, nom: str, code: int,
                 pop: int, annee: int) -> None:
        """constructeur"""

        self.niveau = niveau
        self.nom = nom
        self.code = code
        self.pop = pop
        self.annee = annee

    def __str__(self):
        """Permet d'afficher les informations de l'emplacement"""
        return (
            f"({self.nom} est un/une {self.niveau} ({self.code}) qui comprend "
            f"{self.pop} habitants)"
        )
