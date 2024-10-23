from utils.log_decorator import log
from business_object.point import Point
from business_object.segment import Segment


class SegmentService:
    """Classe contenant les méthodes de service des Segments"""

    @log
    def creer(self, point1: Point, point2: Point) -> Segment:
        """Création d'un segment à partir de deux points"""
        nouveau_segment = Segment(point1, point2)
        return nouveau_segment

    @log
    def coupe_a_droite(self, segment: Segment, point: Point) -> int:
        """Vérifie si un segment coupe à droite d'un point"""
        return segment.coupe_a_droite(point)
