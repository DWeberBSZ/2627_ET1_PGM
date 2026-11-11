"""
12.11.26
╔══════════════════════════════════╗
║LISTEN – UMMELDUNG ÜBER DIE STARTNUMMER║
╚══════════════════════════════════╝
"""

"""
Aufgabe 3a: Die Ummeldung über die Startnummer
==============================================

Lernsituation: Wir digitalisieren den Kaminkehrerlauf
               (Unterrichtsszenario — keine Anfrage der Veranstalter.)

Aufgabe 3a)
> Der alte Läufer wird über seine Startnummer eingegeben, Ende ist die Startnummer 0.
  Zu jeder Startnummer liest das Programm den neuen Läufer ein und ersetzt damit den
  alten auf der Startliste. Am Ende gibt es die Startliste aus.

Vorher an der Tafel: unser PAP (Aufgabe 2). Setzen Sie ihn Schritt für Schritt um.
Die Startliste aus der Anmeldung steht unten schon fertig da – so testen Sie schnell.

Testen Sie in EINEM Programmlauf mit diesen Eingaben:
    3
    Lena Huber
    1
    Mia Berger
    0

So kann die Ausgabe aussehen (Beispiel):
    Startnummer: 3
    Neuer Läufer: Lena Huber
    Startnummer: 1
    Neuer Läufer: Mia Berger
    Startnummer: 0
    ['Mia Berger', 'Petra Ostermeier', 'Lena Huber', 'Emil Bauer']

Schon fertig?
> Prüfen Sie die Eingabe: Bei Startnummer 7 bzw. einem Namen, der nicht auf der Liste
  steht, erscheint „Diesen Läufer gibt es nicht.“ statt eines Fehlers.
> Geben Sie am Ende die Startliste mit Startnummern aus: „1 Mia Berger“, „2 Petra
  Ostermeier“ …

Fertig, wenn alles stimmt (Checkliste):
[ ] a) und b) mit den Testeingaben: Am Ende steht ['Mia Berger', 'Petra Ostermeier',
    'Lena Huber', 'Emil Bauer'].
[ ] Nur 0 bzw. nur „ende“: Die Startliste bleibt, wie sie war.
[ ] Startnummer 4 bzw. Emil Bauer, der letzte: Er wird ersetzt — ohne Fehlermeldung.
[ ] Beide Programme folgen unserem PAP: Eingabe vor der Schleife und am Ende des
    Rumpfs.

Zeit: 30 Minuten für 3a und 3b, Einzelarbeit. Kopieren Sie diese Datei in Ihren eigenen Ordner.
"""

# Ihr Code:

# Die Startliste aus der Anmeldung (10.11.) – die Anmeldung ist geschlossen:
startliste = ["Sofia Schneider", "Petra Ostermeier", "Jonas Winkler", "Emil Bauer"]

# Ab hier die Ummeldung:































# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Halten Sie sich an den PAP von der Tafel – Baustein für Baustein.
# - „Eingabe des alten Läufers“ heißt hier: seine Startnummer einlesen.
# - Die Schleife ist dieselbe wie am Dienstag: Eingabe vor der Schleife, 
#   while nummer != 0:, Eingabe am Ende des Rumpfs.
# - input liefert Text – für eine Startnummer brauchen Sie int(input(...)).
# - Startnummer 3 steht an Index 2: startliste[nummer - 1] (Infoblatt oben und Karte 1).
# - Ersetzen: Der Zugriff steht LINKS vom =: startliste[nummer - 1] = neu (Karte 1).
#   Nicht append und nicht insert – die machen die Liste länger (Karte 2).
# - Schon fertig? Eine Startnummer gibt es nur von 1 bis len(startliste):
#   if 1 <= nummer <= len(startliste): … else: …
