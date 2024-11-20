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

    def lire_fichier(self, fichier):
        liste_points = []
        with open(fichier, mode="r") as file:
            csvFile = csv.reader(file)
            for lignes in csvFile:
                liste_points.append(Point(float(lignes[0]), float(lignes[1])))
        return liste_points

    def editer_fichier(self, liste_resultats):
        "liste_resultat: chaque élément sous la forme [x, y, ]"
        fichier = "résultat.csv"
        with open(fichier, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for resultat in liste_resultats:
                writer.writerow([resultat])

        return fichier
