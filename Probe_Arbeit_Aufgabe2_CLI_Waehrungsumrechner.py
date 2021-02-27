#!/usr/bin/env python3

def eingabe_pruefen(eingabe : str):
    for i in eingabe:
        if i not in '0123456789':
            return False
    return True

def eingabe_verarbeiten():
    while True:
        eingabe = input('Gib die zu wechselnde Menge ein:\n')    
        if eingabe_pruefen(eingabe):
            betrag = int(eingabe)
            break
        else:
            print('Ungültige Eingabe!')
            continue
    return betrag


ueberschrift = 'Unit-Converter\n--------------\n'
begruessung = 'Wähle eine der folgenden Möglichkeiten:\n'
moeglichkeit_1 = 'Euro in Dollars [1],\n'
moeglichkeit_2 = 'Dollars in Euro [2],\n'
moeglichkeit_3 = 'Euro in philippinische Pesos [3],\n'
moeglichkeit_4 = 'Philippinische Pesos in Euro [4],\n'
beenden = 'exit [5]\n'

euro_zu_dollar_faktor = 1.17
dollar_zu_euro_faktor = 0.85
euro_zu_p_pesos_faktor = 56.66
p_pesos_zu_euro_faktor = 0.018

auswahl = 1
while auswahl:
    eingabe = input(ueberschrift + begruessung + moeglichkeit_1 + moeglichkeit_2 + moeglichkeit_3 + moeglichkeit_4 + beenden)
    if eingabe not in '12345':
        print('\nUngültige Auswahl!\n')
        continue
    
    auswahl = int(eingabe)
        
    if auswahl == 1:
        betrag = eingabe_verarbeiten()
        print(betrag * euro_zu_dollar_faktor, '\n')
        continue
    
    elif auswahl == 2:
        betrag = eingabe_verarbeiten()
        print(betrag * dollar_zu_euro_faktor, '\n')
        continue
    
    elif auswahl == 3:
        betrag = eingabe_verarbeiten()
        print(betrag * euro_zu_p_pesos_faktor, '\n')
        continue
    
    elif auswahl == 4:
        betrag = eingabe_verarbeiten()
        print(betrag * p_pesos_zu_euro_faktor, '\n')
        continue

    elif auswahl == 5:
        print('Servus!')
        break
