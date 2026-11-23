"""
24.11.26
╔══════════════════════════════════════╗
║  FUNKTIONEN – PARAMETER UND RETURN   ║
╚══════════════════════════════════════╝
"""
# Lernsituation: Wir digitalisieren den Kaminkehrerlauf
#                (Unterrichtsszenario — keine Anfrage der Veranstalter.)
#
# Ü2 Bestzeit — die Funktion vom 17.11. bekommt einen Parameter und gibt die Zeit zurück
#   Am 17.11. hat zeige_bestzeit() die kleinste Zeit EINER Liste ausgegeben.
#   Jetzt gibt es zwei Strecken. Schreiben Sie die Funktion bestzeit(zeiten): Sie sucht die
#   kleinste Zeit in der Liste, die sie bekommt, und gibt sie zurück.
#   Rufen Sie die Funktion für beide Listen auf und geben Sie die Bestzeiten aus.
#   Erwartete Ausgabe:   Bestzeit 5 km: 24 min
#                        Bestzeit 10 km: 47 min

# ---------- Ihre Funktion



zeiten_5km = [31, 24, 28]
zeiten_10km = [52, 47, 61]

# ---------- Ihr Programm



# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - In der Funktion steht überall der Parameter zeiten — nicht zeiten_5km oder zeiten_10km.
# - Die schnellste Zeit suchen wie am 10.11.: mit der ersten Zeit anfangen, dann jede Zeit vergleichen.
# - Am Ende der Funktion: return schnellste — die Ausgabe macht das Programm.
