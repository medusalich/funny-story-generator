#!/usr/bin/env python
import random

import age
import user_input



def erfrage_geschlecht() -> str:
    """Erzeugt eine Einstufung abhängig vom Geschlecht."""
    while True:
        geschlecht_input = user_input.ohne_zahl("\n(männlich/weiblich/divers)Bitte gib dein Geschlecht ein: ").lower()
        if geschlecht_input in ["m", "männlich"]:
            return "er"
        elif geschlecht_input in ["w", "weiblich"]:
            return "sie"
        elif geschlecht_input in ["d", "divers"]:
            return "er/sie"
        else:
            print("Bitte gib nur 'männlich', 'weiblich' oder 'divers' ein.")


def gestalte_story_einleitung() -> str:
    """Erzeugt einen Wechsel am Story Anfang."""
    story_einleiten = (
        "In einem weit entfernten Königreich, ",
        "Es war einmal ",
        "Vor langer langer Zeit ",
        "In einer stürmischen Nacht, ",
        "In einer Welt, in der die Zeit stillzustehen schien, ",
    )
    random_element = random.choice(story_einleiten)
    return random_element


def gestalte_story_wetter() -> str:
    """Erzeugt einen Wechsel des Wetters."""
    story_wetter = (
        "sonnigen",
        "nebeligen",
        "verschneiten",
        "regnerischen",
        "wolkigen",
    )
    random_wetter_element = random.choice(story_wetter)
    return random_wetter_element


def erfrage_aktivitaet() -> str:
    """Erfrage Aktivität und setze 'zu' ein"""
    story_abschnitt_aktivitaet = user_input.ohne_zahl("\nGib ein, was du jetzt gerne am liebsten tun würdest: ")
    aktivitaet_split = story_abschnitt_aktivitaet.strip().rsplit(" ", 1)
    aktivitaet_split.insert(-1, "zu")
    story_abschnitt_aktivitaet = " ".join(aktivitaet_split)
    return story_abschnitt_aktivitaet


def gestalte_story() -> None:
    """Erzeuge Story durch User-Eingaben"""
    print("Herzlich willkommen und viel Spaß beim Gestalten deiner Geschichte")

    name = user_input.ohne_zahl("\nGib deinen Namen ein: ")
    gegenstand = user_input.ohne_zahl(f"\nHallo {name}, bitte nenne mir deinen liebsten Gegenstand: ")
    monat = user_input.ohne_zahl("\nGib einen Monat ein: ")
    ort = user_input.ohne_zahl("\nGib einen Ort ein, an dem du jetzt gerne wärst: ")

    aktivitaet = erfrage_aktivitaet()
    geschlecht = erfrage_geschlecht()
    alter = user_input.ohne_buchstabe("\nNenne mir dein Alter in Zahlenform: ")
    alters_einstufung = age.stufe_alter_ein(alter)
    funfact_jahrzehnt = age.erzeuge_funfact(alter)

    print("\nHier folgt deine für dich geschriebene Geschichte:")
    print(f"\n{gestalte_story_einleitung()} eine {alters_einstufung} namens {name}, " + f"sie liebte es {aktivitaet}.")
    print(f"{geschlecht} ist in dem Jahrzehnt, {funfact_jahrzehnt} geboren.")
    print(
        f"An einem {gestalte_story_wetter()} Tag im {monat}"
        + f"nahm {geschlecht} seinen/ihren wichtigsten {gegenstand} und ging zum {ort}."
    )


def main() -> None:
    """Start der Story und Neustartabfrage"""
    while True:
        gestalte_story()
        neustart_erfragen = input("Soll der Spaß von vorn anfangen? (ja/nein): ").lower()
        if neustart_erfragen == "ja":
            continue
        elif neustart_erfragen == "nein":
            print("Vielen Dank fürs mitmachen")
            break
        else:
            print("Bitte nur ja oder nein eingeben, versuche es nochmal.")


if __name__ == "__main__":
    main()
