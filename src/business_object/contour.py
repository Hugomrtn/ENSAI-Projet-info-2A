from business_object.polygone import Polygone
from business_object.point import Point


class Contour:
    """Classe représentant un contour
    Parameters
    ----------
    polygones_composants: list[Polygone]
    polygones_enclaves: list[Polygone]
    """

    def __init__(
        self, polygones_composants: list[Polygone],
        polygones_enclaves: list[Polygone]
    ):
        self.polygones_composants = polygones_composants
        self.polygones_enclaves = polygones_enclaves

    def contour_contient_point(self, point: Point):
        bool_composant = False
        bool_enclave = False
        for polygone in self.polygones_composants:
            if polygone.polygone_contient_point(point):
                bool_composant = True
                break
        for polygone in self.polygones_enclaves:
            if polygone.polygone_contient_point(point):
                bool_enclave = True
                break
        return bool_composant and not bool_enclave

    def __str__(self):
        return (
            f"(Contour comportant {self.polygones_composants} et "
            f"excluant {self.polygones_enclaves})"
        )
