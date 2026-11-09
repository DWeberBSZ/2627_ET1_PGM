# 06 – Listen: die Startliste

*Zuletzt aktualisiert: 10.11.2026 – Unterricht vom 10.11.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 7.1 und 7.2 (1. Aufl. S. 112–117) und
Kap. 8.3 „Schleifen über Listen“ (S. 141). Dazu das
[Infoblatt mit Arbeitsblatt](Infoblatt_Arbeitsblatt_Listen.pdf).

## Lernziele

- Den Bausteinen eines PAP den passenden Python-Befehl zuordnen (Liste anlegen, `input`, `append`, `in`,
  `len`, Index, `print`)
- Den Ablauf der Startliste als PAP planen – und begründen, warum die Liste vor der Schleife angelegt
  und vor dem Anhängen geprüft wird
- Alle Anmeldungen in einer Liste speichern und die Startliste mit Startnummern ausgeben
- Doppelte Anmeldungen mit `in` abweisen und Startnummern ohne Lücke vergeben

## Die Lernsituation

**Wir digitalisieren den Kaminkehrerlauf.** *Unterrichtsszenario – keine Anfrage der Veranstalter.*
Unsere Anmeldung vom 27.10. meldet beliebig viele Läufer an – danach kennt sie aber nur noch den
letzten Namen. Petra Ostermeier hat sich zweimal angemeldet und hält jetzt zwei Startnummern in der
Hand. Der Veranstalter will die **Startliste**, und jeder darf nur einmal drauf. Heute merkt sich unser
Programm alle Anmeldungen in einer Liste und weist doppelte ab.

## So läuft die Stunde

1. **Infoblatt** lesen (Einzelarbeit).
2. **Aufgabe 1 – Vom PAP zu Python** (Partnerarbeit mit dem Banknachbarn): Welcher Python-Befehl
   setzt den PAP-Baustein um? Gesichert wird an der Tafel-App.
3. **Aufgabe 2 – Unser Ablauf als PAP** (Partnerarbeit, Partnerkarten): Das Programm liest
   nacheinander Namen ein, bis „ende“ eingegeben wird. Jeder neue Name kommt in die Startliste und
   bekommt seine Startnummer, ein doppelter wird abgewiesen. Am Ende gibt es die Anzahl der
   Teilnehmer und die Startliste aus. **PAP = Programm am Papier** – erst planen, dann programmieren.
   Gesichert wird an der Tafel mit den Applikationen.
4. **Aufgabe 3 – Die Startliste** (Einzelarbeit): Erweitern Sie Ihre Anmeldung. Nutzen Sie ggf. die
   fertige Anmeldung in [`A_Startliste.py`](Übungsaufgaben/A_Startliste.py). Setzen Sie das Programm aus
   dem PAP um.

## Variable oder Liste?

Eine **Variable** merkt sich **einen** Wert. Eine **Liste** merkt sich **viele** Werte unter einem
Namen – in der Reihenfolge, in der sie dazukommen.

```python
person = "Cem"                       # Variable: ein Wert
helfer = ["Anna", "Ben", "Cem"]      # Liste: viele Werte
```

## Eine Liste anlegen

```python
helfer = []                          # leer – die Werte kommen erst im Programm dazu
helfer = ["Anna", "Ben", "Cem"]      # mit Werten, durch Komma getrennt
```

## Ein Element holen

Jedes Element hat eine Platznummer, den **Index**. Er beginnt bei **0**.

```python
helfer[0]      # "Anna"
helfer[1]      # "Ben"
helfer[-1]     # "Cem" – der letzte Eintrag
```

## Anhängen, zählen, prüfen, ausgeben

```python
helfer.append("Dana")    # hängt genau einen Wert hinten an
len(helfer)              # 4 – zählt die Elemente
"Ben" in helfer          # True
"Emil" in helfer         # False
print(helfer)            # ['Anna', 'Ben', 'Cem', 'Dana'] – die ganze Liste mit Klammern
```

