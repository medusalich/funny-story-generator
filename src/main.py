#!/usr/bin/env python


def main():

    print("Herzlich willkommen und viel Spaß", "\n")
    
    name = input("Gib deinen Namen ein: ")
    print("Hallo", name, "\n")

    gegenstand = input("Nenne mir deinen liebsten Gegenstand: ")
    print("Liebster Gegenstand:", gegenstand, "\n")

    monat = input("Gib einen Monat ein: ")
    print("Der Monat lautet:", monat, "\n")

    ort = input("Gib einen Ort ein, an dem du jetzt gerne wärst: ")
    print("Der Ort lautet:", ort, "\n")

    aktivitaet = input("Gib ein, was du jetzt gerne am liebsten tun würdest: ")
    print("Du würdest jetzt gerne:", aktivitaet, "\n")

    print("Hier folgt deine für dich geschriebene Geschichte:", "\n")

    print("Es war einmal im", monat, "eine Person namens", name, ", die jetzt gern im", ort, "wäre.")
    print(name, "mag es am liebsten, mit dem", gegenstand, "zu", aktivitaet, ".")


if __name__ == "__main__":
    main()
