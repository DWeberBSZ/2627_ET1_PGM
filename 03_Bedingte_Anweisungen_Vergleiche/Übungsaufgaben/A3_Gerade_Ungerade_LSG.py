'''
Aufgabe: Restlos teilbar?
=================================

Arbeitsauftrag:

- Schreiben Sie ein Python-Skript, welches eine Ganzzahl von der Konsole einliest
  und überprüft, ob diese gerade oder ungerade ist.
  
- Geben Sie das Ergebnis als Textinformation auf der Konsole aus.
'''
zahl = int(input("Bitte geben Sie eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")