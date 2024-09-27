# from dao.dao_emplacement import Dao_emplacement


class Emplacement:

    def __init__(self, niveau: str, nom: str, population: int,
                 id_com: int = None, id_reg: int = None, id_dep: int= None,
                 id_can: int = None, id_arr: int = None) -> None:
        """constructeur"""

        self.niveau = niveau
        self.nom = nom
        self.population = population

        self.id_com = id_com
        self.id_reg = id_reg
        self.id_dep = id_dep
        self.id_can = id_can
        self.id_arr = id_arr

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
