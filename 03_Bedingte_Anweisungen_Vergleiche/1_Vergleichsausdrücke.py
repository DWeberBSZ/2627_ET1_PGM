""" 
06.10.26
╔══════════════════════════════════╗
║       VERGLEICHSAUSDRÜCKE        ║
╚══════════════════════════════════╝
""" 
# VERGLEICHSAUSDRÜCKE werden häufig in Verbindung mit bedingten Anweisungen verwendet.

alter_sus_1 = 22 # Datentyp Integer
alter_sus_2 = 22
alter_sus_3 = 20

# 6 unabhängig Abfragen
if alter_sus_1 > alter_sus_2:
    print("SuS1 ist älter als SuS2")
    
if alter_sus_1 >= alter_sus_2: # das geht NICHT: =>
    print("SuS1 ist älter oder gleich alt wie SuS2")
    
if alter_sus_1 < alter_sus_2:
    print("SuS1 ist jünger als SuS2")
    
if alter_sus_1 <= alter_sus_2: # das geht NICHT: =<
    print("SuS1 ist jünger oder gleich alt wie SuS2")
    
if alter_sus_1 == alter_sus_3: # Beim Vergleichen == benutzen und NICHT =
    print("SuS1 ist genauso alt wie SuS3")
    
if alter_sus_2 != alter_sus_3: # ungleich
    print("SuS2 ist nicht so alt wie SuS3")
    
if not(alter_sus_2 != alter_sus_3): 
    print("SuS2 und SuS3 sind gleich alt (nicht ungleich)")
    
if True:
    print("Das ist immer True")

    
# Vergleichsoperatoren
# > größer
# >= größer oder gleich
# < kleiner
# <= kleiner oder gleich
# == ist gleich
# != ist ungleich

