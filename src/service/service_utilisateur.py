from dao.dao_emplacement import Dao_emplacement
from dao.dao_contour import Dao_contour
from business_object.point import Point # noqa
from business_object.contour import Contour # noqa


class Service_utilisateur:

    def fonction1_obtenir_informations_selon_code_niveau_et_annee(self, code,
                                                                  niveau,
                                                                  annee):
        """
        Fonction permettant d'obtenir des informations de la BDD à
        travers la DAO.

        -------------

        Parameters:
            code : int
                Code insee
            niveau : str
                niveau recherché par l'utilisateur
            annee : int
                annee recherche

        -------------

        Returns :
            L'emplacement correspondant s'il existe.

        """
        id_emplacement = Dao_emplacement().obtenir_id_selon_code_et_niveau(
            code, niveau)
        emplacement = Dao_emplacement().obtenir_emplacement_selon_id_et_annee(
            id_emplacement, annee)
        # penser à gerer les exceptions
        return emplacement if emplacement else None

    def fonction2_obtenir_emplacement_selon_point_niveau_annee(self, niveau,
                                                               annee, point):
        """
        Fonction permettant d'obtenir des informations de la BDD à
        travers la DAO.

        -------------

        Parameters:
            point : Point
            niveau : str
                niveau recherché par l'utilisateur
            annee : int
                annee recherche

        -------------

        Returns :
            L'emplacement correspondant s'il existe.

        """
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
            self, liste_points, niveau, annee):
        """
        Fonction permettant d'obtenir des informations de la BDD à
        travers la DAO.

        -------------

        Parameters:
            liste_points: list[Point, Point, ...]
                Liste d'objet point
            niveau : str
                niveau recherché par l'utilisateur
            annee : int
                annee recherche

        -------------

        Returns :
            List_emplacement : list[Emplacement, ...]
                La liste d'emplacement correspondant s'il existe.

        """

        liste_emplacements = []
        for i in range(len(liste_points)):
            liste_emplacements.append(
                Service_utilisateur().
                fonction2_obtenir_emplacement_selon_point_niveau_annee(
                    niveau, annee, liste_points[i]))

        liste_resultat = []

        for i in range(len(liste_emplacements)):
            if liste_emplacements[i]:
                texte = (f"{repr(liste_points[i])} se trouve dans "
                         f"{repr(liste_emplacements[i])}.")
            else:
                texte = f"{repr(liste_points[i])} n'a pas été trouvé."
            liste_resultat.append(texte)

        return liste_resultat
