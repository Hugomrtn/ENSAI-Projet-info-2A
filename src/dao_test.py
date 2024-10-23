from random import randint
from dao.dao_contour import Dao_contour
from dao.dao_emplacement import Dao_emplacement
from dao.dao_point import Dao_point
from dao.dao_polygone import Dao_polygone

from business_object.point import Point
from business_object.polygone import Polygone
from business_object.contour import Contour
from business_object.emplacement import Emplacement

from dao.db_connection import DBConnection
from utils.reset_database import ResetDatabase

p1 = Point(10, 11)
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

p17 = Point(17, 17)
p18 = Point(18, 18)
p19 = Point(19, 19)
p20 = Point(20, 20)

poly5 = Polygone([p17, p18, p19, p20])

p21 = Point(21, 21)
p22 = Point(22, 22)
p23 = Point(23, 23)
p24 = Point(24, 24)

poly6 = Polygone([p21, p22, p23, p24])

contour = Contour([poly1, poly1], [poly3, poly4])

emplacement = Emplacement("Ville", "Rennes", 35000, 250000, 2024)

###
# ResetDatabase().lancer()
###
# DAO POINT
"""
print(Dao_point().creer(p1))
print(Dao_point().creer(p2))
print(Dao_point().creer(p3))
print(Dao_point().creer(p4))
print(Dao_point().creer(p5))
print(Dao_point().creer(p6))
print(Dao_point().creer(p7))
print(Dao_point().creer(p8))
print(Dao_point().creer(p9))
print(Dao_point().creer(p10))
print(Dao_point().creer(p11))
print(Dao_point().creer(p12))
print(Dao_point().creer(p13))
print(Dao_point().creer(p14))
print(Dao_point().creer(p15))
print(Dao_point().creer(p16))"""

# DAO POLYGONE

"""print(Dao_polygone().creer_entierement_polygone(poly1))
print(Dao_polygone().creer_entierement_polygone(poly2))
print(Dao_polygone().creer_entierement_polygone(poly3))
print(Dao_polygone().creer_entierement_polygone(poly4))"""

# DAO Contour


# print(Dao_contour().creer_entierement_contour(contour))


# DAO emplacement

# print(Dao_emplacement().creer(emplacement))
# print(Dao_emplacement().creer_association_emplacement_contour(1, 2024, 1, 23456789))

"""print(Dao_emplacement().creer_entierement_emplacement(
    emplacement, Dao_contour().creer_entierement_contour(contour)))"""

# print(Dao_emplacement().creer_entierement_emplacement(emplacement, 1))

print(Dao_polygone().existe(poly4))
