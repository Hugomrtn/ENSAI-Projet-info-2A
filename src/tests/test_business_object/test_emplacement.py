import pytest
from src.business_object.emplacement import Emplacement


@pytest.fixture
def emplacement_sample():
    return Emplacement(
        niveau="ville",
        nom="Paris",
        code=75000,
        pop=2200000,
        annee=2024
    )


def test_emplacement_initialization(emplacement_sample):
    assert emplacement_sample.niveau == "ville"
    assert emplacement_sample.nom == "Paris"
    assert emplacement_sample.code == 75000
    assert emplacement_sample.pop == 2200000
    assert emplacement_sample.annee == 2024


def test_emplacement_str_method(emplacement_sample):
    result_str = str(emplacement_sample)
    expected_str = "Paris est un/une ville qui comprend 2200000 habitants"
    assert result_str == expected_str
