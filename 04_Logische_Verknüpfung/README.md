# 04 – Logische Operatoren: Paket-Zuordnung (AP1)

*Zuletzt aktualisiert: 19.10.2026 – für den Unterricht vom 20.10.2026*

Nachschlagewerk zu diesem Thema. Fachbuch: Kofler, Kap. 3.2 „Binäre versus logische Operatoren“
und „Operatorhierarchie“, S. 68–70 (1. Auflage); `if`-Verzweigung in Kap. 8.1.

## Lernziele

- Eine Technische Beschreibung lesen und daraus Anforderungen und Testfälle entnehmen
- Bedingungen mit `and` und `or` verknüpfen und mit `not` umkehren
- Das Ergebnis einer verknüpften Bedingung mit einer Wahrheitstabelle vorhersagen
- Die Rangfolge `not` – `and` – `or` kennen und Klammern gezielt setzen
- Mehrere Regeln in die richtige Reihenfolge bringen (verschachtelt oder als `elif`-Kette)
- Ein Programm systematisch mit vorgegebenen Testfällen prüfen

## Die Lernsituation

Die CodeSolutions Neumarkt GmbH entwickelt für einen Kunden die Software für ein Lagersystem:
Jedes Paket wird anhand seiner **Paketnummer** einem von vier Fächern zugeordnet. Grundlage ist die
[Technische Beschreibung](Lernsituationen/Technische%20Beschreibung%20Paketzuordnung.pdf) – dort
stehen Software-Architektur (EVA-Prinzip), die Zuordnungsregeln, die Arbeitsinhalte und die
**Testfälle**. Das Projekt hat drei Arbeitspakete:

1. **AP1** – einmalige Zuordnung eines Pakets (heute)
2. **AP2** – kontinuierliche Zuordnung, bis die Paketnummer 0 eingegeben wird
3. **AP3** – Paketnummern aus einer Textdatei einlesen

Zum Start gibt es ein [Funktionsmuster](Lernsituationen/Funktionsmuster.py) aus dem
Kundenworkshop: Es liest eine Paketnummer ein, ordnet aber noch nichts zu.

## Logische Operatoren

Mit `and` und `or` werden zwei Bedingungen zu **einer** verknüpft. Das Ergebnis ist wieder
`True` oder `False`.

| Bedingung A | Bedingung B | `A and B` | `A or B` |
|---|---|---|---|
| `False` | `False` | `False` | `False` |
| `False` | `True` | `False` | `True` |
| `True` | `False` | `False` | `True` |
| `True` | `True` | `True` | `True` |

- **`and`** – nur wahr, wenn **beide** Bedingungen wahr sind.
- **`or`** – wahr, wenn **mindestens eine** Bedingung wahr ist (auch wenn beide wahr sind).
- **`not`** – kehrt eine Bedingung um (kennst du aus Thema 03).

```python
a = 15

if a > 10 and a < 20:
    print("a liegt zwischen 10 und 20")

zahl = 10

if zahl % 4 == 0 or zahl % 5 == 0:
    print("restlos durch 4 oder durch 5 teilbar")
```

**Jede Seite braucht einen vollständigen Vergleich.** `zahl % 4 == 0 or zahl % 5 == 0` ist richtig,
`zahl % 4 or 5 == 0` ist zwar erlaubt, prüft aber etwas ganz anderes.

### Rangfolge und Klammern

Wie „Punkt vor Strich“ gilt hier: **`not` vor `and` vor `or`**. Diese beiden Zeilen sind also
**nicht** dasselbe:

```python
a or b and c       # wird gelesen als:  a or (b and c)
(a or b) and c     # erst or, dann and
```

Faustregel: Sobald `and` und `or` in einer Bedingung vorkommen, Klammern setzen – dann ist es für
jeden lesbar.

### Kurzschluss-Auswertung

Python hört auf zu prüfen, sobald das Ergebnis feststeht: Bei `and` nach dem ersten `False`, bei
`or` nach dem ersten `True`. Beispiel aus dem Buch: In `b != 0 and a / b > 3` wird gar nicht erst
geteilt, wenn `b` null ist.

## Mehrere Regeln: Die Reihenfolge entscheidet

Gelten mehrere Regeln, die sich **überschneiden**, kommt es auf die Reihenfolge an. In einer
`elif`-Kette gewinnt die **erste** Bedingung, die zutrifft – alle weiteren werden übersprungen.

Ein Beispiel ohne Pakete – eine Temperaturüberwachung:

```python
temperatur = 95

# FALSCH: 95 ist auch > 60 – die Abschaltung wird nie erreicht
if temperatur > 60:
    print("Warnung")
elif temperatur > 90:
    print("Abschaltung")

# RICHTIG: die strengste Bedingung zuerst
if temperatur > 90:
    print("Abschaltung")
elif temperatur > 60:
    print("Warnung")
```

Es gibt zwei Wege, das sauber zu lösen:

- **Strengste Bedingung zuerst** (wie oben), oder
- jede Bedingung **vollständig** hinschreiben (z. B. `temperatur > 60 and temperatur <= 90`), dann
  überschneiden sich die Fälle nicht mehr.

Wo eine Regel nur gilt, wenn eine andere **schon** zutrifft („zusätzlich“), kann man auch
**verschachteln**: die zweite `if`-Anweisung steht dann eingerückt im Block der ersten.

## Testen mit Testfällen

Die Technische Beschreibung legt für AP1 acht **Testfälle** fest (Eingabe → erwartetes Fach). Ein
Programm ist erst fertig, wenn **alle** Testfälle stimmen – nicht schon, wenn es ohne
Fehlermeldung läuft. Am besten schon während der Entwicklung immer wieder testen.

## Typische Fehler

- `=` statt `==` im Vergleich
- `zahl % 4 or 5 == 0` statt `zahl % 4 == 0 or zahl % 5 == 0`
- `and` und `or` verwechselt – im Zweifel die Wahrheitstabelle befragen
- `and` und `or` gemischt, ohne Klammern
- Die allgemeine Regel steht in der `elif`-Kette vor der strengeren
- Nur einen oder zwei Testfälle geprüft

## Dateien in diesem Ordner

- [`Lernsituationen/Technische Beschreibung Paketzuordnung.pdf`](Lernsituationen/Technische%20Beschreibung%20Paketzuordnung.pdf) – Regeln, Arbeitspakete und Testfälle
- [`Lernsituationen/Funktionsmuster.py`](Lernsituationen/Funktionsmuster.py) – Startpunkt aus dem Kundenworkshop
- [`20_Uebungsblatt.md`](20_Uebungsblatt.md) – Übungen nach AP1: Vorhersage, Eingabeprüfung, `elif`-Kette, Knobelaufgabe
- [`30_Hausaufgabe.md`](30_Hausaufgabe.md) – Die Pressensteuerung (Zweihandbedienung), Bonus Schaltjahr
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für deinen KI-Tutor (Stand Thema 04)
