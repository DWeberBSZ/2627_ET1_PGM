# 02 – Operatoren: die Nettozeit

*Zuletzt aktualisiert: 29.09.2026*

Nachschlagewerk zu diesem Thema (Unterricht vom 29.09.2026). Übungen: [`20_Uebungsblatt.md`](20_Uebungsblatt.md), Hausaufgabe: [`30_Hausaufgabe.md`](30_Hausaufgabe.md).

## Lernziele

- `/`, `//` und `%` unterscheiden
- Eine Sekundenzahl in Minuten und Sekunden zerlegen
- Eine Zahl zweistellig ausgeben (führende Null) – nur mit Rechnen, ohne Formatierung
- Text und Zahlen mit `+` und `str()` zu einer Zeile zusammensetzen
- Die eigene Rechnung mit einer Gegenprobe prüfen

## Drei Arten zu teilen

```python
print(150 / 60)    # 2.5  – normale Division, Kommazahl
print(150 // 60)   # 2    – Ganzzahldivision: wie oft passt 60 ganz hinein?
print(150 % 60)    # 30   – Modulo: was bleibt übrig?
```

**Achtung:** `2.5` Minuten sind **nicht** 2 Minuten 50 Sekunden, sondern 2 Minuten 30 Sekunden.

## Sekunden werden Minuten und Sekunden

```python
zeit = 150
minuten = zeit // 60     # 2
sekunden = zeit % 60     # 30
```

## Eine Zeile aus Text und Zahlen

`+` hängt nur **Text an Text**. Zahlen brauchen vorher ein `str()`:

```python
print("Nettozeit: " + str(minuten) + ":" + str(sekunden))   # Nettozeit: 2:30
```

## Die führende Null

Bei 125 Sekunden kommt `2:5` heraus – auf jeder Uhr steht aber `2:05`. Die Sekunden lassen sich in Zehner- und Einerstelle zerlegen:

```python
sekunden = 5
print(sekunden // 10)    # 0  – Zehnerstelle
print(sekunden % 10)     # 5  – Einerstelle
print(str(sekunden // 10) + str(sekunden % 10))   # 05
```

## Die Gegenprobe

Rückwärts rechnen und mit `==` vergleichen. `==` fragt „ist das gleich?“ und liefert `True` oder `False`:

```python
print(minuten * 60 + sekunden == zeit)   # True
```

Die Gegenprobe beweist, dass die Rechnung stimmt – **nicht**, dass die Schreibweise stimmt.

## Punkt vor Strich

```python
print(ziel - start // 60)     # rechnet zuerst start // 60 – falsch!
print((ziel - start) // 60)   # so war es gemeint
```

## Umwandeln (Zusatzaufgabe W7)

```python
zeit_text = "4388.4"
sekunden = int(float(zeit_text))   # erst float, dann int -> 4388
print(int(4388.9))                 # 4388 – int() schneidet ab, es rundet nicht
```

## Dateien in diesem Ordner

- [`20_Uebungsblatt.md`](20_Uebungsblatt.md) – Übungsblatt der Stunde
- [`30_Hausaufgabe.md`](30_Hausaufgabe.md) – Hausaufgabe „Der Betriebsstundenzähler“
- [`KI_Tutor_Kontext.md`](KI_Tutor_Kontext.md) – Kontextdatei für deinen KI-Tutor (Stand Thema 02)
