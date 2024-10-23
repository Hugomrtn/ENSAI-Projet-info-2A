from unittest.mock import MagicMock

from src.service.point_service import PointService

from src.dao.dao_point import Dao_point

from src.business_object.point import Point


def test_creer_ok():
    """Test pour vérifier que la création du point réussit"""

    # GIVEN
    x, y = 10.5, 20.3
    nouveau_point = Point(x=x, y=y)
    Dao_point().creer = MagicMock(return_value=True)

    # WHEN
    resultat = PointService().creer(x, y)

    # THEN
    assert resultat == nouveau_point
    assert resultat.x == x
    assert resultat.y == y


def test_creer_echec():
    """Test pour vérifier que la création du point échoue"""

    # GIVEN
    x, y = 10.5, 20.3
    Dao_point().creer = MagicMock(return_value=False)  # Simuler échec de la création

    # WHEN
    resultat = PointService().creer(x, y)

    # THEN
    assert resultat is None


def test_lister_tous():
    """Test pour vérifier la méthode lister_tous"""

    # GIVEN
    point_1 = Point(x=10.5, y=20.3)
    point_2 = Point(x=15.2, y=25.6)

    Dao_point().lister_tous = MagicMock(return_value=[point_1, point_2])

    # WHEN
    resultat = PointService().lister_tous()

    # THEN
    assert resultat == [point_1, point_2]
    assert len(resultat) == 2
    assert resultat[0].x == point_1.x
    assert resultat[0].y == point_1.y
    assert resultat[1].x == point_2.x
    assert resultat[1].y == point_2.y


def test_trouver_par_id_succes():
    """Test pour vérifier la méthode trouver_par_id pour un ID existant"""

    # GIVEN
    id_point = "point1"
    point_attendu = Point(x=10.5, y=20.3)

    Dao_point().trouver_par_id = MagicMock(return_value=point_attendu)

    # WHEN
    resultat = PointService().trouver_par_id(id_point)

    # THEN
    assert resultat == point_attendu
    assert resultat.x == 10.5
    assert resultat.y == 20.3


def test_trouver_par_id_echec():
    """Test pour vérifier la méthode trouver_par_id pour un ID non existant"""

    # GIVEN
    id_point = "inconnu"
    Dao_point().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    resultat = PointService().trouver_par_id(id_point)

    # THEN
    assert resultat is None


def test_modifier_succes():
    """Test pour vérifier que la modification réussit"""

    # GIVEN
    point = Point(x=10.5, y=20.3)
    Dao_point().modifier = MagicMock(return_value=True)

    # WHEN
    resultat = PointService().modifier(point)

    # THEN
    assert resultat == point
    assert resultat.x == 10.5
    assert resultat.y == 20.3


def test_modifier_echec():
    """Test pour vérifier que la modification échoue"""

    # GIVEN
    point = Point(x=10.5, y=20.3)
    Dao_point().modifier = MagicMock(return_value=False)

    # WHEN
    resultat = PointService().modifier(point)

    # THEN
    assert resultat is None


def test_supprimer_succes():
    """Test pour vérifier que la suppression réussit"""

    # GIVEN
    point = Point(x=10.5, y=20.3)
    Dao_point().supprimer = MagicMock(return_value=True)

    # WHEN
    resultat = PointService().supprimer(point)

    # THEN
    assert resultat is True


def test_supprimer_echec():
    """Test pour vérifier que la suppression échoue"""

    # GIVEN
    point = Point(x=10.5, y=20.3)
    Dao_point().supprimer = MagicMock(return_value=False)

    # WHEN
    resultat = PointService().supprimer(point)

    # THEN
    assert resultat is False
