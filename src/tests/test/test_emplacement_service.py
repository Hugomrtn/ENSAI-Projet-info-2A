from unittest.mock import MagicMock

from service.emplacement_service import EmplacementService

from dao.dao_emplacement import Dao_emplacement

from business_object.emplacement import Emplacement


liste_emplacements = [
    emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234"),
    emplacement(id_emplacement="lea", niveau="0", nom="lea@mail.fr", code="0000"),
    emplacement(id_emplacement="gg", niveau="10", nom="gg@mail.fr", code="abcd"),
]#à modifier


def test_creer_ok():
    """ "Création d'emplacement réussie"""

    # GIVEN
    niveau, nom, code = "jp", "1234", 15
    Dao_emplacement().creer = MagicMock(return_value=True)

    # WHEN
    emplacement = EmplacementService().creer(niveau, nom, code)

    # THEN
    assert emplacement.niveau == niveau


def test_creer_echec():
    """Création d'emplacement échouée
    (car la méthode Dao_emplacement().creer retourne False)"""

    # GIVEN
    niveau, nom, code = "jp", "1234", 15
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
    assert resultat[0].id_emplacement == "jp"


def test_trouver_par_id():
    """Test pour vérifier la méthode trouver_par_id"""

    # GIVEN
    id_emplacement = "jp"
    emplacement_attendu = Emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234")
    Dao_emplacement().trouver_par_id = MagicMock(return_value=emplacement_attendu)

    # WHEN
    resultat = EmplacementService().trouver_par_id(id_emplacement)

    # THEN
    assert resultat == emplacement_attendu
    assert resultat.id_emplacement == "jp"
    assert resultat.niveau == "10"
    assert resultat.nom == "jp@mail.fr"
    assert resultat.code == "1234"


def test_modifier_succes():
    """Test pour vérifier que la modification réussit"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234")
    Dao_emplacement().modifier = MagicMock(return_value=True)

    # WHEN
    resultat = EmplacementService().modifier(emplacement)

    # THEN
    assert resultat == emplacement


def test_modifier_echec():
    """Test pour vérifier que la modification échoue"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234")
    Dao_emplacement().modifier = MagicMock(return_value=False)

    # WHEN
    resultat = EmplacementService().modifier(emplacement)

    # THEN
    assert resultat is None


def test_supprimer_succes():
    """Test pour vérifier que la suppression réussit"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234")
    Dao_emplacement().supprimer = MagicMock(return_value=True)

    # WHEN
    resultat = EmplacementService().supprimer(emplacement)

    # THEN
    assert resultat is True


def test_supprimer_echec():
    """Test pour vérifier que la suppression échoue"""

    # GIVEN
    emplacement = Emplacement(id_emplacement="jp", niveau="10", nom="jp@mail.fr", code="1234")
    Dao_emplacement().supprimer = MagicMock(return_value=False)

    # WHEN
    resultat = EmplacementService().supprimer(emplacement)

    # THEN
    assert resultat is False


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
