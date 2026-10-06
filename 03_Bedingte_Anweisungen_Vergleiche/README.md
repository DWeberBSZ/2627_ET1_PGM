# 03 – Bedingte Anweisungen und Vergleichsausdrücke

*Zuletzt aktualisiert: 06.10.2026, 15:38 Uhr*

Nachschlagewerk zu diesem Thema (Unterricht vom 06.10.2026). Fachbuch: Kapitel 8.1 „if-Verzweigung“.

## Lernziele

- Den Programmablauf mit `if`, `elif` und `else` steuern
- Einen Anweisungsblock richtig einrücken
- Mit `isinstance()` den Datentyp einer Variable prüfen
- Werte mit Vergleichsoperatoren (`>`, `>=`, `<`, `<=`, `==`, `!=`) vergleichen
- Eine Bedingung mit `not` umkehren
- Einen Programmablaufplan (PAP) in Python-Code übersetzen

## Die if-Anweisung

Mit bedingten Anweisungen wird der **Programmablauf** gesteuert: Das Programm führt bestimmte Anweisungen nur aus, wenn eine **Bedingung** erfüllt ist.

```python
if BEDINGUNG:          # Doppelpunkt nicht vergessen!
    Anweisung 1        # mit TAB einrücken
    Anweisung 2        # alle eingerückten Zeilen = ANWEISUNGSBLOCK
else:                  # der else-Zweig ist optional
    Anweisung 1
    Anweisung 2
```

**Wichtig:** Die Bedingung muss sich zu `True` oder `False` auswerten lassen. Das geht mit

- `True`, `False` oder einer Variable vom Datentyp `bool`
- einem Vergleichsausdruck (siehe unten)

## Den Datentyp prüfen mit `isinstance()`

`isinstance()` fragt: „Ist die Variable von diesem Datentyp?“ – und liefert `True` oder `False`.

```python
a = 5.4
print(isinstance(a, int))     # False
print(isinstance(a, float))   # True
```

Das Ergebnis ist selbst ein `bool` und eignet sich deshalb direkt als Bedingung:

```python
a = 5.4
ist_int = isinstance(a, int)

if ist_int:
    print("Die Variable ist vom Datentyp Integer")
else:
    print("Die Variable ist kein Integer")
```

Die Typnamen für `isinstance()`: `int`, `float`, `bool`, `str`.

## Mehrere Fälle: verschachteln oder `elif`

Sollen mehr als zwei Fälle unterschieden werden, gibt es zwei Möglichkeiten.

**Verschachtelt** – im `else`-Zweig steht eine weitere `if`-Anweisung (jede Ebene eine Einrückung tiefer):

```python
if isinstance(a, bool):
    print("Die Variable ist vom Typ Bool.")
else:
    if isinstance(a, float):
        print("Die Variable ist vom Typ Float.")
    else:
        ...
```

**Mit `elif`** („else if“) – gleicher Ablauf, aber übersichtlicher, weil alles auf einer Ebene bleibt:

```python
if isinstance(a, bool):
    print("Die Variable ist vom Typ Bool.")
elif isinstance(a, float):
    print("Die Variable ist vom Typ Float.")
elif isinstance(a, int):
    print("Die Variable ist vom Typ Integer.")
elif isinstance(a, str):
    print("Die Variable ist vom Typ String.")
```

Python prüft die Bedingungen von oben nach unten. Sobald **eine** zutrifft, wird ihr Block ausgeführt – alle weiteren werden übersprungen.

**Achtung, Reihenfolge:** In Python zählt ein `bool` auch als `int` – `isinstance(True, int)` liefert `True`. Deshalb wird im PAP zuerst auf `bool` geprüft und erst danach auf `int`.

## Vergleichsausdrücke

Vergleichsausdrücke werden häufig zusammen mit bedingten Anweisungen verwendet. Ihr Ergebnis ist immer `True` oder `False`.

| Operator | Bedeutung            | Achtung                     |
|----------|----------------------|-----------------------------|
| `>`      | größer               |                             |
| `>=`     | größer oder gleich   | `=>` gibt es **nicht**      |
| `<`      | kleiner              |                             |
| `<=`     | kleiner oder gleich  | `=<` gibt es **nicht**      |
| `==`     | ist gleich           | **nicht** `=` (Zuweisung!)  |
| `!=`     | ist ungleich         |                             |

```python
alter_sus_1 = 22
alter_sus_2 = 22
alter_sus_3 = 20

if alter_sus_1 >= alter_sus_2:
    print("SuS1 ist älter oder gleich alt wie SuS2")

if alter_sus_1 == alter_sus_3:
    print("SuS1 ist genauso alt wie SuS3")

if alter_sus_2 != alter_sus_3:
    print("SuS2 ist nicht so alt wie SuS3")
```

Mehrere `if`-Anweisungen untereinander (ohne `elif`) sind **unabhängige** Abfragen: Jede wird für sich geprüft, es können also mehrere Ausgaben erscheinen.

## Bedingung umkehren mit `not`

`not` macht aus `True` ein `False` und umgekehrt:

```python
if not(alter_sus_2 != alter_sus_3):
    print("SuS2 und SuS3 sind gleich alt (nicht ungleich)")
```

`if True:` wird übrigens **immer** ausgeführt.

## Programmablaufplan (PAP)

Ein PAP zeigt den Ablauf eines Programms als Grafik, bevor man ihn programmiert:

- **Abgerundetes Feld:** Start / Ende
- **Rechteck:** Anweisung (z. B. Variable anlegen)
- **Raute:** Bedingung mit den Ausgängen *ja* / *nein* → wird zu `if` / `else` bzw. `elif`
- **Parallelogramm:** Ausgabe → wird zu `print()`

Beispiel: [`Übungsaufgaben/A0_Datentyp_PAP_Angabe.png`](Übungsaufgaben/A0_Datentyp_PAP_Angabe.png). Ein Alltagsbeispiel mit Augenzwinkern: [`Algorithmus_Bier.jpg`](Algorithmus_Bier.jpg).

## Typische Fehler

- Doppelpunkt nach `if …`, `elif …` oder `else` vergessen
- Anweisungsblock nicht eingerückt
- `=` statt `==` beim Vergleichen
- `=>` oder `=<` statt `>=` bzw. `<=`
- Bei der Typprüfung `int` vor `bool` abgefragt

## Dateien in diesem Ordner

- [`0_Bedingte Anweisungen.py`](0_Bedingte%20Anweisungen.py) – if/else und `isinstance()`
- [`1_Vergleichsausdrücke.py`](1_Vergleichsausdrücke.py) – Vergleichsoperatoren und `not`
- [`Algorithmus_Bier.jpg`](Algorithmus_Bier.jpg) – Ablaufdiagramm aus dem Alltag
- `Übungsaufgaben/`
  - [`A0_Datentyp.py`](Übungsaufgaben/A0_Datentyp.py) – Aufgabe: Datentyp erkennen (mit PAP als [`.png`](Übungsaufgaben/A0_Datentyp_PAP_Angabe.png) und [`.pap`](Übungsaufgaben/A0_Datentyp.pap))
  - [`A0_Datentyp_LSG_1.py`](Übungsaufgaben/A0_Datentyp_LSG_1.py) – Lösung mit verschachtelten if/else
  - [`A0_Datentyp_LSG_2.py`](Übungsaufgaben/A0_Datentyp_LSG_2.py) – Lösung mit `elif`
  - [`A1_Maximum.py`](Übungsaufgaben/A1_Maximum.py) – Aufgabe: Maximum von drei Zahlen
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für deinen KI-Tutor (Stand Thema 03)
