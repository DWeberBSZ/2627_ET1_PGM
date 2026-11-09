"""
10.11.26
╔══════════════════════════════════╗
║      ÜBUNG UND HAUSAUFGABE       ║
╚══════════════════════════════════╝
"""

"""
Ü3: Der Akkutest
================

Diese Aufgabe hat mit dem Kaminkehrerlauf nichts zu tun: In der Werkstatt wird ein
Akkupack geprüft. Jede Zelle wird einzeln gemessen. Eine Zelle unter 3000 mV ist
zu schwach.

Arbeitsauftrag:

> Schreiben Sie ein Programm, das Zellspannungen in mV einliest, bis ende
  eingegeben wird, und alle Messwerte in einer Liste speichert.

> Geben Sie danach die Anzahl der Messungen und den Durchschnitt aus.

> Melden Sie jede Messung unter 3000 mV mit ihrer Nummer. Die erste Messung hat
  die Nummer 1.

Testen Sie mit: 3700 · 3600 · 2800 · 3900 · 2900 · ende

So kann die Ausgabe aussehen (Beispiel):
    Spannung in mV: 3700
    …
    Spannung in mV: ende
    Messungen: 5
    Durchschnitt: … mV
    Messung 3 zu niedrig: 2800 mV
    …

Zusatz: Geben Sie die Messwerte zum Schluss rückwärts aus.

Zeit: ca. 35 Minuten, Einzelarbeit.

Übung und Hausaufgabe: fertig bis Dienstag, 17.11.
"""

# Ihr Code:






























# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Erst mit "ende" vergleichen, dann mit int() umwandeln – sonst gibt es einen
#   ValueError.
# - Der Durchschnitt ist Summe / Anzahl – erst NACH der Schleife.
# - Die Nummer einer Messung: for i in range(len(messwerte)): … messwerte[i] … i + 1
# - Zusatz rückwärts: Der letzte Index ist len(messwerte) - 1; eine while-Schleife,
#   in der der Index kleiner wird.
