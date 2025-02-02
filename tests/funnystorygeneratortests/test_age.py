import src.age


def test_stufe_alter_ein_junge_person() -> None:
    for alter in [0, 1, 13, 25, 26]:
        alters_einstufung = src.age.stufe_alter_ein(alter)
        assert alters_einstufung == "junge Person"


def test_stufe_alter_ein_erwachsene_person() -> None:
    for alter in [27, 28, 35, 58, 59]:
        alters_einstufung = src.age.stufe_alter_ein(alter)
        assert alters_einstufung == "erwachsene Person"


def test_stufe_alter_ein_aeltere_person() -> None:
    for alter in [60, 61, 101, 121, 122]:
        alters_einstufung = src.age.stufe_alter_ein(alter)
        assert alters_einstufung == "ältere Person"


def test_stufe_alter_ein_unglaubwuerdige_person() -> None:
    for alter in [123, 124, 210, 1221]:
        alters_einstufung = src.age.stufe_alter_ein(alter)
        assert alters_einstufung == "unglaubwürdige Person"


def test_stufe_alter_ein_noch_nicht_geborene_person() -> None:
    for alter in [-1, -2, -50]:
        alters_einstufung = src.age.stufe_alter_ein(alter)
        assert alters_einstufung == "noch nicht geborene Person"
