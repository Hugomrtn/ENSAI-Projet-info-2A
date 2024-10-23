
class Emplacement:
    """Classe représentant un emplacement
    Attributs
    ----------


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
            f"{self.nom} est un/une {self.niveau}, {self.code} qui comprend "
            f"{self.pop} habitants"
        )
