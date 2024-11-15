from dao.dao_emplacement import Dao_emplacement
from dao.dao_contour import Dao_contour
from business_object.point import Point
from business_object.contour import Contour # noqa


class Service_utilisateur:

    def fonction1_obtenir_informations_selon_code_et_annee(self, code, annee):
        """
        Récupère les informations d'un emplacement en fonction de son code et d'une année donnée.

        Parameters
        ----------
        code : str
            Le code unique de l'emplacement (ex. code postal ou code INSEE).

        annee : int
            L'année pour laquelle les informations de l'emplacement sont demandées.

        Returns
        -------
        emplacement : dict or None
            Un dictionnaire contenant les informations de l'emplacement si trouvé.
            Retourne `None` si aucun emplacement correspondant n'est trouvé ou en cas d'erreur.
        """
        id_emplacement = Dao_emplacement().obtenir_id_selon_code(code)
        emplacement = Dao_emplacement().obtenir_emplacement_selon_id_et_annee(
            id_emplacement, annee)
        # penser à gerer les exceptions
        return emplacement if emplacement else None

    def fonction2_obtenir_emplacement_selon_point_niveau_annee(self, niveau,
                                                               annee, point):
         """
        Trouve l'ID d'un emplacement en fonction d'un point géographique, du niveau et de l'année spécifiés.

        Parameters
        ----------
        niveau : str
            Niveau de l'emplacement (par exemple : commune, département, région, etc.).

        annee : int
            Année pour laquelle les informations de l'emplacement sont recherchées.

        point : Point
            Point géographique (objet `Point`) à localiser.

        Returns
        -------
        id_emplacement : int or None
            L'ID de l'emplacement contenant le point si trouvé, ou `None` si aucun emplacement ne correspond.
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
                return id_emplacement
        return None

    def fonction3_obtenir_multiples_emplacements_selons_liste_coordonnees(
            self, liste_coordonnees):
        """
        Trouve les emplacements correspondant à une liste de coordonnées.

        Cette méthode prend une liste de coordonnées (x, y), les transforme en objets `Point`,
        et recherche pour chacun l'emplacement correspondant en utilisant une méthode de localisation.

        Parameters
        ----------
        liste_coordonnees : list of tuple
            Liste de couples (x, y) représentant les coordonnées géographiques
            à traiter.

        Returns
        -------
        liste_resultat : list of int or None
            Liste des IDs des emplacements trouvés pour chaque point. Si un point
            ne correspond à aucun emplacement, l'entrée sera `None`.
        """
        # ON DIT QUE DANS LISTE COORDONNEES IL Y A DES COUPLES
        liste_points = [Point(x, y) for (x, y) in liste_coordonnees]

        liste_resultat = [
            Service_utilisateur.fonction2_obtenir_emplacement_selon_coordonnees
            (point)
            for point in liste_points
        ]
        return liste_resultat
