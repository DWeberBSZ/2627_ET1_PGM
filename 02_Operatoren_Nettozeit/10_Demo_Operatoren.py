"""
Stunde 3 - 29.09.2026 - Operatoren: die Nettozeit
Programmieren ET1, Technikerschule Elektrotechnik

Lernsituation: Neumarkter Stadtlauf - Auftrag 3
Die Zeitmessung liefert Sekunden. Auf der Urkunde steht mm:ss.

TEIL 1-3 ist das Live-Coding in der Stunde (wenige Minuten, nur das Prinzip,
nur mit 150 s - die 4388 rechnet die Klasse selbst).
Der NACHSCHLAG unten wird erst NACH der Uebungsphase gezeigt - die
fuehrende Null und die Klammerfalle sollen die Klasse selbst finden.

Starten:  python 10_Demo_Operatoren.py
"""

# ---------------------------------------------------------------
# 1. Das Problem - der "schlechte Vorschlag" aus dem Zielgespraech
# ---------------------------------------------------------------

print(4388 / 60)                  # 73.1333... - "also 73 Minuten 13, drucken wir?"
print(150 / 60)                   # 2.5 - "150 Sekunden sind also 2 Minuten 50?"
# Nein: 2:30. Die Stelle hinter dem Komma sind Bruchteile einer Minute,
# keine Sekunden. So kann das nicht auf die Urkunde.


# ---------------------------------------------------------------
# 2. // und % - das Paar fuer die Umrechnung, gezeigt an 150
# ---------------------------------------------------------------
# //  wie oft passt es ganz hinein
# %   was bleibt uebrig
# Die 4388 rechnet die Klasse in A2 selbst - hier nicht vorrechnen.

zeit = 150
minuten = zeit // 60     # 2 volle Minuten
sekunden = zeit % 60     # 30 Sekunden bleiben

print(minuten, "Minuten und", sekunden, "Sekunden")


# ---------------------------------------------------------------
# 3. Die Gegenprobe
# ---------------------------------------------------------------
# Zurueckrechnen - passt es wirklich zusammen?

print(minuten * 60 + sekunden)           # 150
print(minuten * 60 + sekunden == zeit)   # True

# == fragt "ist das gleich?" und liefert ein bool - bekannt aus Stunde 2.
# =  dagegen legt einen Wert ab.

# ---- Hier endet das Live-Coding. "Jetzt ihr: dieselbe Rechnung mit
# ---- 4388 - und die Zeile fuer die Urkunde" (Aufgabe A2).


# ===============================================================
# NACHSCHLAG - erst nach der Uebungsphase zeigen
# ===============================================================

# 4. Die fuehrende Null: 73:8 ist nicht 73:08
# ---------------------------------------------------------------

minuten = 4388 // 60     # 73
sekunden = 4388 % 60     # 8

print(str(minuten) + ":" + str(sekunden))       # 73:8  - so nicht

# Zwei Wege, beide nur mit dem Stoff dieser Stunde:
print(str(minuten) + ":" + str(sekunden // 10) + str(sekunden % 10))   # 73:08
# oder, wenn die Klasse schon Verzweigungen kennt (ab 06.10.):
#   if sekunden < 10: ... "0" davorsetzen


# 5. Punkt vor Strich - was ohne Klammer schiefgeht
# ---------------------------------------------------------------

start = 36024        # 10:00:24 in Sekunden seit Mitternacht
ziel = 40412         # 11:13:32

print(ziel - start // 60)      # 39812 - Unsinn: erst start // 60, dann minus
print((ziel - start) // 60)    # 73    - so war es gemeint

# Regel: Muss man beim Lesen ueberlegen, setzt man die Klammer.
