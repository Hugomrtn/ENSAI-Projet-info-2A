import os
import pytest
from unittest.mock import patch, MagicMock
from src.business_object.point import Point
from src.dao.dao_point import Dao_point

# Erreur d'import dans le dao.dao_point mais
# Je comprends pas pourquoi


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        yield


@patch("dao.db_connection.DBConnection")
def test_creer_ok(mock_db_conn):
    """Test de la création d'un point avec succès"""

    # GIVEN
    point = Point(x=10, y=20)
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {"id_point": 1}
    mock_db_conn().connection.cursor.return_value.__enter__.return_value = mock_cursor

    # WHEN
    created = Dao_point().creer(point)

    # THEN
    assert created
    assert point.id_point == 1


@patch("dao.db_connection.DBConnection")
def test_creer_ko(mock_db_conn):
    """Test d'échec de la création d'un point"""

    # GIVEN
    point = Point(x=10, y=20)
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_db_conn().connection.cursor.return_value.__enter__.return_value = mock_cursor

    # WHEN
    created = Dao_point().creer(point)

    # THEN
    assert not created
    assert point.id_point is None


@patch("dao.db_connection.DBConnection")
def test_association_polygone_points_ok(mock_db_conn):
    """Test de la création de l'association entre un polygone et des points"""

    # GIVEN
    id_polygone = 1
    liste_id_point = [1, 2, 3]
    mock_cursor = MagicMock()
    mock_db_conn().connection.cursor.return_value.__enter__.return_value = mock_cursor

    # WHEN
    Dao_point().association_polygone_points(id_polygone, liste_id_point)

    # THEN
    assert mock_cursor.execute.call_count == 3
    # S'assure que les points sont dans le bon ordre
    for i, id_point in enumerate(liste_id_point):
        mock_cursor.execute.assert_any_call(
            "INSERT INTO association_polygone_points(       "
            "id_polygone, id_point, ordre) VALUES           "
            "(%(id_polygone)s, %(id_point)s, %(ordre)s);    ",
            {"id_polygone": id_polygone, "id_point": id_point, "ordre": i},
        )


@patch("dao.db_connection.DBConnection")
def test_existe_polygone_true(mock_db_conn):
    """Test pour vérifier si un polygone existe (réussite)"""

    # GIVEN
    liste_id_point = [1, 2, 3]
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {"id_polygone": 1}
    mock_db_conn().connection.cursor.return_value.__enter__.return_value = mock_cursor

    # WHEN
    exists = Dao_point().existe_polygone(liste_id_point)

    # THEN
    assert exists


@patch("dao.db_connection.DBConnection")
def test_existe_polygone_false(mock_db_conn):
    """Test pour vérifier si un polygone existe (échec)"""

    # GIVEN
    liste_id_point = [1, 2, 3]
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_db_conn().connection.cursor.return_value.__enter__.return_value = mock_cursor

    # WHEN
    exists = Dao_point().existe_polygone(liste_id_point)

    # THEN
    assert not exists


if __name__ == "__main__":
    pytest.main([__file__])
