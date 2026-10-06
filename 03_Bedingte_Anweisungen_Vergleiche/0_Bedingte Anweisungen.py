""" 
06.10.26
╔══════════════════════════════════╗
║       BEDINGTE ANWEISUNGEN       ║
╚══════════════════════════════════╝
""" 

# Mit bedingten Anweisungen kann der PROGRAMMABLAUF gesteuert werden.
# Das Programm arbeitet in Abhängigkeit von BEDINGUNGEN nur bestimmte Anweisungen ab.

"""
Arbeitsauftrag:
===============
Informieren Sie sich zu bedingten Anweisungen mithilfe des Fachbuchs.

- Lesen Sie Kapitel 8.1 "if-Verzweigung" im Fachbuch

Zeit: 8 Minuten, Einzelarbeit
"""

# BEDINGTE ANWEISUNGEN
# =====================
""" Bedingte Anweisung, auch genannt: "if-Anweisung"

Aufbau einer if-Anweisung:

if BEDINGUNG: # : nicht vergessen
    Anweisung 1 # Anweisungen mit TAB einrücken!
    Anweisung 2 # Die Anweisungsfolge innerhalb einer if-Anweisung nennt sich ANWEISUNGSBLOCK
    ...
    
else: # Der else-Zweig ist optional
    Anweisung 1
    Anweisung 2
    ...
    

WICHTIG: Die BEDINGUNG muss sich zu True oder False auswerten lassen!
    - Entweder: Verwendung von True, False oder einer Variable vom Datentyp bool
    - Oder: Vergleichsaudrücke -> machen wir später!

"""
#a = 5.4 # Datentyp: float, Gleitkommazahl
#b = 4   # Datentyp: Integer, Ganzzahl
#c = True # Datentyp: Bool, Wahrheitswert
#d = "Dominik" # Datentyp: String, Zeichenkette

#ergebnis_a = isinstance(a, int) # Was macht diese Funktion?
# Vorschlag Melanie: "Ist meine Variable a vom Typ Integer?"

# Die Funktion isinstance prüft den Datentyp einer Variable.
#ergebnis_b = isinstance(b, int)

#print(ergebnis_a)
#print(ergebnis_b)

#print(isinstance(ergebnis_a, bool))

a = 5.4

ist_int = isinstance(a, int)

if ist_int:
    print("Die Variable ist vom Datentyp Integer")
    
else: # kein Integer
    # restliche Fälle überprüfen (andere Datentypen)
    ist_float = isinstance(a, float) # ...
    
    
    
    
    
    



















