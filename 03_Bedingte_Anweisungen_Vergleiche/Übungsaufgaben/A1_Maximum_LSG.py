'''
Aufgabe: Maximum von drei Zahlen
=================================

Arbeitsauftrag:

> Ziel ist die Erstellung eines Programms, welches nacheinander drei Ganzzahlen von der Konsole einliest
  und den Wert der größten der drei Zahlen auf der Konsole ausgibt.
  
a) Erstellen Sie zunächst einen PAP, der alle hierfür notwendigen Schritte beinhaltet 
   und den Programmablauf sinnvoll beschreibt.
  
b)Programmieren Sie das zugehörige Programm. 
  - Speichern Sie die eingelesenen Zahlen zunächst in Variablen ab.
  - Unterscheiden Sie mithilfe von bedingten Anweisungen, welche der drei Zahlen die größte ist.
  - Geben Sie die größte der drei Zahlen in folgender Form auf der Konsole aus: 
    "Das Maximum der drei Zahlen ist xx."

Zeit: 30 Minuten, Einzelarbeit.
'''

zahl1 = int(input("Bitte gebe Zahl 1 ein: "))
zahl2 = int(input("Bitte gebe Zahl 2 ein: "))
zahl3 = int(input("Bitte gebe Zahl 3 ein: "))

max = 0 # für positive Zahlen

if zahl1 > max:
   # ja 
   max = zahl1
# nein 

if zahl2 > max:
    max = zahl2
    
if zahl3 > max:
  max = zahl3
        
print(f"Das Maximum der drei Zahlen ist {max}.")

    

