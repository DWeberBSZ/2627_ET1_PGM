# Übungsblatt 03 — Der Kopf deiner Urkunde · Die Nettozeit

**Programmieren ET1 · 29.09.2026**
**Lernsituation:** Neumarkter Stadtlauf — Auftrag 3

Heute hat zwei Hälften. **Teil 1** ist der Kopf der Urkunde: Erst wenn er bei allen läuft, darf
die Karte auf „Fertig“. **Teil 2** ist die nächste Karte: die Nettozeit.

Lege einen Ordner `Meine Programme\03_Operatoren` an und speichere jede Aufgabe als eigene Datei.
Starten wie gewohnt: Konsole im Ordner öffnen, `python w1_sofia.py`.

Unter jeder Aufgabe steht ein **Hilfe**-Kasten: was du dafür brauchst und ein Tipp. Erst selbst
probieren, dann hineinschauen.

**Im Buch nachlesen:** Kofler, Kap. 3 „Operatoren", S. 65–73 — dort stehen `//` und `%`.

Das Blatt liegt auch im git der Klasse: <https://bycs.link/pggit>

---

# Teil 1 — Der Kopf deiner Urkunde

> **Der Stand:** Die Karte „Kopf der Urkunde“ hängt wieder bei „In Arbeit“ — der Probedruck ist
> abgestürzt. Auf „Fertig“ darf sie erst, wenn der Kopf bei allen läuft.
>
> **Ziel der ersten Hälfte:** Dein Programm druckt den Kopf deiner eigenen Urkunde — so:
>
> ```
> URKUNDE – Neumarkter Stadtlauf
> Startnummer : 512
> Name        : Julia Berger
> Jahrgang    : 2003 (24 Jahre)
> Strecke     : 10km
> ```
>
> Mit deinen Daten, und das Alter rechnet das Programm selbst aus.

> **Letztes Mal alles geschafft (A1–A4 und B)?** Dann nimm den **Expressweg**: W1 überspringen,
> W2 und W3 zügig — dein Kopf mit Alter muss laufen, er ist die Grundlage für alles Weitere —,
> danach direkt **W7** und **W8**. W4 bis W6 kennst du im Wesentlichen schon.

### W1 Der Kopf von Sofias Urkunde

Der erste Kopf ist der von der Urkunde, die vorne hängt. Lege `w1_sofia.py` an und **tippe den
Anfang ab** — nicht kopieren, beim Abtippen lernen die Finger mit:

```python
startnummer = 847
name = "Sofia Schneider"
jahrgang = 1970
strecke = "10km"

print("URKUNDE – Neumarkter Stadtlauf")
print("Startnummer :", startnummer)
```

Überleg **vor** dem Start: Was wird ausgegeben? Dann ausführen. **Ergänze danach selbst** die
drei Zeilen für Name, Jahrgang und Strecke, bis der Kopf aussieht wie auf der Urkunde vorne.

Jetzt eine Änderung nach der anderen — jeweils erst überlegen, dann ausführen:

1. Setze den Jahrgang auf `2001`. Welche Zeilen der Ausgabe ändern sich, welche nicht?
2. Ergänze `zielzeit_minuten = 73.1` und gib den Wert als letzte Zeile mit aus.
3. Schreibe `startnummer = "847"` — mit Anführungszeichen — und ergänze
   `print("Nächste :", startnummer + 1)`. Was passiert, und **warum**? Als Kommentar dazuschreiben.

> **Hilfe W1**
> **Brauchst du:** `=` (Wert ablegen) · `print(...)` (ausgeben) · `#` (Kommentar)
> **Tipp:** In `print` trennt ein **Komma** die Teile — Text in Anführungszeichen, Variablen ohne.
> Bei Nummer 3: Schau auf die letzte Zeile der Fehlermeldung.

### W2 Der Kopf deiner Urkunde

Lege `w2_urkunde.py` an. Trage dich selbst als Läufer ein — jede Angabe in **eine eigene
Variable**: Startnummer (zwischen 100 und 1 999, such dir eine aus), Vorname, Nachname,
Geburtsjahr, Strecke (`"5km"`, `"10km"` oder `"HM"`).

Drucke damit den Kopf deiner Urkunde — erst einmal **ohne** das Alter.

**Heb die Datei auf.** Sie ist der Anfang von allem, was bis Weihnachten folgt.

> **Hilfe W2**
> **Brauchst du:** `=` · `print(...)`
> **Tipp:** Vorname und Nachname sind zwei Variablen — in `print` stehen sie mit Komma
> nebeneinander.

### W3 Das Alter rechnet das Programm

