import src.age


def test_stufe_alter_ein_alter_0() -> None:
    wert = src.age.stufe_alter_ein(0)
    assert wert == "junge Person"
