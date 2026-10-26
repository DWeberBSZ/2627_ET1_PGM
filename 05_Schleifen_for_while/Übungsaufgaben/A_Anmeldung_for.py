"""
27.10.26
╔══════════════════════════════════╗
║      SCHLEIFEN – GRUPPE FOR      ║
╚══════════════════════════════════╝
"""

"""
Aufgabe 2: Beliebig viele Anmeldungen – Gruppe for
==================================================

Lernsituation: Wir digitalisieren den Kaminkehrerlauf
               (Unterrichtsszenario — keine Anfrage der Veranstalter.)

Gruppe for: Nutzen Sie die for-Schleife.

2a)
> Schreiben Sie in Einzelarbeit ein Programm, um mehrere Läufer anzumelden. Bei einer
  Anmeldung gibt ein Läufer Name und Jahrgang an und bekommt als Ausgabe seine Startnummer.

2b)
> Geben Sie am Ende aus, wie viele Läufer angemeldet sind und wie viel Startgeld
  zusammenkommt.

Startgeld:
    Startgeld        18 €
    bis 13 Jahre     12 €      (Alter = 2027 − Jahrgang)

Testen Sie mit diesen vier Läufern:
    Lena Huber        2010
    Jonas Meier       1988
    Mia Berger        2015
    Sofia Schneider   1970

So kann die Ausgabe aussehen (Beispiel):
    Anmeldung Kaminkehrerlauf 2027
    Name: Lena Huber
    Jahrgang: 2010
    Startnummer 1 für Lena Huber
    …
    Angemeldet: …
    Startgeld: … €

Schon fertig?
> Erweitern Sie Ihr Programm: Jeder Läufer wählt zusätzlich seine Strecke (5 oder 10 km).
  Geben Sie am Ende aus, wie viele Läufer auf jeder Strecke starten.

Zeit: 30 Minuten, Einzelarbeit. Erstellen Sie ein neues Skript in Ihrem eigenen Ordner.
"""

# Ihr Code:































# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - for braucht die Anzahl, BEVOR die Schleife beginnt. Woher kann sie kommen?
#   Infoblatt Karte 6: range mit einer Variablen, z. B. aus einer Eingabe.
# - Die Schleifenvariable kann gleich die Startnummer sein.
# - Name und Jahrgang werden IN der Schleife abgefragt – für jeden Läufer neu.
# - 2b: Die Summe des Startgelds beginnt VOR der Schleife bei 0 (Infoblatt Karte 2).
#   In der Schleife: Alter berechnen, mit if entscheiden, 12 oder 18 dazuzählen.
# - Schon fertig? Zwei Zähler (5 km, 10 km), beide beginnen vor der Schleife bei 0.
