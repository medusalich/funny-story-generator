def user_input_ohne_zahl(text: str) -> str:
    """Frage den Nutzer nach einer Eingabe ohne Zahl""" 
    while True:
        worte = input(text)
        if not any(char.isdigit() for char in worte):
            return worte
        else:
            print("Bitte keine Zahlen verwenden, versuche es nochmal.")   


def user_input_ohne_buchstabe(text: str) -> int:
    """Frage den Nutzer nach einer Zahl"""    
    while True:
        zahl = input(text)
        if zahl.isdigit():
            return int(zahl)
        else:
            print("Bitte nur Zahlen verwenden, versuche es nochmal.")

