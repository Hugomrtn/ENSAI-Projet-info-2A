from dao import Dao_emplacement
from business_object import Emplacement
from business_object import Point


class Service_utilisateur:

    def fonction1_obtenir_informations_selon_code(self, code):
        # obtenir l'id a partir du code
        id_emplacement = Dao_emplacement().obtenir_id_selon_code(code)
        # obtenir les informatiosn avec l'id
        res = Dao_emplacement().obtenir_informations(id_emplacement)
        # PENSER A BIEN METTRE LES ARGUMENTS, APRES AVOIR CODÉ LA FONCTION
        # OBTENIR INFORMATIONS
        emplacement = Emplacement(res)
        # penser à gerer les exceptions
        return emplacement if emplacement else None

    def fonction2_obtenir_emplacement_selon_coordonnees(self, point):
        # RENVOIE LE CODE
        return True

    def fonction3_obtenir_multiples_emplacements_selons_liste_coordonnees(
            self, liste_coordonnees):
        # ON DIT QUE DANS LISTE COORDONNEES IL Y A DES COUPLES
        liste_points = [Point(x, y) for (x, y) in liste_coordonnees]

        liste_resultat = [
            Service_utilisateur.fonction2_obtenir_emplacement_selon_coordonnees
            (point)
            for point in liste_points
        ]
        return liste_resultat