`in` liefert `True` oder `False` – das kann ein `if` nutzen:

```python
if "Ben" in helfer:
    print("Ben ist schon dabei.")
```

## Der PAP

Die Symbole wie im PAP-Designer (wie bei Frau Weber):

| Symbol | Bedeutung | Beispiel |
|---|---|---|
| Oval | Start / Ende | Start |
| Rechteck | Operation | Leere Liste startliste anlegen |
| Parallelogramm mit E | Eingabe | Eingabe von name |
| Parallelogramm mit A | Ausgabe | Ausgabe der Startliste |
| Raute | Verzweigung (ja/nein) | name schon in startliste? |
| Sechseck oben | Schleifenanfang | Solange name ungleich "ende" |
| Sechseck unten | Schleifenende | |

**Schleifen im PAP:** Der PAP bietet zwei Möglichkeiten, eine Schleife zu zeichnen – **beide sind
richtig.** Entweder eine Raute mit Rücksprung (wie am 27.10.) oder Schleifenanfang und Schleifenende.
In Python wird aus beiden dieselbe `while`-Schleife:

```python
name = input("Name: ")
while name != "ende":
    helfer.append(name)
    name = input("Name: ")
print(helfer)
```

## Für die Übungen

Die Liste **vor** der Schleife anlegen, **in** der Schleife füllen, **nach** der Schleife auswerten.
Steht `werte = []` **in** der Schleife, ist die Liste bei jedem Durchlauf wieder leer.

```python
for person in helfer:        # die Liste Element für Element durchlaufen
    print(person)

helfer.index("Cem")          # 2 – an welchem Platz steht der Wert? Platz = Index + 1
```

## Typische Fehler

- Liste **in** der Schleife angelegt – am Ende steht nur der letzte Wert drin
- `liste = name` statt `liste.append(name)` – die Liste ist weg
- `liste = liste.append(name)` – `append` liefert nichts, danach ist `liste` gleich `None`
- Erst angehängt, dann mit `in` geprüft – dann ist jeder Name „schon drin“
- Startnummer zählt auch bei doppelten weiter – die Startnummern haben eine Lücke
- `liste[len(liste)]` – den Index gibt es nicht (`IndexError`), der letzte ist `len(liste) - 1`

## Dateien in diesem Ordner

- [`Infoblatt_Arbeitsblatt_Listen.pdf`](Infoblatt_Arbeitsblatt_Listen.pdf) – Infoblatt (2 Seiten) und Arbeitsblatt (Aufgabe 1 bis 3) der Stunde
- `Übungsaufgaben/` – A_ in der Stunde (Aufgabe 3); Ü1–Ü3 sind Übung **und** Hausaufgabe: in der Übungsphase anfangen, was nicht fertig wird, zu Hause – **fertig bis Dienstag, 17.11.** (zusammen etwa 60–90 Minuten). Tipps jeweils ganz unten in der Datei
  - [`A_Startliste.py`](Übungsaufgaben/A_Startliste.py) – Aufgabe 3: unseren PAP umsetzen, mit dem Anmeldeprogramm als Ausgangspunkt
  - [`Ü1_Die_Spendenliste.py`](Übungsaufgaben/Ü1_Die_Spendenliste.py) – Spenden in einer Liste sammeln, Anzahl und Summe (ca. 20 min)
  - [`Ü2_Die_Zielzeiten.py`](Übungsaufgaben/Ü2_Die_Zielzeiten.py) – schnellste Zeit und ihre Startnummer, ohne `min()` (ca. 25 min)
  - [`Ü3_Der_Akkutest.py`](Übungsaufgaben/Ü3_Der_Akkutest.py) – Messwerte speichern, Durchschnitt, zu schwache Zellen melden (ca. 35 min)
- [`Ergebnisse/`](Ergebnisse/) – was wir in der Stunde gemeinsam erarbeiten: die Bilder der Sicherung,
  unsere Lösung und die Projektseite
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für Ihren KI-Tutor (Stand Thema 06)
