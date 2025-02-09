import builtins
import unittest.mock

import src.user_input


def test_ohne_zahl() -> None:
    nutzer_eingabe = "A aSf>!=.,-äÖßÜ?+*(&)"
    with unittest.mock.patch.object(builtins, "input", lambda _: nutzer_eingabe):
        ohne_zahl = src.user_input.ohne_zahl("")
        assert ohne_zahl == nutzer_eingabe


def test_ohne_zahl_leere_eingabe(capsys) -> None:
    # Ersezte input() durch ein MagicMock.
    # Gibt beim ersten Aufruf einen leeren String und beim zweiten Aufruf einen gültigen String.
    nutzer_eingaben = iter(["", "Hi"])
    with unittest.mock.patch.object(builtins, "input", side_effect=nutzer_eingaben):
        ohne_zahl = src.user_input.ohne_zahl("")
        # capsys: Ermöglicht es, die Konsolenausgaben (z.B. von print()) während eines Tests zu erfassen.
        konsolen_ausgaben = capsys.readouterr()
        assert konsolen_ausgaben.out == "Es wurde nichts eingeben, versuche es nochmal.\n"
        assert ohne_zahl == "Hi"


def test_ohne_zahl_mit_zahl(capsys) -> None:
    nutzer_eingaben = iter(["2", "Hi"])
    with unittest.mock.patch.object(builtins, "input", side_effect=nutzer_eingaben):
        ohne_zahl = src.user_input.ohne_zahl("")
        konsolen_ausgaben = capsys.readouterr()
        assert konsolen_ausgaben.out == "Bitte keine Zahlen verwenden, versuche es nochmal.\n"
        assert ohne_zahl == "Hi"


def test_ohne_zahl_zwei_falsche_eingaben(capsys) -> None:
    nutzer_eingaben = iter(["", "2", "Hi"])
    with unittest.mock.patch.object(builtins, "input", side_effect=nutzer_eingaben):
        ohne_zahl = src.user_input.ohne_zahl("")
        konsolen_ausgaben = capsys.readouterr()
        assert (
            konsolen_ausgaben.out == "Es wurde nichts eingeben, versuche es nochmal.\n"
            "Bitte keine Zahlen verwenden, versuche es nochmal.\n"
        )
        assert ohne_zahl == "Hi"
