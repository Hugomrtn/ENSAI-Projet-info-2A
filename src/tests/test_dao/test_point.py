import pytest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")))

from dao.dao_point import Dao_point  # NOQA
from business_object.point import Point  # NOQA


class MockCursor:
    """
    Simulation d'un curseur de base de données.
    """

    def __init__(self):
        self.queries = []
        self.return_values = []
        self.index = 0

    def execute(self, query, params=None):
        self.queries.append((query, params))

    def fetchone(self):
        if self.index < len(self.return_values):
            result = self.return_values[self.index]
            self.index += 1
            return result
        return None

    def fetchall(self):
        return self.return_values

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockDBConnection:
    """
    Simulation d'une connexion à la base de données.
    """

    def __init__(self, cursor):
        self.cursor_instance = cursor

    def cursor(self):
        return self.cursor_instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@patch("dao.db_connection.DBConnection")
def test_creer_point_existant(mock_db_conn):
    """
    Test création d'un point existant.
    """
    # GIVEN
    point = Point(x=10, y=20)
    dao_point = Dao_point()
    dao_point.existe = lambda p: (True, 1)

    # WHEN
    result = dao_point.creer(point)

    # THEN
    assert result == 1


@patch("dao.db_connection.DBConnection")
def test_creer_point_nouveau(mock_db_conn):
    """
    Test création d'un nouveau point.
    """
    # GIVEN
    point = Point(x=10, y=20)
    dao_point = Dao_point()
    dao_point.existe = lambda p: (False, None)

    mock_cursor = MockCursor()
    mock_cursor.return_values = [{"id_point": 1}]
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    # WHEN
    result = dao_point.creer(point)

    # THEN
    assert result == 1
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith("INSERT INTO projet_2A.points")
    assert mock_cursor.queries[0][1] == {"x": 10, "y": 20}


@patch("dao.db_connection.DBConnection")
def test_existe_point_vrai(mock_db_conn):
    """
    Test vérification d'existence pour un point existant.
    """
    # GIVEN
    point = Point(x=10, y=20)
    mock_cursor = MockCursor()
    mock_cursor.return_values = [{"id_point": 1}]
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    dao_point = Dao_point()

    # WHEN
    result = dao_point.existe(point)

    # THEN
    assert result == [True, 1]
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith(
        "SELECT id_point FROM projet_2A.points"
        )
    assert mock_cursor.queries[0][1] == {"x": 10, "y": 20}


@patch("dao.db_connection.DBConnection")
def test_existe_point_faux(mock_db_conn):
    """
    Test vérification d'existence pour un point inexistant.
    """
    # GIVEN
    point = Point(x=10, y=20)
    mock_cursor = MockCursor()
    mock_cursor.return_values = []
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    dao_point = Dao_point()

    # WHEN
    result = dao_point.existe(point)

    # THEN
    assert result == [False, None]
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith(
        "SELECT id_point FROM projet_2A.points"
        )
    assert mock_cursor.queries[0][1] == {"x": 10, "y": 20}


@patch("dao.db_connection.DBConnection")
def test_obtenir_points_ordonnes_selon_id_polygone(mock_db_conn):
    """
    Test récupération des points ordonnés associés à un polygone.
    """
    # GIVEN
    id_polygone = 1
    mock_cursor = MockCursor()
    mock_cursor.return_values = [
        {"x": 1, "y": 2},
        {"x": 3, "y": 4},
        {"x": 5, "y": 6},
    ]
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    dao_point = Dao_point()

    # WHEN
    result = dao_point.obtenir_points_ordonnes_selon_id_polygone(id_polygone)

    # THEN
    assert len(result) == 3
    assert result[0].x == 1 and result[0].y == 2
    assert result[1].x == 3 and result[1].y == 4
    assert result[2].x == 5 and result[2].y == 6
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith("SELECT points.x, points.y")
    assert mock_cursor.queries[0][1] == {"id_polygone": id_polygone}


@patch("dao.db_connection.DBConnection")
def test_obtenir_point_selon_id(mock_db_conn):
    """Test récupération d'un point selon son ID."""
    # GIVEN
    id_point = 1
    mock_cursor = MockCursor()
    mock_cursor.return_values = [{"x": 10, "y": 20}]
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    dao_point = Dao_point()

    # WHEN
    result = dao_point.obtenir_point_selon_id(id_point)

    # THEN
    assert result.x == 10
    assert result.y == 20
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith(
        "SELECT x, y FROM projet_2A.point"
        )
    assert mock_cursor.queries[0][1] == {"id_point": id_point}


@patch("dao.db_connection.DBConnection")
def test_obtenir_point_selon_id_inexistant(mock_db_conn):
    """
    Test récupération d'un point inexistant selon son ID.
    """
    # GIVEN
    id_point = 1
    mock_cursor = MockCursor()
    mock_cursor.return_values = []
    mock_db_conn.return_value = MockDBConnection(mock_cursor)

    dao_point = Dao_point()

    # WHEN
    result = dao_point.obtenir_point_selon_id(id_point)

    # THEN
    assert result is None
    assert len(mock_cursor.queries) == 1
    assert mock_cursor.queries[0][0].startswith(
        "SELECT x, y FROM projet_2A.point"
        )
    assert mock_cursor.queries[0][1] == {"id_point": id_point}


if __name__ == "__main__":
    pytest.main([__file__])
