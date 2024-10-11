from business_object.polygone import Polygone


class Contour:

    def __init__(self, polygones_composants: list[Polygone],
                 polygones_enclaves: list[Polygone]):
        self.polygones_composants = polygones_composants
        self.polygones_enclaves = polygones_enclaves
