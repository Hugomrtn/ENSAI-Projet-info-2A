class geometrie:

    def est_dans_polygone(polygone: list, point: list):
        """Ray-casting qui permet de déterminer si un point se trouve dans un
        polygone."""

        # initialisations
        x, y = point
        intersections = 0

        for i in range(len(polygone)):
            x1, y1 = polygone[i]
            x2, y2 = polygone[(i + 1) % len(polygone)]

            if min(y1, y2) < y <= max(y1, y2) and x <= max(x1, x2):
                if y1 != y2:
                    if x1 == x2 or x <= ((y - y1) * (x2 - x1) / (y2 - y1)
                                         + x1):
                        intersections += 1
        return intersections % 2 == 1

    def est_dans_liste_polygones(liste_polygones: list, point: list):
        b = False
        for i in range(liste_polygones):
            b = geometrie.est_dans_polygone(liste_polygones[i], point)
            if b:
                break
        return b
