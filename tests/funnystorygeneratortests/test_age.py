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
