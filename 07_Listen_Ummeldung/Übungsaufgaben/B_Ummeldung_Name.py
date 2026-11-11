"""
12.11.26
╔══════════════════════════════════╗
║LISTEN – UMMELDUNG ÜBER DEN NAMEN ║
╚══════════════════════════════════╝
"""

"""
Aufgabe 3b: Die Ummeldung über den Namen
========================================

Lernsituation: Wir digitalisieren den Kaminkehrerlauf
               (Unterrichtsszenario — keine Anfrage der Veranstalter.)

Aufgabe 3b)
> Der alte Läufer wird über seinen Namen eingegeben, Ende ist „ende“. Sonst wie a).
  Den Platz des alten Läufers findet startliste.index(alt) (Infoblatt Karte 4).

Vorher an der Tafel: unser PAP (Aufgabe 2). Setzen Sie ihn Schritt für Schritt um.
Die Startliste aus der Anmeldung steht unten schon fertig da – so testen Sie schnell.

Testen Sie in EINEM Programmlauf mit diesen Eingaben:
    Jonas Winkler
    Lena Huber
    Sofia Schneider
    Mia Berger
    ende

So kann die Ausgabe aussehen (Beispiel):
    Alter Läufer: Jonas Winkler
    Neuer Läufer: Lena Huber
    Alter Läufer: Sofia Schneider
    Neuer Läufer: Mia Berger
    Alter Läufer: ende
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
# - Derselbe PAP wie bei 3a – nur „Eingabe des alten Läufers“ heißt jetzt: den Namen einlesen.
# - Ende ist jetzt der Text "ende" – wie am Dienstag: while alt != "ende":
# - Ein Name ist kein Index. Den Platz findet startliste.index(alt) (Infoblatt Karte 4).
# - Ersetzen: platz = startliste.index(alt), dann startliste[platz] = neu.
# - Schon fertig? Steht der Name nicht in der Liste, gibt index einen Fehler –
#   vorher prüfen: if alt in startliste: … else: …
