# Hausaufgabe zum 06.10.2026 — Der Betriebsstundenzähler

**Programmieren ET1 · Abgabe:** Dienstag, 06.10., zu Stundenbeginn · **Dauer:** etwa 30 Minuten

Dieses Blatt liegt auch im git der Klasse: <https://bycs.link/pggit>

---

## Worum es geht

Heute war die Zeitmessung am Zielband dran. Dieselbe Rechnung brauchst du an jeder Anlage: Ein
**Betriebsstundenzähler** zählt Sekunden — abgelesen werden sollen Stunden, Minuten und Sekunden.
Und wenn die Anlage in dieser Zeit Teile produziert hat, will der Meister die **Taktzeit** wissen:
wie lange ein Teil im Schnitt gebraucht hat.

Der Lauf kommt hier nicht vor. Das Werkzeug ist dasselbe: `//` und `%`.

## Aufgabe

Lege `betriebsstunden.py` in `Meine Programme\03_Operatoren` an. Gegeben ist der Ausgangscode —
tippe ihn ab und baue ihn aus:

```python
SEK_PRO_STUNDE = 3600
SEK_PRO_MINUTE = 60

zaehlerstand = 26475      # Sekunden seit dem letzten Reset
stueckzahl = 350          # in dieser Zeit produzierte Teile
```

Das Programm gibt aus:

```
Laufzeit  : 7:21:15
Taktzeit  : 1:15 min/Stück
```

Vorgehen:

1. Die Stunden abtrennen — wie oft passen 3 600 Sekunden ganz in den Zählerstand?
2. Mit dem **Rest** weiterrechnen: Minuten und Sekunden, wie in A2.
3. Die Taktzeit: Zählerstand durch Stückzahl, ganzzahlig — das sind die Sekunden je Teil. Daraus
   wieder Minuten und Sekunden.
4. Beide Ausgaben mit **führender Null**, wo sie hingehört.

**Gegenprobe:** Am Ende eine Zeile, die `True` ausgeben muss — aus Stunden, Minuten und Sekunden
wieder den Zählerstand bilden und vergleichen.

## Hinweise

- Eine Stunde hat 3 600 Sekunden. Das ist eine **Konstante** und steht deshalb oben, nicht mitten
  in der Rechnung.
- Kommt bei der Taktzeit `75.6` heraus, hast du `/` statt `//` benutzt.
- Kommt eine riesige Zahl heraus, fehlt eine Klammer.
- Wer Teil 1 der Stunde nicht fertig hatte: **W1 bis W3 zuerst** — der eigene Urkundenkopf. Der
  wird am 22.12. zu deiner Urkunde.

## Bonus (freiwillig)

Der Zähler läuft weiter. Wie lange dauert es, bis der Wert die Marke von 24 Stunden überschreitet —
und was gibt dein Programm dann aus? Probier es mit `zaehlerstand = 90000` und schreib in einem
Satz auf, ob die Ausgabe noch stimmt.
