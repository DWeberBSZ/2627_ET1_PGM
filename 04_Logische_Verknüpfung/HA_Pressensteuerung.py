"""
20.10.26
╔══════════════════════════════════╗
║           HAUSAUFGABE            ║
╚══════════════════════════════════╝
"""

"""
Aufgabe: Die Pressensteuerung
=============================

Eine hydraulische Presse darf nur fahren, wenn niemand die Hand im Werkzeug hat.
Deshalb hat sie eine ZWEIHANDBEDIENUNG: zwei Taster, so weit auseinander, dass man beide Hände
braucht. Dazu kommen eine SCHUTZTÜR und ein NOT-AUS.

Das Programm bekommt die vier Signale als Konsoleneingabe, jeweils als 1 oder 0:

    Signal          1 bedeutet      0 bedeutet
    Taster links    gedrückt        nicht gedrückt
    Taster rechts   gedrückt        nicht gedrückt
    Schutztür       geschlossen     offen
    Not-Aus         gedrückt        nicht gedrückt

Arbeitsauftrag:

a) Die Freigabe:
   Die Presse fährt nur, wenn BEIDE Taster gedrückt sind, die Schutztür GESCHLOSSEN ist
   und der Not-Aus NICHT gedrückt ist. Sonst ist sie gesperrt.
   Prüfen Sie das mit EINER EINZIGEN if-Bedingung und geben Sie aus:

       Presse: FÄHRT        bzw.        Presse: GESPERRT

b) Der Grund:
   Geben Sie bei einer Sperre zusätzlich GENAU EINE Meldung aus – die wichtigste zuerst:

       1. Grund: Not-Aus gedrückt
       2. Grund: Schutztür offen
       3. Grund: Beide Taster drücken

   Ist z. B. der Not-Aus gedrückt UND die Tür offen, erscheint nur die Not-Aus-Meldung.

Testfälle für a) und b):

    Nr.  links  rechts  Tür  Not-Aus   Ausgabe
    T1   1      1       1    0         Presse: FÄHRT
    T2   1      0       1    0         Presse: GESPERRT / Grund: Beide Taster drücken
    T3   1      1       0    0         Presse: GESPERRT / Grund: Schutztür offen
    T4   1      1       1    1         Presse: GESPERRT / Grund: Not-Aus gedrückt
    T5   0      0       0    1         Presse: GESPERRT / Grund: Not-Aus gedrückt
    T6   0      1       0    0         Presse: GESPERRT / Grund: Schutztür offen

Gut zu wissen: In der echten Maschine reicht das noch nicht. Die Norm (DIN EN ISO 13851)
verlangt, dass beide Taster INNERHALB VON 0,5 SEKUNDEN gedrückt werden – sonst könnte
jemand einen Taster festklemmen. Dafür bräuchte man eine Zeitmessung.

Bonus: HA_Bonus_Schaltjahr.py
"""

# Eingabe

# Verarbeitung

# Ausgabe































# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - Die Eingabe ist Text. Mit int(input(...)) wird daraus eine Zahl,
#   die Sie mit == 1 oder == 0 vergleichen können.
# - a) braucht dreimal and.
# - b) ist eine elif-Kette. Wie bei der Paket-Zuordnung entscheidet die REIHENFOLGE,
#   welche Meldung gewinnt.
