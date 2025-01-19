#!/usr/bin/env python
import alter

def main():

    print("Herzlich willkommen und viel Spaß beim Gestalten deiner Geschichte")
    
    name = input("\nGib deinen Namen ein: ")
    
    gegenstand = input(f"\nHallo {name}, bitte nenne mir deinen liebsten Gegenstand: ")
    
    monat = input("\nGib einen Monat ein: ")

    ort = input("\nGib einen Ort ein, an dem du jetzt gerne wärst: ")
    
    aktivitaet = input("\nGib ein, was du jetzt gerne am liebsten tun würdest: ")

    story_abschnitt_alter = alter.alter_erfragen()
    alters_einstufung = alter.alter_einstufen(story_abschnitt_alter)
    funfact_jahrzehnt = alter.alter_funfact(story_abschnitt_alter)

    print("\nHier folgt deine für dich geschriebene Geschichte:")
    
    print(f"\nEs war einmal im {monat} eine Person namens {name}, die jetzt gern im {ort} wäre.")
    print(f"{alters_einstufung}, die im Jahrzehnt, {funfact_jahrzehnt}, geboren wurde.")
    print(f"{name} mag es am liebsten, mit dem {gegenstand} zu {aktivitaet}.")


if __name__ == "__main__":
    main()
