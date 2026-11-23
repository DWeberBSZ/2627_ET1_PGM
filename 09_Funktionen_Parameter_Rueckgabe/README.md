# 09 – Funktionen: Parameter und Rückgabewert

*Zuletzt aktualisiert: 24.11.2026 – Unterricht vom 24.11.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 9. Dazu das
[Infoblatt mit Arbeitsblatt](Infoblatt_Arbeitsblatt_Parameter_return.pdf).

**Leitsatz: Eine Funktion – unterschiedliche Werte hinein, ein Ergebnis zurück.**

## Lernziele

- Begründen, warum eine Funktion Parameter braucht, wenn sie mit unterschiedlichen Werten arbeiten soll
- Parameter (Namen in der Funktion) und Werte im Aufruf unterscheiden und einander zuordnen
- Mit `return` einen Wert zurückgeben und ihn im Programm weiterverwenden
- Erklären, dass es die Variablen einer Funktion nur in der Funktion gibt
- Eine Funktion mit Parametern und Rückgabewert als PAP planen und programmieren: `freie_plaetze(liste, plaetze)`

## Die Lernsituation

**Wir digitalisieren den Kaminkehrerlauf.** *Unterrichtsszenario – keine Anfrage der Veranstalter.*

Wir spielen den Lauftag durch. Der Lauf ist ausgebucht: 250 Läufer. Kaminkehrer Sepp will mitlaufen – unser
Programm zeigt „Plätze übrig: 0“. Dabei hält der Verein 30 Plätze für Kaminkehrer frei. Unser Programm kennt
aber nur eine Liste.

Unser Ziel: Das Programm zeigt die freien Plätze für Kaminkehrer und für Läufer – berechnet von einer einzigen
Funktion. Dafür brauchen wir zwei Dinge:

1. Werte hinein: Parameter.
2. Ergebnis heraus: `return`.

## So läuft die Stunde

1. **Infoblatt** lesen (Einzelarbeit).
2. **Aufgabe 1 – Die Funktion benutzen** (Partnerarbeit mit dem Banknachbarn): im Programm die Lücken ergänzen
   (die Rechnung in der Funktion, `return`, die Werte in den Aufrufen) und die Ausgabe vorhersagen.
   Gesichert wird an der Tafel.
3. **Aufgabe 2 – Unser Ablauf als PAP** (Partnerarbeit): unser Programm und die Funktion als PAP planen.
   Gesichert wird an der Tafel.
4. **Aufgabe 3 – Freie Plätze für beide Listen** (Einzelarbeit,
   [`A_Freie_Plaetze.py`](Übungsaufgaben/A_Freie_Plaetze.py)): umsetzen – a) die Funktion, b) das Programm nach dem
   eigenen PAP.
5. **Übungsphase:** Aufgabe 3 fertigstellen, dann [`Ü1_Startgeld.py`](Übungsaufgaben/Ü1_Startgeld.py)
   und [`Ü2_Bestzeit.py`](Übungsaufgaben/Ü2_Bestzeit.py).

## Parameter: Werte hinein

Wie weit ist es noch bis ins Ziel? Sofia läuft 10 km und ist bei km 4. Emil läuft 5 km und ist bei km 3.

```python
def reststrecke(strecke, gelaufen):
    rest = strecke - gelaufen
    return rest

rest_sofia = reststrecke(10, 4)
print("Sofia hat noch", rest_sofia, "km")
rest_emil = reststrecke(5, 3)
print("Emil hat noch", rest_emil, "km")
```

- `strecke, gelaufen` – die **Parameter**: Namen für die Werte, die die Funktion braucht.
- `reststrecke(10, 4)` – der Aufruf mit den **Werten**. Der erste Wert landet im ersten Parameter
  (`strecke` ist 10), der zweite im zweiten (`gelaufen` ist 4).
- In der Funktion rechnet man mit den Namen.

## Rückgabewert: Ergebnis heraus

- `return rest` gibt einen Wert zurück – den **Rückgabewert**.
- `return` beendet die Funktion.
- Der Aufruf steht für diesen Wert. Das Programm merkt ihn sich in einer Variablen:
  `rest_sofia = reststrecke(10, 4)` – danach ist `rest_sofia` 6.

## Warum so?

Variablen einer Funktion gibt es **nur in der Funktion**: `rest` kennt das Programm draußen nicht.
Deshalb gehen Werte über **Parameter** hinein und das Ergebnis kommt über **`return`** heraus.
So rechnet eine einzige Funktion für Sofia und für Emil – mit anderen Werten.

## Im PAP

Im Aufruf-Symbol (Kasten mit doppeltem Rand) stehen die Werte: `reststrecke(10, 4)`.
Der PAP der Funktion beginnt mit ihrem Namen und den Parametern und endet mit der Rückgabe.

## Typische Fehler

- `return` vergessen – die Funktion gibt `None` zurück, in der Ausgabe steht `None`
- `print` statt `return` in der Funktion – das Programm kann mit dem Ergebnis nicht weiterarbeiten
- In der Funktion steht der Name einer bestimmten Liste statt des Parameters – sie rechnet dann nur für diese Liste
- Werte im Aufruf vertauscht – die Reihenfolge muss zur Reihenfolge der Parameter passen
- Zu wenige oder zu viele Werte im Aufruf – `TypeError: ... missing 1 required positional argument`
- Das Ergebnis nicht gemerkt: `freie_plaetze(kaminkehrer, 30)` ohne Variable davor – der Wert geht verloren
- Eine Variable der Funktion im Programm verwenden – `NameError`

## Dateien in diesem Ordner

- [`Infoblatt_Arbeitsblatt_Parameter_return.pdf`](Infoblatt_Arbeitsblatt_Parameter_return.pdf) – Infoblatt und Arbeitsblatt (Aufgabe 1 bis 3) der Stunde
- [`Übungsaufgaben/A_Freie_Plaetze.py`](Übungsaufgaben/A_Freie_Plaetze.py) – Aufgabe 3a und 3b: die beiden Listen
  stehen schon drin; Tipps ganz unten in der Datei
- [`Übungsaufgaben/Ü1_Startgeld.py`](Übungsaufgaben/Ü1_Startgeld.py) – eine Funktion mit zwei Parametern, mit dem
  Ergebnis weiterrechnen
- [`Übungsaufgaben/Ü2_Bestzeit.py`](Übungsaufgaben/Ü2_Bestzeit.py) – die Funktion vom 17.11. bekommt einen
  Parameter und gibt die Zeit zurück
- [`Ergebnisse/`](Ergebnisse/) – was wir in der Stunde gemeinsam erarbeiten
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für Ihren KI-Tutor (Stand Thema 09)

Keine Hausaufgabe zu dieser Stunde.
