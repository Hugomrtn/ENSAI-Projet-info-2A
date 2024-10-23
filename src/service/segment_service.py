from utils.log_decorator import log
from business_object.point import Point
from business_object.segment import Segment


class SegmentService:
    @log
    def creer(self, point1: Point, point2: Point) -> Segment:
        nouveau_segment = Segment(point1, point2)
        return nouveau_segment

    @log
    def coupe_a_droite(self, segment: Segment, point: Point) -> int:
        return segment.coupe_a_droite(point)
