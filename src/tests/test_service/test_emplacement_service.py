from unittest.mock import MagicMock

from src.service.emplacement_service import EmplacementService

from src.dao.dao_emplacement import Dao_emplacement

from src.business_object.emplacement import Emplacement


liste_emplacements = [
    emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000"),
    emplacement(id_emplacement="2", niveau="0", nom="", code="0000"),
    emplacement(id_emplacement="3", niveau="10", nom="", code="1111"),
]#à modifier


def test_creer_ok():
    """ "Création d'emplacement réussie"""

    # GIVEN
    niveau, nom, code = "Ville", "Rennes", "35000"
    Dao_emplacement().creer = MagicMock(return_value=True)

    # WHEN
    emplacement = EmplacementService().creer(niveau, nom, code)

    # THEN
    assert emplacement.niveau == niveau


def test_creer_echec():
    """Création d'emplacement échouée
    (car la méthode Dao_emplacement().creer retourne False)"""

    # GIVEN
    niveau, nom, code = "Ville", "Rennes", "35000"
    Dao_emplacement().creer = MagicMock(return_value=False)

    # WHEN
    emplacement = EmplacementService().creer(niveau, nom, code)

    # THEN
    assert emplacement is None


def test_lister_tous():
    """Test pour vérifier la méthode lister_tous"""

    # GIVEN
    Dao_emplacement().lister_tous = MagicMock(return_value=liste_emplacements)

    # WHEN
    resultat = EmplacementService().lister_tous()

    # THEN
    assert resultat == liste_emplacements
    assert len(resultat) == 3
    assert resultat[0].id_emplacement == "1"


def test_trouver_par_id():
    """Test pour vérifier la méthode trouver_par_id"""

    # GIVEN
    id_emplacement = "1"
    emplacement_attendu = Emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000")
    Dao_emplacement().trouver_par_id = MagicMock(return_value=emplacement_attendu)

    # WHEN
    resultat = EmplacementService().trouver_par_id(id_emplacement)

    # THEN
    assert resultat == emplacement_attendu
    assert resultat.id_emplacement == "1"
    assert resultat.niveau == "Ville"
    assert resultat.nom == "Rennes"
    assert resultat.code == "35000"


def test_modifier_succes():
    """Test pour vérifier que la modification réussit"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000")
    Dao_emplacement().modifier = MagicMock(return_value=True)

    # WHEN
    resultat = EmplacementService().modifier(emplacement)

    # THEN
    assert resultat == emplacement


def test_modifier_echec():
    """Test pour vérifier que la modification échoue"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000")
    Dao_emplacement().modifier = MagicMock(return_value=False)

    # WHEN
    resultat = EmplacementService().modifier(emplacement)

    # THEN
    assert resultat is None


def test_supprimer_succes():
    """Test pour vérifier que la suppression réussit"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000")
    Dao_emplacement().supprimer = MagicMock(return_value=True)

    # WHEN
    resultat = EmplacementService().supprimer(emplacement)

    # THEN
    assert resultat is True


def test_supprimer_echec():
    """Test pour vérifier que la suppression échoue"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="1", niveau="Ville", nom="Rennes", code="35000")
    Dao_emplacement().supprimer = MagicMock(return_value=False)

    # WHEN
    resultat = EmplacementService().supprimer(emplacement)

    # THEN
    assert resultat is False


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
