#!/usr/bin/env python
import alter
import user_input


def geschlecht_erfragen() -> str:
    geschlecht = input("\n(männlich/weiblich/divers)Bitte gib dein Geschlecht ein: ")
    
    if geschlecht == "männlich":
        return "Er"
    elif geschlecht == "weiblich":
        return "Sie"
    elif geschlecht == "divers":
        return "Er/Sie"
    else:
        raise NotImplementedError


def main():

    print("Herzlich willkommen und viel Spaß beim Gestalten deiner Geschichte")
    
    name = user_input.user_input_ohne_zahl("\nGib deinen Namen ein: ")
    
    gegenstand = user_input.user_input_ohne_zahl(f"\nHallo {name}, bitte nenne mir deinen liebsten Gegenstand: ")
    
    monat = user_input.user_input_ohne_zahl("\nGib einen Monat ein: ")

    ort = user_input.user_input_ohne_zahl("\nGib einen Ort ein, an dem du jetzt gerne wärst: ")
    
    aktivitaet = user_input.user_input_ohne_zahl("\nGib ein, was du jetzt gerne am liebsten tun würdest: ")

    story_abschnitt_alter = user_input.user_input_ohne_buchstabe("\nNenne mir dein Alter in Zahlenform: ")
    alters_einstufung = alter.alter_einstufen(story_abschnitt_alter)
    funfact_jahrzehnt = alter.alter_funfact(story_abschnitt_alter)

    print("\nHier folgt deine für dich geschriebene Geschichte:")
    
    print(f"\nEs war einmal im {monat} eine Person namens {name}, die jetzt gern im {ort} wäre.")
    print(f"{alters_einstufung}, die im Jahrzehnt, {funfact_jahrzehnt}, geboren wurde.")
    print(f"{name} mag es am liebsten, mit dem {gegenstand} zu {aktivitaet}.")


if __name__ == "__main__":
    main()
