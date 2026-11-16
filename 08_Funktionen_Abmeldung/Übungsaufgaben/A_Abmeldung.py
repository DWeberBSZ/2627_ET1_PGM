"""
17.11.26
╔══════════════════════════════════╗
║    FUNKTIONEN – DIE ABMELDUNG    ║
╚══════════════════════════════════╝
"""
# Lernsituation: Wir digitalisieren den Kaminkehrerlauf
#                (Unterrichtsszenario — keine Anfrage der Veranstalter.)
#
# Das ist unser Programm: die Anmeldung mit dem Display. Der Lauf hat 250 Startplätze.
#
# Aufgabe 3a: Das Display wird zur Funktion.
#   Schreiben Sie hier oben die Funktion zeige_display(). In ihren Rumpf kommen die vier
#   Display-Zeilen aus der Anmeldung. In der Anmeldung steht danach nur noch der Aufruf.
#   Test: 1 · Toni Schlot   →   Angemeldet: 5   Plätze übrig: 245

# ---------- Ihre Funktion (oben im Programm: erst merken, dann aufrufen)



# ---------- unser Programm
startliste = ["Sofia Schneider", "Petra Ostermeier", "Lena Huber", "Emil Bauer"]

auswahl = ""
while auswahl != "0":
    auswahl = input("1 Anmeldung · 0 Ende: ")

    if auswahl == "1":                          # ---------- Anmeldung
        name = input("Name: ")
        startliste.append(name)
        anzahl = len(startliste)                # das Display: diese vier Zeilen
        uebrig = 250 - anzahl
        print("Angemeldet:", anzahl)
        print("Plätze übrig:", uebrig)

    # Aufgabe 3b: Die Abmeldung verwendet das Display wieder.
    #   Ergänzen Sie hier den Menüpunkt 2:  elif auswahl == "2":
    #   Das Programm liest den Namen ein, entfernt den Läufer aus der Startliste und ruft das
    #   Display auf. Neu: startliste.remove(name) entfernt diesen Läufer aus der Liste.
    #   Ergänzen Sie oben auch den Text des Menüs:  1 Anmeldung · 2 Abmeldung · 0 Ende
    #   Test (neuer Start): 2 · Lena Huber   →   Angemeldet: 3   Plätze übrig: 247


# ──────────────────────────────────────────────────────────────────────
# TIPPS – erst lesen, wenn Sie nicht weiterkommen!
# - 3a: Die Funktion steht auf dem Arbeitsblatt, Aufgabe 1, Zeilen 1 bis 5 — die Einrückung zählt.
# - 3a: Die vier Display-Zeilen ausschneiden und unter def einfügen. In der Anmeldung bleibt: zeige_display()
# - 3a: Die Funktion steht OBEN im Programm — sonst: NameError: name 'zeige_display' is not defined.
# - 3b: Der Zweig Abmeldung in Ihrem PAP hat drei Schritte: Eingabe, entfernen, Aufruf — eingerückt unter elif auswahl == "2":
# - 3b: remove braucht den Namen genau so, wie er in der Liste steht.
