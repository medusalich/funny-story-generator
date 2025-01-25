#!/usr/bin/env python
import alter
import user_input
import random


def geschlecht_erfragen() -> str:
    """Erzeugt eine Einstufung abhängig vom Geschlecht."""
    while True:
        geschlecht_input = user_input.user_input_ohne_zahl("\n(männlich/weiblich/divers)Bitte gib dein Geschlecht ein: ")   
        if geschlecht_input in ["m", "männlich"]:
            return "er"
        elif geschlecht_input in ["w", "weiblich"]:
            return "sie"
        elif geschlecht_input in ["d", "divers"]:
            return "er/sie"
        else:
            print("Bitte gib nur 'männlich', 'weiblich' oder 'divers' ein.") 


def einleitung_der_story() -> str:
    """Erzeugt einen Wechsel am Story Anfang."""
    story_einleiten = (
        "In einem weit entfernten Königreich, ",
        "Es war einmal ",
        "Vor langer langer Zeit ",
        "In einer stürmischen Nacht, ",
        "In einer Welt, in der die Zeit stillzustehen schien, "
    )
    random_element = random.choice(story_einleiten)
    return random_element


def wetter_storyabschnitt() -> str:
    """Erzeugt einen Wechsel des Wetters."""
    story_wetter = (
        "sonnigen",
        "nebeligen",
        "verschneiten",
        "bewölkten",
        "wolkigen"
    )
    random_wetter_element = random.choice(story_wetter)
    return random_wetter_element


def aktivitaet_erfragen() -> str:
    """Erfrage Aktivität und setze 'zu' ein"""
    story_abschnitt_aktivitaet = user_input.user_input_ohne_zahl("\nGib ein, was du jetzt gerne am liebsten tun würdest: ")
    aktivitaet_split = story_abschnitt_aktivitaet.strip().rsplit(" ", 1)
    aktivitaet_split.insert(-1, "zu")
    story_abschnitt_aktivitaet = " ".join(aktivitaet_split)      
    return story_abschnitt_aktivitaet
        

def main() -> None:
    print("Herzlich willkommen und viel Spaß beim Gestalten deiner Geschichte")
    
    name = user_input.user_input_ohne_zahl("\nGib deinen Namen ein: ")
    gegenstand = user_input.user_input_ohne_zahl(f"\nHallo {name}, bitte nenne mir deinen liebsten Gegenstand: ")
    monat = user_input.user_input_ohne_zahl("\nGib einen Monat ein: ")
    ort = user_input.user_input_ohne_zahl("\nGib einen Ort ein, an dem du jetzt gerne wärst: ")

    story_abschnitt_aktivitaet = aktivitaet_erfragen()
    story_abschnitt_geschlecht = geschlecht_erfragen()
    story_abschnitt_alter = user_input.user_input_ohne_buchstabe("\nNenne mir dein Alter in Zahlenform: ")
    alters_einstufung = alter.alter_einstufen(story_abschnitt_alter)
    funfact_jahrzehnt = alter.alter_funfact(story_abschnitt_alter)

    print("\nHier folgt deine für dich geschriebene Geschichte:")
    print(f"\n{einleitung_der_story()} eine {alters_einstufung} namens {name}, sie liebte es {story_abschnitt_aktivitaet}.")
    print(f"{story_abschnitt_geschlecht} ist in dem Jahrzehnt, {funfact_jahrzehnt} geboren.")
    print(f"An einem {wetter_storyabschnitt()} Tag im {monat} nahm {story_abschnitt_geschlecht} seinen/ihren wichtigsten {gegenstand} und ging zum {ort}.")


if __name__ == "__main__":
    main()
