
class Emplacement:
    """
    Classe représentant un emplacement

    -----------

    Parameters :

        niveau:str
        nom_emplacement:str
        code:int
        nombre_habitants:int
        annee:int
    """

    def __init__(self, niveau: str, nom_emplacement: str, code: int,
                 nombre_habitants: int, annee: int) -> None:
        """constructeur"""

        self.niveau = niveau
        self.nom_emplacement = nom_emplacement
        self.code = code
        self.nombre_habitants = nombre_habitants
        self.annee = annee

    def __str__(self):
        """Permet d'afficher les informations de l'emplacement"""
        return (
            f"{self.nom_emplacement}, {self.niveau} de code INSEE "
            f"{self.code} qui comprend {self.nombre_habitants} habitants en "
            f"{self.annee}"
        )

    def __repr__(self):
        return (
            f"{self.nom_emplacement}, {self.niveau} de code INSEE "
            f"{self.code} qui comprend {self.nombre_habitants} habitants en "
            f"{self.annee}"
        )
