def ohne_zahl(text: str) -> str:
    """Frage den Nutzer nach einer nicht leeren Eingabe ohne Zahl"""
    while True:
        nutzer_eingabe = input(text)
        if nutzer_eingabe == "":
            print("Es wurde nichts eingeben, versuche es nochmal.")
        elif not any(char.isdigit() for char in nutzer_eingabe):
            return nutzer_eingabe
        else:
            print("Bitte keine Zahlen verwenden, versuche es nochmal.")


def ohne_buchstabe(text: str) -> int:
    """Frage den Nutzer nach einer Zahl"""
    while True:
        nutzer_eingabe = input(text)
        if nutzer_eingabe.isdigit():
            return int(nutzer_eingabe)
        else:
            print("Bitte nur Zahlen verwenden, versuche es nochmal.")
