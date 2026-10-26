"""
27.10.26
╔══════════════════════════════════╗
║      ÜBUNG UND HAUSAUFGABE       ║
╚══════════════════════════════════╝
"""

"""
Ü3: Die Messreihe
=================

Diese Aufgabe hat mit dem Kaminkehrerlauf nichts zu tun: Ein Temperatursensor an
einer Maschine liefert während einer Schicht viele Messwerte. Unser Programm soll
sie alle auswerten, ohne dass man es für jeden Messwert neu startet.

Arbeitsauftrag:

> Schreiben Sie ein Programm, das Messwerte in °C einliest, bis ende eingegeben
  wird, und zu jedem Messwert eine Meldung ausgibt:

      unter 60 °C              normal
      60 °C bis unter 80 °C    WARNUNG
      ab 80 °C                 ABSCHALTUNG

> Geben Sie am Ende aus: die Anzahl der Messungen, der Warnungen und der
  Abschaltungen sowie den Durchschnitt aller Messwerte.

> Entscheiden Sie selbst, ob Sie for oder while verwenden, und begründen Sie
  Ihre Wahl in einem Kommentar oben im Programm.

Testen Sie mit: 55 · 72.5 · 81 · 64 · 40 · ende

So kann die Ausgabe aussehen (Beispiel):
    Messwert: 55
    55.0 °C normal
    Messwert: 72.5
    72.5 °C WARNUNG
    …
    Messwert: ende
    Messungen    : 5
    Warnungen    : 2
    Abschaltungen: 1
    Durchschnitt : 62.5 °C

Zusatz: Geben Sie auch den höchsten Messwert aus – ohne max().

Zeit: ca. 35 Minuten, Einzelarbeit.

Übung und Hausaufgabe: fertig bis Dienstag, 10.11.
"""

# Begründung for oder while:

# Ihr Code:































# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Die Eingabe ist Text: Erst mit "ende" vergleichen, dann mit float() umwandeln.
# - Zähler und Summe beginnen VOR der Schleife bei 0.
# - Durchschnitt = Summe / Anzahl der Messungen.
# - Zusatz: Merken Sie sich den bisher höchsten Wert in einer Variablen und
#   vergleichen Sie jeden neuen Messwert damit.
