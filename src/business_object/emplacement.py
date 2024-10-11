# from dao.dao_emplacement import Dao_emplacement


class Emplacement:
    """Classe représentant un emplacement
    Attributs
    ----------


    """

    def __init__(self, niveau: str, nom: str, code: int) -> None:
        """constructeur"""

        self.niveau = niveau
        self.nom = nom
        self.code = code

    def __str__(self):
        """Permet d'afficher les informations de l'emplacement"""
        return (
            f"({self.nom} est un/une {self.niveau} qui comprend "
            f"{self.population} habitants)"
        )

    def as_list(self) -> list[str]:
        """Retourne les attributs de l'emplacement dans une liste"""
        return [self.niveau, self.nom, self.population, self.id_com,
                self.id_reg, self.id_can, self.id_arr]
