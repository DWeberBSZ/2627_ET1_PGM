# 05 – Schleifen mit for und while: die Anmeldung

*Zuletzt aktualisiert: 27.10.2026 – Unterricht vom 27.10.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 8.3 „»for«-Schleife“ (1. Aufl. S. 139–140)
und Kap. 8.4 „»while«-Schleife“ (S. 147–148). Dazu das
[Infoblatt mit Arbeitsblatt](Infoblatt_Arbeitsblatt_Schleifen.pdf).

## Lernziele

- Einen Block von Anweisungen mit einer Schleife beliebig oft ausführen
- Eine `while`-Schleife mit Bedingung schreiben und eine Endlosschleife erkennen
- Eine `for`-Schleife mit `range` schreiben und sagen, welche Werte `range` liefert
- Einen Zähler oder eine Summe richtig führen: Startwert vor der Schleife, verändern in der Schleife
- Eine Schleife durch eine Eingabe beenden
- Begründen, wann `for` und wann `while` besser passt

## Die Lernsituation

**Wir digitalisieren den Kaminkehrerlauf** – den Benefizlauf um den Wolfsberg in Mühlbach
(Lkr. Neumarkt): 5,25 km und 10,5 km, Start und Ziel am Bildungszentrum der Kaminkehrer, der Erlös
geht an krebskranke Kinder. Wir sind das Entwicklerteam. *Unterrichtsszenario – keine Anfrage der
Veranstalter.*

Das erste Stück ist die **Anmeldung**: Name und Jahrgang rein, Startnummer raus. Unser erstes
Programm konnte genau einen Läufer anmelden – am Lauftag kommen aber rund 175. Wir brauchen
Schleifen, weil wir mehrere Läufer anmelden wollen: Heute meldet unser Programm beliebig viele
Läufer nacheinander an, jeder mit seiner eigenen Startnummer.

## Die while-Schleife

```python
countdown = 3
while countdown > 0:          # Schleifenkopf mit Bedingung, Doppelpunkt!
    print(countdown)          # Schleifenrumpf: eingerückt
    countdown = countdown - 1
print("Los!")                 # nach der Schleife
```

Vor **jedem** Durchlauf wird die Bedingung geprüft. Ist sie `True`, läuft der Rumpf; ist sie
`False`, geht es nach der Schleife weiter.

**Endlosschleife:** Ändert sich im Rumpf nichts an der Bedingung, bleibt sie `True` – die Schleife
hört nie auf. Abbrechen mit **Strg + C**.

## Zählen und summieren

Ein Zähler bekommt seinen **Startwert vor** der Schleife und wird **in** der Schleife verändert.
Steht der Startwert in der Schleife, beginnt er bei jedem Durchlauf von vorn.

```python
runde = 1
while runde <= 2:
    print("Runde", runde, "von 2")
    runde = runde + 1
```

## Abbruch durch eine Eingabe

Weiß vorher niemand, wie oft die Schleife laufen soll, fragt man **am Ende** des Rumpfs, ob es
weitergeht. Ist die Antwort nicht `j` (`weitere != "j"`), wird die Bedingung `False` und die Schleife
endet:

```python
summe = 0
weitere = "j"
while weitere == "j":
    spende = int(input("Spende: "))
    summe = summe + spende
    weitere = input("Weitere Spende (j/n)? ")
print("Summe:", summe, "€")
```

## Die for-Schleife mit range

```python
for kilometer in range(1, 6):     # Schleifenvariable kilometer bekommt 1, 2, 3, 4, 5
    print("Schild:", kilometer, "km")
```

- `range(1, 6)` liefert 1, 2, 3, 4, 5 – der Stopp-Wert ist **nicht** mehr dabei.
- `range(3)` liefert 0, 1, 2.
- Die Grenze von `range` kann eine **Variable** sein, z. B. `range(1, runden + 1)`. Ihr Wert muss
  feststehen, bevor die Schleife beginnt: `for runde in range(1, runden + 1):`

## for oder while?

| | for | while |
|---|---|---|
| läuft … | eine feste Folge von Werten durch | solange die Bedingung gilt |
| Anzahl | steht fest, bevor die Schleife beginnt | darf vorher unbekannt sein |
| Zähler | die Schleifenvariable zählt von selbst | um Zähler kümmert man sich selbst |

Welche für unsere Anmeldung am Lauftag besser passt, haben wir im Unterricht verglichen.

## Typische Fehler

- Doppelpunkt nach `while …` oder `for …` vergessen
- Rumpf nicht eingerückt – oder eine Zeile zu viel eingerückt (läuft dann jedes Mal mit)
- Startwert **in** der Schleife: Die Startnummer beginnt jedes Mal wieder bei 1
- Zähler in der `while`-Schleife nicht erhöht: Endlosschleife
- `range(1, 3)` erwartet, dass die 3 dabei ist
- Abbruch durch eine Eingabe: die Eingabe nur vor der Schleife abgefragt – dann ändert sich die Bedingung nie und die Schleife läuft endlos

## Dateien in diesem Ordner

- [`Infoblatt_Arbeitsblatt_Schleifen.pdf`](Infoblatt_Arbeitsblatt_Schleifen.pdf) – Infoblatt und Arbeitsblatt der Stunde (je 2 Seiten)
- `Übungsaufgaben/` – A_ in der Stunde (Aufgabe 2); Ü1–Ü3 sind Übung **und** Hausaufgabe: in der Übungsphase anfangen, was nicht fertig wird, zu Hause – **fertig bis Dienstag, 10.11.** (zusammen etwa 60–90 Minuten). Tipps jeweils ganz unten in der Datei
  - [`A_Anmeldung_for.py`](Übungsaufgaben/A_Anmeldung_for.py) – Aufgabe 2, Gruppe for
  - [`A_Anmeldung_while.py`](Übungsaufgaben/A_Anmeldung_while.py) – Aufgabe 2, Gruppe while
  - [`Ü1_Die_andere_Schleife.py`](Übungsaufgaben/Ü1_Die_andere_Schleife.py) – dieselbe Anmeldung mit der anderen Schleife (ca. 20 min)
  - [`Ü2_Das_Spendenziel.py`](Übungsaufgaben/Ü2_Das_Spendenziel.py) – Spenden bis 1 111 €, Anzahl und Überschuss (ca. 20 min)
  - [`Ü3_Die_Messreihe.py`](Übungsaufgaben/Ü3_Die_Messreihe.py) – Messwerte auswerten, for oder while selbst wählen (ca. 35 min)
- [`Ergebnisse/`](Ergebnisse/) – was wir in der Stunde gemeinsam erarbeiten: die Bilder der
  Sicherung an der Tafel, die Lösung der Gruppe for und der Gruppe while, das Foto der Vor- und
  Nachteile und der Projektseite
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für Ihren KI-Tutor (Stand Thema 05)
