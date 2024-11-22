import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from business_object.emplacement import Emplacement # noqa


@pytest.fixture
def emplacement_sample():
    return Emplacement(
        niveau="ville",
        nom_emplacement="Paris",
        code=75000,
        nombre_habitants=2200000,
        annee=2024
    )


def test_emplacement_initialization(emplacement_sample):
    assert emplacement_sample.niveau == "ville"
    assert emplacement_sample.nom_emplacement == "Paris"
    assert emplacement_sample.code == 75000
    assert emplacement_sample.nombre_habitants == 2200000
    assert emplacement_sample.annee == 2024


def test_emplacement_str_method(emplacement_sample):
    result_str = str(emplacement_sample)
    expected_str = ("Paris, ville de code INSEE 75000 qui" +
                    " comprend 2200000 habitants en 2024")
    assert result_str == expected_str
