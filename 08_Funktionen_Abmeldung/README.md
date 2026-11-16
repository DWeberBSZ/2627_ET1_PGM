# 08 – Funktionen: Wir bauen die Abmeldung

*Zuletzt aktualisiert: 17.11.2026 – Unterricht vom 17.11.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 9. Dazu das
[Infoblatt mit Arbeitsblatt](Infoblatt_Arbeitsblatt_Funktionen.pdf).

**Leitsatz: Code einmal schreiben – mehrmals verwenden.**

## Lernziele

- Begründen, warum man Programmcode, den man mehrmals braucht, als Funktion schreibt
- Die Teile einer Funktion benennen: `def`, Funktionsname, Klammern und Doppelpunkt, Rumpf; den Aufruf
- Angeben, in welcher Reihenfolge Python ein Programm mit einer Funktion ausführt
- Vorhandenen Programmcode in eine Funktion verschieben und sie aufrufen: `zeige_display()`
- Eine Funktion in einem zweiten Programmteil wiederverwenden: die Abmeldung
- Ein Element mit `remove` aus einer Liste entfernen

## Die Lernsituation

**Wir digitalisieren den Kaminkehrerlauf.** *Unterrichtsszenario – keine Anfrage der Veranstalter.*

Wir spielen den Lauftag durch. Der Lauf hat 250 Startplätze und ist ausgebucht. 8:40 Uhr: Thomas meldet
sich ab. 9:30 Uhr: Kaminkehrer Toni will kurzfristig mitlaufen – ein Platz ist ja frei geworden. Aber das
Programm zeigt „Plätze übrig: 0“.

Dafür brauchen wir zwei Dinge:

1. Das Display wird zur Funktion.
2. Die Abmeldung verwendet es wieder.

## So läuft die Stunde

1. **Infoblatt** lesen (Einzelarbeit).
2. **Aufgabe 1 – Aufbau einer Funktion** (Partnerarbeit mit dem Banknachbarn): an unserem Display
   `zeige_display()` die Teile benennen und die Reihenfolge der Zeilen angeben. Gesichert wird an der Tafel.
3. **Aufgabe 2 – Unser Ablauf als PAP** (Partnerarbeit): den Ablauf mit Auswahl, Anmeldung und Abmeldung als
   PAP planen – mit dem Symbol für den Aufruf einer Funktion. Gesichert wird an der Tafel.
4. **Aufgabe 3 – Display und Abmeldung** (Einzelarbeit,
   [`A_Abmeldung.py`](Übungsaufgaben/A_Abmeldung.py)): umsetzen – a) das Display wird zur Funktion,
   b) die Abmeldung nach dem eigenen PAP.
5. **Übungsphase:** Aufgabe 3 fertigstellen, dann [`Ü1_Urkunde.py`](Übungsaufgaben/Ü1_Urkunde.py)
   und [`Ü2_Bestzeit.py`](Übungsaufgaben/Ü2_Bestzeit.py).

## Eine Funktion schreiben

Jeder Läufer bekommt nach der Anmeldung dieselbe Info – einmal geschrieben, zweimal verwendet:

```python
def zeige_info():
    print("Start: 10 Uhr")
    print("Viel Erfolg!")

print("Angemeldet: Sofia")
zeige_info()
print("Angemeldet: Emil")
zeige_info()
```

- `def` – das Schlüsselwort: Hier beginnt eine Funktion.
- `zeige_info` – der Funktionsname. Sie wählen ihn selbst; er sagt, was die Funktion tut.
- `():` – ein Klammerpaar und ein Doppelpunkt gehören immer dazu.
- Eingerückt darunter – der Rumpf: das tut die Funktion.

## Eine Funktion aufrufen

```python
zeige_info()
```

Der Aufruf: der Name mit Klammern. Python springt in die Funktion, führt den Rumpf aus und macht
hinter dem Aufruf weiter. Aufrufen kann man eine Funktion so oft man will – das ist Wiederverwenden.

## In welcher Reihenfolge?

Python **merkt** sich die Funktion nur. Sie läuft erst beim **Aufruf** – deshalb steht `def` oben.

```python
def zeige_display():                    # 1  nur merken
    anzahl = len(startliste)            # 4
    uebrig = 250 - anzahl                # 5
    print("Angemeldet:", anzahl)        # 6
    print("Plätze übrig:", uebrig)      # 7

startliste = ["Sofia", "Emil"]          # 2
zeige_display()                         # 3  Aufruf
print("Der Nächste, bitte!")            # 8
```

## Im PAP

Für den Aufruf einer Funktion gibt es ein eigenes Symbol: den Kasten mit dem doppelten Rand
(Unterprogramm). In diesem Symbol steckt der ganze PAP der Funktion.

## Neu bei den Listen: ein Element entfernen

```python
helfer = ["Anna", "Ben", "Cem"]
helfer.remove("Ben")       # ['Anna', 'Cem']
```

## Typische Fehler

- Die Funktion steht unter dem Aufruf – `NameError: name 'zeige_display' is not defined`
- Aufruf ohne Klammern: `zeige_display` statt `zeige_display()` – es passiert nichts
- Der Rumpf ist nicht eingerückt – `IndentationError`
- Klammern oder Doppelpunkt hinter dem Namen vergessen – `SyntaxError`
- Die vier Zeilen stehen ein zweites Mal im Programm, statt die Funktion aufzurufen
- `remove` mit einem Namen, der nicht in der Liste steht – `ValueError`

## Dateien in diesem Ordner

- [`Infoblatt_Arbeitsblatt_Funktionen.pdf`](Infoblatt_Arbeitsblatt_Funktionen.pdf) – Infoblatt und Arbeitsblatt (Aufgabe 1 bis 3) der Stunde
- [`Übungsaufgaben/A_Abmeldung.py`](Übungsaufgaben/A_Abmeldung.py) – Aufgabe 3a und 3b: unser Programm
  mit der Anmeldung; Tipps ganz unten in der Datei
- [`Übungsaufgaben/Ü1_Urkunde.py`](Übungsaufgaben/Ü1_Urkunde.py) – eine Funktion schreiben und dreimal aufrufen
- [`Übungsaufgaben/Ü2_Bestzeit.py`](Übungsaufgaben/Ü2_Bestzeit.py) – eine Funktion nach jeder neuen Zeit aufrufen
- [`Ergebnisse/`](Ergebnisse/) – was wir in der Stunde gemeinsam erarbeiten
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für Ihren KI-Tutor (Stand Thema 08)

Keine Hausaufgabe zu dieser Stunde.
