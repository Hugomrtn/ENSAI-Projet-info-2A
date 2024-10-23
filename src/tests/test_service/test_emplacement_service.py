from unittest.mock import MagicMock
import pytest

from service.emplacement_service import EmplacementService
from dao.dao_emplacement import Dao_emplacement
from business_object.emplacement import Emplacement

liste_emplacements = [
    Emplacement(niveau="Ville", nom="Rennes", code=35000),
    Emplacement(niveau="Département", nom="Ille-et-Vilaine", code=35),
    Emplacement(niveau="Région", nom="Bretagne", code=53),
]


def test_creer_emplacement_ok():
    niveau, nom, code = "Ville", "Rennes", 35000
    Dao_emplacement().creer = MagicMock(return_value=True)
    emplacement = EmplacementService().creer(niveau, nom, code)
    assert emplacement.niveau == niveau
    assert emplacement.nom == nom
    assert emplacement.code == code


def test_creer_emplacement_echec():
    niveau, nom, code = "Ville", "Rennes", 35000
    Dao_emplacement().creer = MagicMock(return_value=False)
    emplacement = EmplacementService().creer(niveau, nom, code)
    assert emplacement is None


def test_lister_tous_emplacements():
    Dao_emplacement().lister_tous = MagicMock(return_value=liste_emplacements)
    res = EmplacementService().lister_tous()
    assert len(res) == 3


def test_trouver_par_id_emplacement_ok():
    id_emplacement = 1
    Dao_emplacement().trouver_par_id = MagicMock(return_value=liste_emplacements[0])
    emplacement = EmplacementService().trouver_par_id(id_emplacement)
    assert emplacement.niveau == "Ville"
    assert emplacement.nom == "Rennes"
    assert emplacement.code == 35000


def test_trouver_par_id_emplacement_echec():
    id_emplacement = 1
    Dao_emplacement().trouver_par_id = MagicMock(return_value=None)
    emplacement = EmplacementService().trouver_par_id(id_emplacement)
    assert emplacement is None


if __name__ == "__main__":
    pytest.main([__file__])