import csv


class Point:
    """Classe représentant un point
    Parameters
    ----------
    x: float
    y: float
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"(Point de coordonnées {self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def lire_fichier(fichier):
        liste_points = []
        with open(fichier, mode="r") as file:
            csvFile = csv.reader(file)
            for lignes in csvFile:
                liste_points.append(Point(lignes[0], lignes[1]))
        return liste_points

    def editer(texte):
        fichier = open("texte.txt", "w")
        fichier.close()
