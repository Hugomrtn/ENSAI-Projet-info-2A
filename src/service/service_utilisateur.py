from dao.dao_emplacement import Dao_emplacement
from dao.dao_contour import Dao_contour
from business_object.point import Point
from business_object.contour import Contour # noqa


class Service_utilisateur:

    def fonction1_obtenir_informations_selon_code_et_annee(self, code, annee):
        id_emplacement = Dao_emplacement().obtenir_id_selon_code(code)
        emplacement = Dao_emplacement().obtenir_emplacement_selon_id_et_annee(
            id_emplacement, annee)
        # penser à gerer les exceptions
        return emplacement if emplacement else None

    def fonction2_obtenir_emplacement_selon_point_niveau_annee(self, niveau,
                                                               annee, point):
        # RENVOIE L'ID
        liste_id_emplacements = Dao_emplacement().\
            obtenir_id_emplacements_selon_niveau_annee(niveau, annee)
        for id_emplacement in liste_id_emplacements:
            id_contour = Dao_contour().\
                obtenir_id_contour_selon_id_emplacement_annne(id_emplacement,
                                                              annee)
            contour = Dao_contour().\
                instancier_contour_selon_id_contour(id_contour)
            if contour.contour_contient_point(point):
                return Dao_emplacement().obtenir_emplacement_selon_id_et_annee(
                    id_emplacement, annee)
        return None

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
