# 00 – Einführung: Hallo

*Zuletzt aktualisiert: 15.09.2026, 17:50 Uhr*

Nachschlagewerk zu diesem Thema. Referenz zum Beispielskript [`erstesProgramm.py`](erstesProgramm.py).

## Lernziele

- Mit `print()` Werte und Berechnungen ausgeben können
- Grundlegende Rechenoperatoren in Python kennen und anwenden
- Zeichenketten (Strings) verketten und vervielfachen können
- Kommentare im Code lesen und verstehen

## Ausgabe mit `print()`

Mit `print()` wird ein Wert oder das Ergebnis einer Berechnung auf dem Ausgabekanal (der „Konsole") ausgegeben.

```python
print(5 * 5)   # Multiplikation -> 25
print(5 ** 2)  # Potenzierung   -> 25
```

## Rechnen mit Zahlen

```python
print(10 / 3)   # (normale) Komma-Division -> 3.333...
print(10 // 3)  # Ganzzahldivision (ohne Rest) -> 3
print(6 % 4)    # Modulo-Operator (Rest einer Division) -> 2
```

## Strings verknüpfen und vervielfachen

```python
print("Hallo" * 10)                        # 10x "Hallo" hintereinander ausgegeben
print("Mein Name ist Herr " + "Weber")      # Verketten von Zeichenketten mit +
print("Heute ist ein schöner Tag!")
```

## Kommentare

Mit `#` beginnt ein Kommentar. Kommentare werden von Python **nicht ausgewertet** und dienen nur der Dokumentation im Code.

```python
print(5 * 5)  # Das ist ein Kommentar
```

## Dateien in diesem Ordner

- [`erstesProgramm.py`](erstesProgramm.py) – Beispielskript mit den obigen Konzepten
