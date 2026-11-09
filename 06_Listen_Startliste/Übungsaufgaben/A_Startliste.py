"""
10.11.26
╔══════════════════════════════════╗
║     LISTEN – DIE STARTLISTE      ║
╚══════════════════════════════════╝
"""

"""
Aufgabe 3: Die Startliste
=========================

Lernsituation: Wir digitalisieren den Kaminkehrerlauf
               (Unterrichtsszenario — keine Anfrage der Veranstalter.)

Aufgabe 3)
> Erweitern Sie unser Anmeldeprogramm nach dem PAP von der Tafel: Es speichert jeden
  Namen in einer Liste, weist doppelte Anmeldungen mit dem Hinweis „… ist schon
  angemeldet.“ ab und gibt am Ende die Anzahl und die Startliste aus — Startnummer
  und Name, Zeile für Zeile, ohne Lücke.

Vorher an der Tafel: unser PAP (Aufgabe 2). Setzen Sie ihn Schritt für Schritt um.

Testen Sie in EINEM Programmlauf mit diesen Eingaben:
    Sofia Schneider
    Petra Ostermeier
    Jonas Winkler
    Petra Ostermeier
    Emil Bauer
    ende

So kann die Ausgabe aussehen (Beispiel):
    Name: Sofia Schneider
    Startnummer 1 für Sofia Schneider
    …
    Petra Ostermeier ist schon angemeldet.
    …
    Name: ende
    Angemeldet: …
    Startliste
    1 Sofia Schneider
    …

Schon fertig?
> Nennen Sie bei einer doppelten Anmeldung auch die Startnummer, die der Läufer schon
  hat.

Fertig, wenn alles stimmt (Checkliste):
[ ] Testeingaben in einem Lauf: die zweite Petra bekommt den Hinweis, Emil hat die
    4, am Ende Angemeldet: 4 und die Startliste 1 bis 4.
[ ] Nur ende: Angemeldet: 0 und eine leere Startliste — ohne Fehlermeldung.
[ ] Mia Berger · Mia Berger · Lena Huber · Mia Berger · ende: Lena hat die 2,
    Angemeldet: 2.
[ ] Mein Programm folgt unserem PAP: Liste vor der Schleife, erst prüfen, dann
    anhängen.

Zeit: 25 Minuten, Einzelarbeit. Kopieren Sie diese Datei in Ihren eigenen Ordner.
"""

# Ihr Code:

# Unser Anmeldeprogramm vom 27.10. – erweitern Sie es:

print("Anmeldung Kaminkehrerlauf 2027")
startnummer = 1
name = input("Name: ")
while name != "ende":
    print("Startnummer", startnummer, "für", name)
    startnummer = startnummer + 1
    name = input("Name: ")
print("Angemeldet:", startnummer - 1)






























# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Halten Sie sich an den PAP von der Tafel – Baustein für Baustein.
# - Die Liste VOR der Schleife leer anlegen (Infoblatt Karte 1),
#   IN der Schleife jeden Namen mit append anhängen (Karte 4).
# - Anzahl: len (Karte 5). Startliste: mit for durch die Liste und die
#   Startnummer selbst mitzählen – sie ist Index + 1.
# - Doppelte: Erst prüfen, dann anhängen: if name in startliste: … else: … (Karte 6).
# - Die Startnummer darf nur weiterzählen, wenn wirklich jemand dazukommt.
# - Schon fertig? startliste.index(name) liefert den Index, an dem name steht –
#   die Startnummer ist Index + 1.