Erweitere `w2_urkunde.py`: Dein Programm soll dein **Alter am Wettkampftag** selbst ausrechnen
und in der Jahrgangszeile mit ausgeben — so wie im Ziel oben. Der Lauf ist **2027**. Leg diese
Jahreszahl als **Konstante** ganz oben ab.

Prüf dein Programm mit Sofia: Jahrgang 1970 muss 57 Jahre ergeben.

Dann die Kontrollfrage, als Kommentar in der Datei: *Warum steht die Jahreszahl oben als
Konstante und nicht einfach in der Rechnung?* Ein Satz genügt.

> **Hilfe W3**
> **Brauchst du:** `=` · ein Rechenzeichen · einen Namen in GROSSBUCHSTABEN für die Konstante
> **Tipp:** Wie rechnest du im Kopf aus, wie alt jemand mit Jahrgang 1970 im Jahr 2027 ist?
> Genau das schreibst du hin — nur mit Namen statt mit Zahlen. Stürzt es ab, lies die letzte
> Zeile der Meldung: Steht dort `str`, ist eine Zahl in Anführungszeichen geraten.

Vor dem Weitermachen die Checkliste:

- [ ] W1 läuft, alle drei Änderungen sind ausprobiert
- [ ] `w2_urkunde.py` druckt deinen Urkundenkopf **mit ausgerechnetem Alter**
- [ ] Die Jahreszahl steht als Konstante ganz oben, in Großbuchstaben
- [ ] Zu Änderung 3 in W1 steht ein Kommentar, **warum** es nicht geht

**Was nimmst du mit?** Zwei Sätze, für dich, nicht für die Lehrkraft: Was hast du verstanden, das
du vorher nicht wusstest? Wo bist du hängen geblieben — und wie bist du weitergekommen?

Fertig und noch Zeit? Dann W4 bis W6.

---

## Für die Schnellen — Teil 1

### W4 Welcher Typ steckt drin?

Lege `w4_typen.py` an. Gib die fünf Angaben aus der Meldeliste mit Wert **und** Typ aus:

`847` · `"Schneider"` · `1970` · `4388.4` · `True`

```
Beispielausgabe:
847 <class 'int'>
Schneider <class 'str'>
```

**Frage zum Mitschreiben:** Welche dieser fünf Angaben steht auf der Urkunde, welche nicht?

> **Hilfe W4**
> **Brauchst du:** `type(wert)` · `print(...)`
> **Tipp:** `type(...)` allein zeigt nichts an — es gehört in ein `print`.

### W5 Die Meldeliste kommt als Text

So kommen die Daten aus dem Anmeldesystem — alles ist Text, auch die Zahlen:

```python
startnummer = "847"
geburtsjahr = "1970"
```

Lege `w5_umwandeln.py` an, mache daraus rechenbare Werte und gib aus: das Alter am Wettkampftag
und die Startnummer plus 1 — nur als Beweis, dass es jetzt eine Zahl ist. Gib zu jedem Wert den
Typ vorher und nachher mit aus.

> **Hilfe W5**
> **Brauchst du:** `int(text)` · `type(wert)` · `print(...)`
> **Tipp:** `geburtsjahr = int(geburtsjahr)` schreibt den umgewandelten Wert in dieselbe Variable
> zurück. `str(zahl)` geht auch andersherum.

### W6 Anmeldung am Laptop

Am Anmeldetisch steht ein Laptop: Wer mitlaufen will, tippt seine Daten selbst ein, und das
Programm druckt sofort den Kopf der Urkunde. Lege `w6_anmeldung.py` an. Das Programm fragt
nacheinander nach Startnummer, Vorname, Nachname, Jahrgang und Strecke und druckt danach den Kopf
**mit ausgerechnetem Alter**.

> **Hilfe W6**
> **Brauchst du:** `input("Frage? ")` · `int(text)`
> **Tipp:** `vorname = input("Vorname? ")` wartet auf die Eingabe und legt sie in der Variablen ab.
> `input()` liefert **immer Text** — beim Jahrgang also umwandeln, sonst scheitert die Rechnung.
> Baue das Alter erst ein, wenn der Rest läuft.

---

## Expressweg — für alle, die letztes Mal fertig wurden

### W7 Die Zeitmessung liefert Text

Die Zeitmessung schreibt ihre Werte als **Text** in eine Datei — mit Zehntelsekunden:

```python
zeit_text = "4388.4"
```

Lege `w7_umwandeln.py` an und probiere Schritt für Schritt — jeweils erst überlegen, dann ausführen:

