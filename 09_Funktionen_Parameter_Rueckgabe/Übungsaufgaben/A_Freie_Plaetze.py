"""
24.11.26
╔══════════════════════════════════════╗
║  FUNKTIONEN – PARAMETER UND RETURN   ║
╚══════════════════════════════════════╝
"""
# Lernsituation: Wir digitalisieren den Kaminkehrerlauf
#                (Unterrichtsszenario — keine Anfrage der Veranstalter.)
#
# Für Kaminkehrer sind 30 Plätze reserviert, für Läufer gibt es 250 Plätze.
# Unser Programm soll die freien Plätze für beide Listen zeigen — mit EINER Funktion.
#
# Aufgabe 3a: Die Funktion.
#   Schreiben Sie hier oben die Funktion freie_plaetze(liste, plaetze) nach Ihrem PAP.
#   Sie rechnet die freien Plätze aus und gibt sie mit return zurück.
#   Test: print(freie_plaetze(["Rosa", "Max"], 30))   →   28

# ---------- Ihre Funktion (oben im Programm: erst merken, dann aufrufen)



# ---------- unsere Listen (die gibt es schon)
kaminkehrer = ["Rosa Glück", "Max Kehrer", "Xaver Ruß", "Toni Schlot"]
laeufer = ["Sofia Schneider", "Petra Ostermeier", "Lena Huber", "Emil Bauer", "Mia Vogel"]

# Aufgabe 3b: Das Programm.
#   Rufen Sie die Funktion für die Kaminkehrer (30 Plätze) und für die Läufer (250 Plätze) auf.
#   Merken Sie sich jedes Ergebnis in einer Variablen und geben Sie es aus.
#   Erwartete Ausgabe:   Freie Plätze Kaminkehrer: 26
#                        Freie Plätze Läufer: 245

# ---------- Ihr Programm



# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - 3a: Die Funktion steht auf dem Arbeitsblatt, Aufgabe 1, Zeilen 1 bis 3 — die Einrückung zählt.
# - 3a: In die Klammer hinter dem Namen kommen die zwei Parameter, mit Komma getrennt: liste, plaetze
# - 3a: Die Funktion steht OBEN im Programm — sonst: NameError: name 'freie_plaetze' is not defined.
# - 3a: Testen: print(freie_plaetze(["Rosa", "Max"], 30))   →   28
# - 3b: Der Aufruf mit den Werten in der Klammer, das Ergebnis in eine Variable: frei_k = freie_plaetze(kaminkehrer, 30)
# - 3b: Für die Läufer derselbe Aufruf — nur mit der anderen Liste und 250.
# - Fehlt return, gibt die Funktion None zurück — dann steht in der Ausgabe: None.
