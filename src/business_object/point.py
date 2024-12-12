import csv


class Point:
    """
    Classe représentant un point

    ----------

    Parameters :

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

    def lire_fichier(self, contenu_fichier):
        """
        Permet de lire un fichier et de créer les nouveaux points de
        ce fichier.

        ------------
        Parameters :
            contenu_ficher : csv
                fichier donné par un utilisateur pour
                rajouter du contenu dans la BDD

        """
        liste_points = []
        csv_reader = csv.reader(contenu_fichier)
        for lignes in csv_reader:
            liste_points.append(Point(float(lignes[1]), float(lignes[0])))
        return liste_points
