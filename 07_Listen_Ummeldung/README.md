# 07 – Listen: einzelne Elemente lesen und ändern (die Ummeldung)

*Zuletzt aktualisiert: 12.11.2026 – Unterricht vom 12.11.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 7.1 (1. Aufl. S. 112–115). Dazu das
[Infoblatt mit Arbeitsblatt](Infoblatt_Arbeitsblatt_Ummeldung.pdf).

## Lernziele

- Ein einzelnes Element einer Liste über seinen Index lesen
- Ein einzelnes Element über den Index ändern: `liste[i] = wert`
- Startnummer und Index auseinanderhalten: Startnummer 3 ist `startliste[2]`, allgemein `startliste[nummer - 1]`
- Den Platz eines Elements mit `index` finden: `startliste.index("Jonas Winkler")`
- Die Ummeldung als PAP planen und umsetzen

## Die Lernsituation

**Wir digitalisieren den Kaminkehrerlauf.** *Unterrichtsszenario – keine Anfrage der Veranstalter.*
Die Anmeldung ist geschlossen, die Startliste steht. Jonas Winkler schreibt: „Ich kann am Samstag
leider nicht laufen. Meine Kollegin Lena Huber übernimmt meine Startnummer 3.“ Unser Programm muss
also genau einen Namen auf der Startliste austauschen – über die Startnummer.

## So läuft die Stunde

1. **Infoblatt** lesen (Einzelarbeit).
2. **Aufgabe 1 – Vom PAP zu Python** (Partnerarbeit mit dem Banknachbarn): Welcher Python-Befehl
   setzt den PAP-Baustein um? Gesichert wird an der Tafel-App.
3. **Aufgabe 2 – Unser Ablauf als PAP** (Partnerarbeit, Partnerkarten): Das Programm liest
   ein, welcher Läufer sich ummeldet, bis Ende eingegeben wird. Zu jedem alten Läufer liest es
   den neuen ein und ersetzt damit den alten auf der Startliste. Am Ende gibt es die Startliste
   aus. Der Ablauf ähnelt dem PAP vom Dienstag.
4. **Aufgabe 3 – Die Ummeldung** (Einzelarbeit): Erweitern Sie Ihre Anmeldung um die Ummeldung
   und setzen Sie das Programm aus dem PAP um — a) mit der Startnummer des alten Läufers
   ([`A_Ummeldung_Startnummer.py`](Übungsaufgaben/A_Ummeldung_Startnummer.py)), b) mit seinem
   Namen ([`B_Ummeldung_Name.py`](Übungsaufgaben/B_Ummeldung_Name.py)).

## Platz und Index

Jedes Element hat einen **Index**. Er beginnt bei **0**. Wir Menschen zählen ab 1:
**Platz = Index + 1**.

```python
helfer = ["Anna", "Ben", "Cem", "Dana"]
#           0       1      2      3      ← Index
#           1       2      3      4      ← Platz
```

## Ein Element lesen

```python
helfer[1]      # "Ben"
helfer[0]      # "Anna" – der erste
platz = 3
helfer[platz - 1]   # "Cem" – Platz 3 ist Index 2
```

## Ein Element ändern

Steht der Zugriff **links vom `=`**, wird das Element **ersetzt**. Die Liste bleibt gleich lang.

```python
helfer[1] = "Emil"      # ['Anna', 'Emil', 'Cem', 'Dana']  – Ben ist ersetzt
helfer.append("Emil")   # ['Anna', 'Ben', 'Cem', 'Dana', 'Emil'] – hinten angehängt
```

## Einfügen

`insert` schiebt einen Wert an einen Platz – alle dahinter rutschen nach, die Liste wird länger.

```python
helfer.insert(1, "Emil")   # ['Anna', 'Emil', 'Ben', 'Cem', 'Dana']
```

## Eine Zahl einlesen

`input` liefert immer Text. Für einen Index braucht man eine Zahl:

```python
platz = int(input("Platz: "))
print(helfer[platz - 1])
```

## Zusatz: Wo steht es?

```python
helfer.index("Cem")     # 2 – der Index, an dem "Cem" steht
```

## Typische Fehler

- `startliste[nummer]` statt `startliste[nummer - 1]` – es trifft den Läufer dahinter, bei der letzten Startnummer gibt es einen `IndexError`
- `startliste.append(neu)` statt `startliste[nummer - 1] = neu` – der alte Läufer bleibt auf der Liste
- `nummer = input(...)` ohne `int` – ein Text ist kein Index (`TypeError`)
- `helfer[4]` bei vier Elementen – den Index gibt es nicht (`IndexError`), der letzte ist `len(helfer) - 1`

## Dateien in diesem Ordner

- [`Infoblatt_Arbeitsblatt_Ummeldung.pdf`](Infoblatt_Arbeitsblatt_Ummeldung.pdf) – Infoblatt (1 Seite, nur Neues) und Arbeitsblatt (Aufgabe 1 bis 3) der Stunde
- [`Übungsaufgaben/A_Ummeldung_Startnummer.py`](Übungsaufgaben/A_Ummeldung_Startnummer.py) – Aufgabe 3a: unseren PAP mit der Startnummer umsetzen
- [`Übungsaufgaben/B_Ummeldung_Name.py`](Übungsaufgaben/B_Ummeldung_Name.py) – Aufgabe 3b: derselbe PAP mit dem Namen (`index`). Die Startliste steht jeweils schon drin, Tipps ganz unten in der Datei
- [`Ergebnisse/`](Ergebnisse/) – was wir in der Stunde gemeinsam erarbeiten: die Bilder der Sicherung,
  unsere Lösung und die Projektseite
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für Ihren KI-Tutor (Stand Thema 07)

Keine Hausaufgabe zu dieser Stunde.