1. Gib `zeit_text` mit seinem Typ aus.
2. Versuche `int(zeit_text)`. Was passiert? Schreib die letzte Zeile der Meldung als Kommentar dazu.
3. Mach aus dem Text zuerst eine **Kommazahl** und daraus dann eine **ganze Zahl**. Gib beides mit Typ aus.
4. Was ergibt `int(4388.9)`? **Rundet** `int()` oder **schneidet** es ab? Als Kommentar.
5. Gib zum Schluss **eine** Zeile aus, nur mit `+` zusammengesetzt (kein Komma im `print`):

```
Rohzeit: 4388 Sekunden
```

> **Hilfe W7**
> **Brauchst du:** `float(text)` (Text → Kommazahl) · `int(zahl)` (→ ganze Zahl) · `str(zahl)` (Zahl → Text) · `type(wert)` · `+`
> **Tipp:** `int()` versteht keinen Text mit Punkt. Erst `float()`, dann `int()` — zwei Schritte
> hintereinander: `sekunden = int(float(zeit_text))`. Mit `+` hängst du nur **Text an Text** —
> die Zahl braucht vorher ein `str()`.

### W8 Die Meldeliste als Zeile

So exportiert das Anmeldesystem jede Person — **eine Zeile Text**, die Felder durch Semikolon
getrennt:

```python
zeile = "847;Schneider;Sofia;1970;W;10km"
```

So kommst du an die einzelnen Stücke — gezählt wird ab **null**:

```python
teile = zeile.split(";")
print(teile[0])   # 847
print(teile[1])   # Schneider
```

Lege `w8_meldezeile.py` an. Zerlege die Zeile und drucke daraus den Kopf der Urkunde **mit
ausgerechnetem Alter** — genau wie in W3, nur dass jetzt alles aus dieser einen Zeile kommt.
Dann tausche die Zeile gegen deine eigene aus: Läuft es ohne weitere Änderung?

**Frage zum Mitschreiben:** Das `W` steht nicht auf dem Kopf der Urkunde. Wofür wird es trotzdem
gebraucht?

> **Hilfe W8**
> **Brauchst du:** `text.split(";")` · `teile[0]` · `int(text)`
> **Tipp:** `teile = zeile.split(";")` zerschneidet an jedem Semikolon. Lass dir erst
> `print(teile)` anzeigen. Das erste Stück ist `teile[0]` — gezählt wird ab **null**. Und alles,
> was herauskommt, ist Text.

---

# Teil 2 — Die Nettozeit

> **Ziel der zweiten Hälfte:** Dein Programm macht aus der Zahl der Zeitmessung die Zeile für
> die Urkunde — und prüft sich selbst:
>
> ```
> Nettozeit: mm:ss
> Gegenprobe: True
> ```
>
> Die Zeitmessung liefert nur **4 388 Sekunden**. Was auf der Urkunde steht, rechnet dein
> Programm aus — und weil dir niemand das Ergebnis verrät, beweist es sich mit der Gegenprobe.

### A1 Die drei Arten zu teilen

Lege `a1_teilen.py` an und gib für `4388` und `60` aus:

- `4388 / 60` — „durch", liefert immer eine Kommazahl
- `4388 // 60` — wie oft passt 60 ganz hinein
- `4388 % 60` — was bleibt übrig

Schreib als Kommentar dazu: **Welche zwei der drei Zahlen braucht man für die Urkunde?**

> **Hilfe A1**
> **Brauchst du:** `/` · `//` · `%` · `print(...)`
> **Tipp:** Drei Zeilen, in jeder ein `print` mit einer Rechnung darin: `print(4388 // 60)`.

### A2 Sekunden werden mm:ss

Das ist die Kernaufgabe. Lege `a2_nettozeit.py` an. Gegeben ist `zielzeit_sekunden = 4388` — die
Zeit von Startnummer 847, Sofia Schneider. Berechne `minuten` und `sekunden` und gib die Zeile für die Urkunde aus:

```
Nettozeit: mm:ss
```

Die Sekunden stehen **immer zweistellig** da — wie auf jeder Digitaluhr.

**Gegenprobe:** Aus `minuten` und `sekunden` wieder die Gesamtsekunden ausrechnen und mit 4388
vergleichen. Das Ergebnis mit ausgeben — es muss `True` herauskommen.

