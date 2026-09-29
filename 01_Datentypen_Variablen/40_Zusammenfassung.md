# Stunde 2 — Zusammenfassung

**Programmieren ET1 · 22.09.2026 · Datentypen, Variablen und Konstanten**

Zum Nachschlagen, bevor du an der Hausaufgabe sitzt.

## Die Funktionen

| Schreibweise | Was sie tut |
|---|---|
| `name = 847` | legt den Wert `847` unter dem Namen `name` ab |
| `print(a, b)` | gibt aus; das Komma setzt ein Leerzeichen dazwischen |
| `type(wert)` | sagt, welcher Typ ein Wert ist — gehört in ein `print` |
| `int("1970")` | macht aus Text eine ganze Zahl |
| `float("73.1")` | macht aus Text eine Kommazahl |
| `str(847)` | macht aus einer Zahl Text |
| `input("Frage? ")` | fragt nach einer Eingabe — das Ergebnis ist **immer Text** |
| `# ...` | Kommentar, wird nicht ausgeführt |

## Die vier Typen

| Typ | Wofür | Beispiel |
|---|---|---|
| `int` | ganze Zahlen, exakt | `startnummer = 847` |
| `float` | Kommazahlen, mit Punkt | `zielzeit = 4388.4` |
| `str` | Text, in Anführungszeichen | `nachname = "Schneider"` |
| `bool` | wahr oder falsch | `im_ziel = True` |

## Das Wichtigste

- **Eine Variable ist ein Name für einen Wert.** Der Wert darf wechseln, der Name bleibt.
- **Anführungszeichen machen Text.** `1970` ist eine Zahl, `"1970"` sind vier Zeichen. Mit Text
  kann man nicht rechnen — `"847" + 1` ist ein Fehler.
- **Der Typ hängt am Wert, nicht am Namen.** Nachsehen jederzeit mit `type()`.
- **Eingaben sind Text.** Wer damit rechnen will, wandelt vorher um: `int(...)` oder `float(...)`.
- **Konstanten schreibt man GROSS**: `LAUFJAHR = 2027`. Python hindert niemanden daran, sie zu
  ändern — die Großbuchstaben sind eine Absprache unter Menschen.
- **Kommazahlen sind Näherungen.** `0.1 + 0.2` ergibt nicht genau `0.3`. Deshalb Zeiten nie mit
  `==` auf Gleichheit prüfen.
- **Bei einer Fehlermeldung die letzte Zeile lesen.** Dort steht, was Python stört. Dann **eine**
  Sache ändern und noch einmal ausführen.

## Wo wir stehen

Ein Läufer steht im Programm als Datensatz, jedes Feld im richtigen Typ. Am 29.09. rechnen wir
zum ersten Mal damit: aus 4 388 Sekunden wird die Nettozeit `73:08`.
