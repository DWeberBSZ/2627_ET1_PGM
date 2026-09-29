# 01 – Datentypen, Variablen und Konstanten

*Zuletzt aktualisiert: 29.09.2026*

Nachschlagewerk zu diesem Thema (Unterricht vom 22.09.2026). Übungen: [`20_Uebungsblatt.md`](20_Uebungsblatt.md), kurze Zusammenfassung: [`40_Zusammenfassung.md`](40_Zusammenfassung.md).

## Lernziele

- Werte unter einem Namen ablegen (Variablen) und wieder ausgeben
- Die vier Datentypen `int`, `float`, `str` und `bool` unterscheiden
- Den Typ eines Werts mit `type()` bestimmen
- Werte umwandeln: Text in Zahl und Zahl in Text
- Konstanten erkennen und selbst anlegen
- Eine Fehlermeldung lesen (die letzte Zeile)

## Variablen

Eine Variable ist ein **Name für einen Wert**. Mit `=` wird der Wert abgelegt.

```python
startnummer = 847
nachname = "Schneider"
print("Startnummer:", startnummer)   # Startnummer: 847
```

Im `print` trennt ein **Komma** die Teile und setzt ein Leerzeichen dazwischen.

## Die vier Datentypen

| Typ | Wofür | Beispiel |
|---|---|---|
| `int` | ganze Zahlen | `startnummer = 847` |
| `float` | Kommazahlen (mit Punkt!) | `zielzeit = 4388.4` |
| `str` | Text, in Anführungszeichen | `nachname = "Schneider"` |
| `bool` | wahr oder falsch | `im_ziel = True` |

```python
print(type(847))       # <class 'int'>
print(type("847"))     # <class 'str'>  – Anführungszeichen machen Text!
```

## Umwandeln

```python
jahrgang = int("1970")       # Text -> ganze Zahl
zeit = float("73.1")         # Text -> Kommazahl
text = str(847)              # Zahl -> Text
```

`input()` liefert **immer Text** – wer damit rechnen will, wandelt vorher um:

```python
jahrgang = int(input("Jahrgang? "))
```

## Konstanten

Werte, die sich im Programm nicht ändern sollen, schreibt man **GROSS** und ganz oben hin:

```python
LAUFJAHR = 2027
alter = LAUFJAHR - jahrgang
```

## Fehlermeldungen lesen

```python
startnummer = "847"
print(startnummer + 1)
# TypeError: can only concatenate str (not "int") to str
```

**Die letzte Zeile lesen.** Steht dort `str` und `int`, hat eine Zahl Anführungszeichen – oder Text wird mit `+` an eine Zahl gehängt.

## Dateien in diesem Ordner

- [`20_Uebungsblatt.md`](20_Uebungsblatt.md) – Übungsblatt der Stunde
- [`40_Zusammenfassung.md`](40_Zusammenfassung.md) – das Wichtigste auf einer Seite
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für deinen KI-Tutor (Stand Thema 01)
