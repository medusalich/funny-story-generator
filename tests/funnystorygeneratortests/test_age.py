import unittest.mock

import pytest

import src.age


@pytest.mark.parametrize("alter", [0, 1, 13, 25, 26])
def test_stufe_alter_ein_junge_person(alter: int) -> None:
    alters_einstufung = src.age.stufe_alter_ein(alter)
    assert alters_einstufung == "junge Person"


@pytest.mark.parametrize("alter", [27, 28, 35, 58, 59])
def test_stufe_alter_ein_erwachsene_person(alter: int) -> None:
    alters_einstufung = src.age.stufe_alter_ein(alter)
    assert alters_einstufung == "erwachsene Person"


@pytest.mark.parametrize("alter", [60, 61, 101, 121, 122])
def test_stufe_alter_ein_aeltere_person(alter: int) -> None:
    alters_einstufung = src.age.stufe_alter_ein(alter)
    assert alters_einstufung == "ältere Person"


@pytest.mark.parametrize("alter", [123, 124, 210, 1221])
def test_stufe_alter_ein_unglaubwuerdige_person(alter: int) -> None:
    alters_einstufung = src.age.stufe_alter_ein(alter)
    assert alters_einstufung == "unglaubwürdige Person"


@pytest.mark.parametrize("alter", [-1, -2, -50])
def test_stufe_alter_ein_noch_nicht_geborene_person(alter: int) -> None:
    alters_einstufung = src.age.stufe_alter_ein(alter)
    assert alters_einstufung == "noch nicht geborene Person"


@pytest.mark.parametrize("alter", [125, 120, 116])
def test_erzeuge_funfact_1900(alter: int) -> None:
    # Ersetze die Klasse datetime.datetime durch ein MagicMock
    # MagicMock ist ein Dummy, der es erlaubt, beliebeige Verhaltensweisen für Tests zu simulieren.
    with unittest.mock.patch("datetime.datetime") as mock_datetime:
        # Hier wird für datetime.datetime.now().year 2025 als festen Wert vorgegeben.
        # Dadurch ist dieser Test deterministisch und nicht vom Ausführungszeitpunkt abhängig.
        mock_datetime.now.return_value.year = 2025
        funfact = src.age.erzeuge_funfact(alter)
        assert funfact == "als Autos noch mit Pferden um die Wette fuhren"


@pytest.mark.parametrize("alter", [75, 70, 66])
def test_erzeuge_funfact_1950(alter: int) -> None:
    with unittest.mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.year = 2025
        funfact = src.age.erzeuge_funfact(alter)
        assert funfact == "als der Rock'n'Roll die Welt eroberte"


@pytest.mark.parametrize("alter", [5, 3, 1, 0])
def test_erzeuge_funfact_2020(alter: int) -> None:
    with unittest.mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.year = 2025
        funfact = src.age.erzeuge_funfact(alter)
        assert funfact == "als „Zoom“ ein neues Synonym für „Treffen“ war"


@pytest.mark.parametrize("alter", [126, 210])
def test_erzeuge_funfact_zu_alt(alter: int) -> None:
    with unittest.mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.year = 2025
        funfact = src.age.erzeuge_funfact(alter)
        assert funfact == "als es keine Funfacts gab"


@pytest.mark.parametrize("alter", [-1, -5, -21])
def test_erzeuge_funfact_negativ(alter: int) -> None:
    with unittest.mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.year = 2025
        funfact = src.age.erzeuge_funfact(alter)
        assert funfact == "404 ERROR"
