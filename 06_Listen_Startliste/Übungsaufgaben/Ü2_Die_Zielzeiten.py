"""
10.11.26
╔══════════════════════════════════╗
║      ÜBUNG UND HAUSAUFGABE       ║
╚══════════════════════════════════╝
"""

"""
Ü2: Die Zielzeiten
==================

Lernsituation: Wir digitalisieren den Kaminkehrerlauf
               (Unterrichtsszenario — keine Anfrage der Veranstalter.)

Nach dem Lauf liegen die Zielzeiten der 10,5-km-Strecke vor – in Minuten und in
der Reihenfolge der Startnummern: Der erste Wert gehört zu Startnummer 1, der
zweite zu Startnummer 2 und so weiter. Die Liste steht unten schon im Code.

Arbeitsauftrag:

> Geben Sie aus, wie viele Läufer im Ziel sind.

> Finden Sie die schnellste Zeit – ohne min() – und geben Sie die Startnummer dazu
  aus.

> Zählen Sie, wie viele Läufer unter 50 Minuten geblieben sind.

So kann die Ausgabe aussehen (Beispiel):
    Läufer: …
    Schnellste Zeit: … min
    Startnummer: …
    Unter 50 Minuten: …

Zeit: ca. 25 Minuten, Einzelarbeit.

Übung und Hausaufgabe: fertig bis Dienstag, 17.11.
"""

# Ihr Code:

# Zielzeiten der 10,5-km-Strecke in Minuten, in der Reihenfolge der Startnummern
zeiten = [52, 47, 61, 45, 58, 49]






























# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Schnellste Zeit: Startwert ist der ERSTE Eintrag, zeiten[0] – nicht 0!
#   Dann jeden Wert vergleichen: if zeit < schnellste: …
# - Startnummer = Index + 1. Den Index eines Werts liefert zeiten.index(wert).
# - Unter 50 Minuten: ein Zähler, der VOR der Schleife bei 0 beginnt.
