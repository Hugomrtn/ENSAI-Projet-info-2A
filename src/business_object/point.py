class Point:
    """Classe représentant un point
    Parameters
    ----------
    x: float
    y: float
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return (
            f"(Point de coordonnées {self.x}, {self.y})"
        )

    def __repr__(self):
        return (
            f"({self.x}, {self.y})"
        )
