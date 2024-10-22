from unittest.mock import MagicMock

from service.polygone_service import PolygoneService

from dao.dao_polygone import Dao_polygone

from business_object.polygone import Polygone

from business_object.point import Point


def test_creer_ok():
    """Test pour vérifier que la création du polygone réussit"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    liste_points = [point_1, point_2]
    nouveau_polygone = Polygone(liste_points=liste_points)

    Dao_polygone().creer = MagicMock(return_value=True)

    # WHEN
    resultat = PolygoneService().creer(liste_points)

    # THEN
    assert resultat == nouveau_polygone
    assert resultat.liste_points == liste_points


def test_creer_echec():
    """Test pour vérifier que la création du polygone échoue"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    liste_points = [point_1, point_2]

    Dao_polygone().creer = MagicMock(return_value=False)  # Simuler échec de la création

    # WHEN
    resultat = PolygoneService().creer(liste_points)

    # THEN
    assert resultat is None  # Vérifie que le résultat est None en cas d'échec


def test_lister_tous():
    """Test pour vérifier la méthode lister_tous"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone_1 = Polygone(liste_points=[point_1, point_2])

    point_3 = Point(x=20.0, y=30.0)
    polygone_2 = Polygone(liste_points=[point_3])

    Dao_polygone().lister_tous = MagicMock(return_value=[polygone_1, polygone_2])

    # WHEN
    resultat = PolygoneService().lister_tous()

    # THEN
    assert resultat == [polygone_1, polygone_2]
    assert len(resultat) == 2
    assert resultat[0].liste_points == [point_1, point_2]
    assert resultat[1].liste_points == [point_3]


def test_trouver_par_id_succes():
    """Test pour vérifier la méthode trouver_par_id pour un ID existant"""

    # GIVEN
    id_polygone = "polygone1"
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone_attendu = Polygone(liste_points=[point_1, point_2])

    Dao_polygone().trouver_par_id = MagicMock(return_value=polygone_attendu)

    # WHEN
    resultat = PolygoneService().trouver_par_id(id_polygone)

    # THEN
    assert resultat == polygone_attendu
    assert resultat.liste_points == [point_1, point_2]


def test_trouver_par_id_echec():
    """Test pour vérifier la méthode trouver_par_id pour un ID non existant"""

    # GIVEN
    id_polygone = "inconnu"
    Dao_polygone().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    resultat = PolygoneService().trouver_par_id(id_polygone)

    # THEN
    assert resultat is None


def test_modifier_succes():
    """Test pour vérifier que la modification réussit"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone = Polygone(liste_points=[point_1, point_2])

    Dao_polygone().modifier = MagicMock(return_value=True)

    # WHEN
    resultat = PolygoneService().modifier(polygone)

    # THEN
    assert resultat == polygone
    assert resultat.liste_points == [point_1, point_2]


def test_modifier_echec():
    """Test pour vérifier que la modification échoue"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone = Polygone(liste_points=[point_1, point_2])

    Dao_polygone().modifier = MagicMock(return_value=False)

    # WHEN
    resultat = PolygoneService().modifier(polygone)

    # THEN
    assert resultat is None


def test_supprimer_succes():
    """Test pour vérifier que la suppression réussit"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone = Polygone(liste_points=[point_1, point_2])

    Dao_polygone().supprimer = MagicMock(return_value=True)
    # WHEN
    resultat = PolygoneService().supprimer(polygone)

    # THEN
    assert resultat is True


def test_supprimer_echec():
    """Test pour vérifier que la suppression échoue"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)
    polygone = Polygone(liste_points=[point_1, point_2])

    Dao_polygone().supprimer = MagicMock(return_value=False)

    # WHEN
    resultat = PolygoneService().supprimer(polygone)

    # THEN
    assert resultat is False
