# Übungsblatt 02 — Die Felder der Urkunde

**Programmieren ET1 · 22.09.2026**
**Lernsituation:** Neumarkter Stadtlauf — Auftrag 2

> Auf der alten Urkunde stehen sechs Angaben, von Hand eingetragen. Damit ein Programm sie
> drucken kann, muss es sie erst einmal **halten** können. Heute bringen wir die Angaben in eine
> Form, mit der sich arbeiten lässt.

Arbeite die Aufgaben der Reihe nach durch. **A** musst du schaffen, **B** solltest du schaffen,
**C** ist für alle, die schneller sind.

Speichere jede Aufgabe als eigene Datei.

Starten wie letzte Woche: Konsole im Ordner öffnen, `python a1_felder.py`.

---

## A — Pflicht

### A1 Was steht da eigentlich?

Lege `a1_felder.py` an. Die folgenden fünf Angaben stammen aus der Meldeliste des Laufs.
Schreibe für jede eine Variable mit sprechendem Namen und gib Wert **und** Typ aus:

`847` · `"Schneider"` · `1970` · `4388.4` · `True`

```
Beispielausgabe:
847 <class 'int'>
Schneider <class 'str'>
1970 <class 'int'>
4388.4 <class 'float'>
True <class 'bool'>
```

**Frage zum Mitschreiben:** Welche dieser fünf Angaben steht auf der Urkunde, welche nicht?

### A2 Dein eigener Startdatensatz

Lege `a2_startdatensatz.py` an. Trage dich selbst als Teilnehmer ein:

- Startnummer — such dir eine zwischen 100 und 1 999 aus
- Vorname und Nachname
- Geburtsjahr
- Geschlecht — `"W"` oder `"M"`
- Strecke — `"5km"`, `"10km"` oder `"HM"` (Halbmarathon)

Gib den Datensatz sauber untereinander aus.

**Heb die Datei auf.** Diese sechs Zeilen sind der Anfang von allem, was bis Weihnachten folgt.

### A3 Wie alt ist der Läufer?

Erweitere `a2_startdatensatz.py`:

1. Lege ganz oben eine **Konstante** `LAUFJAHR = 2027` an.
2. Berechne daraus dein Alter am Wettkampftag.
3. Gib es mit aus.

Dann die Kontrollfrage, als Kommentar in der Datei: *Warum steht die Jahreszahl oben als
Konstante und nicht einfach in der Rechnung?* Ein Satz genügt.

### A4 Vier Fehler in der Meldeliste

> **Erst A3 fertig machen, dann aufklappen.** Der Code unten verrät, wie man das Alter über eine
> Konstante ausrechnet — wer ihn vorher liest, hat A3 nicht selbst gelöst.

<details>
<summary><b>A4 aufklappen</b> — erst nach A3!</summary>

Das Programm unten soll das Alter und die Zielzeit einer Läuferin ausgeben. Es tut es nicht.
Kopiere es als `a4_reparatur.py` und bring es zum Laufen. Es sind **vier** Fehler — und einer
davon erzeugt selbst **keine** Fehlermeldung, er fällt erst eine Zeile später auf.

```python
LAUFJAHR = "2027"
geburtsjahr = 1970
alter = LAUFJAHR - geburtsjahr
print("Alter: " + alter)

zielzeit = 73,1
print("Zielzeit in Minuten: " + zielzeit)
```

Schreibe zu jedem Fehler einen Kommentar: **was** war falsch und **woran** hast du es gemerkt.

</details>

---

## B — Vertiefung

### B1 Die Meldeliste kommt als Text

So kommen die Daten aus dem Anmeldesystem — alles ist Text, auch die Zahlen:

```python
startnummer = "847"
geburtsjahr = "1970"
zielzeit    = "4388.4"
```

Lege `b1_umwandeln.py` an und mache daraus rechenbare Werte. Gib anschließend aus:

- das Alter am Wettkampftag
- die Zielzeit in **Minuten** (eine Kommazahl)
- die Startnummer plus 1 — nur als Beweis, dass es jetzt eine Zahl ist

Gib zu jedem Wert den Typ mit aus, vorher und nachher.

**Zusatz:** Lass das Geburtsjahr statt aus dem Text mit `input()` eintippen. Was musst du ändern?

---

## C — Zusatz

### C1 Was kommt heraus?

Schreibe **erst auf Papier** hin, was jede Zeile ausgibt und welchen Typ das Ergebnis hat.
Erst danach tippen und prüfen.

```python
print("847" + "1")
print(847 + 1)
print(4388 / 60)
print(4388 // 60)
print(int("1970") + 1)
print(str(847) + " Schneider")
print(2027 - 1970 > 40)
```

Wo du falsch lagst: ein Satz, warum. (`//` ist neu — rate einfach, nächste Woche kommt es dran.)

### C2 Namen aufräumen

Hier ist die Meldezeile einer Läuferin, geschrieben von jemandem, der es eilig hatte:

```python
a = 847
b = "Schneider"
c = 1970
d = 4388.4
e = 2027 - c
```

Schreib das Ganze als `c2_namen.py` neu, mit Namen, die sagen, was drinsteht. Ändere nichts an
der Rechnung. Vergleiche die beiden Fassungen.

---

## Checkliste

Bevor du schließt:

- [ ] A1 bis A4 laufen ohne Fehlermeldung
- [ ] In A2 steht dein eigener Datensatz mit allen sechs Feldern
- [ ] In A3 steht die Konstante ganz oben und in Großbuchstaben
- [ ] In A4 steht zu jedem der vier Fehler ein Kommentar
- [ ] Alle Dateien sind gespeichert.

**Was heute an die Wand kommt:** Überlege dir die wichtigsten Learnings aus dieser Stunde.
