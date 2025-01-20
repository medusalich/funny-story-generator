import datetime
import math


def alter_erfragen() -> int:
    """Frage Alter des Nutzers ab."""    
    while True:
        try:
            alter = int(input("\nNenne mir dein Alter in Zahlenform: "))
            return alter
        except ValueError:
            print("Bitte eine Zahl eingeben:")


def alter_einstufen(alter: int) -> str:
    """Erzeugt eine Alterseinstufung abhängig vom Alter."""
    junger_mensch = 0 <= alter < 27
    erwachsener_mensch = 27 <= alter <= 59 
    alter_mensch = 60 <= alter <= 122
    zu_alter_mensch = alter > 122

    if junger_mensch:
        return "Die junge Person"
    elif erwachsener_mensch:
        return "Die erwachsene Person"
    elif alter_mensch:
        return "Die ältere Person"
    elif zu_alter_mensch:
        return "Die unglaubwürdige Person"
    else:
        return "Versuch es nochmal^^"


def alter_funfact(alter: int) -> str:
    """Erzeugt eine Funfact nach Geburtsjahrzehnt."""
    funfacts = {
        1900: "als Autos noch mit Pferden um die Wette fuhren",
        1910: "als das erste Telefon mit Wählscheibe herauskam",
        1920: "als es Cola aus Glasflaschen gab",
        1930: "als man für einen Brief eine Woche auf Antwort warten musste",
        1940: "als der erste elektronische Computer ENIAC gebaut wurde",
        1950: "als der Rock'n'Roll die Welt eroberte",
        1960: "als Juri Gagarin als erster Mensch im All war",
        1970: "als das erste Handy von Martin Cooper erfunden wurde",
        1980: "als die Gurtpflicht auch für die Rückbank galt",
        1990: "als Tamagotchis populär wurden",
        2000: "als die D-Mark verabschiedet wurde",
        2010: "als Sprachassistenz-Geräte beliebte Gesprächspartner wurden",
        2020: "als „Zoom“ ein neues Synonym für „Treffen“ war"
    }

    aktuelles_jahr = datetime.datetime.now().year
    geburtsjahr = aktuelles_jahr - alter
    geburtsjahr_abgerundet = math.floor(geburtsjahr / 10 ) * 10
    funfact = funfacts[geburtsjahr_abgerundet]
    return funfact
