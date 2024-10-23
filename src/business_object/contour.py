from business_object.polygone import Polygone


class Contour:
     """Classe représentant un contour
    Parameters
    ----------
    polygones_composants: list[Polygone]
    polygones_enclaves: list[Polygone]
    """

    def __init__(self, polygones_composants: list[Polygone],
                 polygones_enclaves: list[Polygone]):
        self.polygones_composants = polygones_composants
        self.polygones_enclaves = polygones_enclaves

    def __str__(self):
        return (
            f"(Contour comportant {self.polygones_composants} et "
            f"excluant {self.polygones_enclaves})"
        )
