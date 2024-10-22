import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_object.point import Point
from business_object.polygone import Polygone
from business_object.contour import Contour
from business_object.emplacement import Emplacement


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)
p4 = Point(4, 4)
p5 = Point(5, 5)
p6 = Point(6, 6)
p7 = Point(7, 7)
p8 = Point(8, 8)
p9 = Point(9, 9)
p10 = Point(10, 10)
p11 = Point(11, 11)
p12 = Point(12, 12)
p13 = Point(13, 13)
p14 = Point(14, 14)
p15 = Point(15, 15)
p16 = Point(16, 16)

poly1 = Polygone([p1, p2, p3, p4])
poly2 = Polygone([p5, p6, p7, p8])
poly3 = Polygone([p9, p10, p11, p12])
poly4 = Polygone([p13, p14, p15, p16])

contour = Contour([poly1, poly1], [poly3, poly4])

emplacement = Emplacement("Ville", "Rennes", 35000, 250000, 2024)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)
print(p12)
print(p13)
print(p14)
print(p15)
print(p16)

print(poly1)
print(poly2)
print(poly3)
print(poly4)

print(contour)

print(emplacement)