> **Hilfe A2 — Schritt für Schritt**
> **Brauchst du:** `//` · `%` · `str(zahl)` · `+` (Text zusammensetzen) · `==` (vergleichen)
>
> 1. **Erst mit 150 üben** — da weißt du, dass `2:30` herauskommen muss (wie an der Tafel).
>    Setz `zielzeit_sekunden = 150`, erst am Ende `4388`.
> 2. `minuten = zielzeit_sekunden // 60` — wie oft passt 60 ganz hinein.
>    `sekunden = zielzeit_sekunden % 60` — was bleibt übrig.
> 3. Zwischendurch prüfen: `print(minuten, sekunden)` muss bei 150 `2 30` zeigen.
> 4. Für die Urkunde alles zu **einem** Text zusammenhängen:
>    `print("Nettozeit: " + str(minuten) + ":" + str(sekunden))`
> 5. **Die Null:** Probier `zielzeit_sekunden = 125`. Da kommt `2:5` statt `2:05`. Zerleg die
>    Sekunden in Zehner und Einer: `sekunden // 10` ist die Zehnerstelle (bei 5: `0`),
>    `sekunden % 10` die Einerstelle (bei 5: `5`). Häng beide als Text hintereinander —
>    statt `str(sekunden)` also `str(sekunden // 10) + str(sekunden % 10)`.
> 6. **Gegenprobe:** rückwärts rechnen und vergleichen:
>    `print("Gegenprobe:", minuten * 60 + sekunden == zielzeit_sekunden)`
> 7. Jetzt `zielzeit_sekunden = 4388` einsetzen.

### Geschafft?

- [ ] `a2_nettozeit.py` gibt die Nettozeit als `mm:ss` aus — Sekunden **zweistellig**
- [ ] Die Gegenprobe steht darunter und zeigt `True`
- [ ] Du kannst sagen, was deine Gegenprobe beweist — und was sie **nicht** beweist
- [ ] Alle Dateien liegen in `Meine Programme\03_Operatoren`

Damit ist das Ziel der Stunde erreicht. Wer fertig ist, macht hier weiter:

---

## Für die Schnellen — Teil 2

### A3 Noch zwei Läuferinnen

Kopiere A2 als `a3_drei.py` und rechne auch diese beiden Nettozeiten aus:

- Startnummer 836, Andrea Winkler: **2 801** Sekunden
- Startnummer 851, Monika Maier: **3 399** Sekunden

Prüf eine davon von Hand nach — mit Papier, nicht mit Python.

> **Hilfe A3**
> **Brauchst du:** dasselbe wie in A2
> **Tipp:** Kopiere die drei Zeilen aus A2 und ändere nur die Sekundenzahl. Dass dabei fast
> derselbe Code dreimal dasteht, stört zu Recht — am 20.10. räumen wir das mit Funktionen auf.

### B1 Der Halbmarathon braucht Stunden

Lege `b1_halbmarathon.py` an. Gegeben `zielzeit_sekunden = 7845`. Gib aus:

```
Nettozeit: 2:10:45
```

> **Hilfe B1**
> **Brauchst du:** `//` · `%`
> **Tipp:** Dieselben zwei Operatoren, zweimal angewendet. Erst die Stunden abtrennen — eine
> Stunde hat 3 600 Sekunden —, dann mit dem **Rest** weiterrechnen wie in A2.

### C1 Das Tempo

Wie viele Minuten und Sekunden brauchte Sofia Schneider für einen Kilometer? Die Strecke ist
10 km. Lege `c1_tempo.py` an. Erwartet: `Tempo: 7:18 min/km`.

> **Hilfe C1**
> **Brauchst du:** `//` · `%`
> **Tipp:** Erst die Sekunden je Kilometer ausrechnen (`4388 // 10`), dann dieselbe Umrechnung
> wie in A2. Wer `7.31` herausbekommt, hat Bruchteile von Minuten statt Sekunden.

### C2 Schneller als letztes Jahr?

Sofia Schneider ist letztes Jahr auch gelaufen: **4 452** Sekunden. Lege `c2_vergleich.py` an und
lass das Programm vier Fragen beantworten — jede Antwort ist `True` oder `False`, nur die dritte
ist eine Zahl:

```
Unter 75 Minuten?          True
Schneller als im Vorjahr?  True
Sekunden schneller:        64
Unter 70 Minuten?          False
```

> **Hilfe C2**
> **Brauchst du:** `<` · `>` · `<=` · `>=` · `==` · `!=`
> **Tipp:** Ein Vergleich liefert `True` oder `False` — genau wie deine Gegenprobe in A2. Die
> Minuten rechnest du in Sekunden um, nicht umgekehrt. Mit solchen `True`/`False` entscheidet
> das Programm am 06.10. die Altersklasse.

---

## Und wenn du alles hast

Vergleiche deine Lösung von A2 mit der einer anderen Person: Gebt ihr die führende Null auf
demselben Weg aus? Welche der beiden Fassungen versteht jemand, der sie zum ersten Mal liest,
schneller?
