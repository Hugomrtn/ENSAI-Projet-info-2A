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

            # Vérifie si le point se situe au même niveau vertical
            if min(y1, y2) < y <= max(y1, y2) and x <= max(x1, x2):
                # Vérifie que le point n'est pas derrière l'intersection
                if y1 != y2:
                    inter_x = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                if x1 == x2 or x <= inter_x:
                    intersections += 1
        # Si le nombre d'intersections est impair, alors le point y appartient
        return intersections % 2 == 1
