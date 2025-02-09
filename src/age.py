import datetime
import math


def stufe_alter_ein(alter: int) -> str:
    """Erzeugt eine Alterseinstufung abhängig vom Alter."""
    if 0 <= alter < 27:
        return "junge Person"
    elif 27 <= alter <= 59:
        return "erwachsene Person"
    elif 60 <= alter <= 122:
        return "ältere Person"
    elif alter > 122:
        return "unglaubwürdige Person"
    else:
        return "noch nicht geborene Person"


def erzeuge_funfact(alter: int) -> str:
    """Erzeugt einen Funfact nach Geburtsjahrzehnt."""
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
        2020: "als „Zoom“ ein neues Synonym für „Treffen“ war",
    }

    if alter >= 0:
        aktuelles_jahr = datetime.datetime.now().year
        geburtsjahr = aktuelles_jahr - alter
        geburtsjahr_abgerundet = math.floor(geburtsjahr / 10) * 10

        if geburtsjahr_abgerundet in funfacts:
            funfact = funfacts[geburtsjahr_abgerundet]
        else:
            funfact = "als es keine Funfacts gab"
        return funfact
    return "404 ERROR"
