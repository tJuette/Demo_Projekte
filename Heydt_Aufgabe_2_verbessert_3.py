#!/usr/bin/env python3

def betrag_eingeben():
    korrekte_eingabe = False
    while not korrekte_eingabe:
        betrag = '0' + input('Gib die zu wechselnde Menge ein:\n')
        korrekte_eingabe = True
        for i in betrag:
            if i not in '0123456789':
                korrekte_eingabe = False    
                print('Ungültige Eingabe!')
    return int(betrag)    
   
ueberschrift = 'Unit-Converter\n--------------\n'
begruessung = 'Wähle eine der folgenden Möglichkeiten:\n'
moeglichkeit_1 = 'Euro in Dollars [1],\n'
moeglichkeit_2 = 'Dollars in Euro [2],\n'
moeglichkeit_3 = 'Euro in philippinische Pesos [3],\n'
moeglichkeit_4 = 'Philippinische Pesos in Euro [4],\n'
beenden = 'exit [5]\n'

dollar_zu_euro_faktor = 1.17
euro_zu_dollar_faktor = 0.85
euro_zu_p_pesos_faktor = 56.66
p_pesos_zu_euro_faktor = 0.018

auswahl = 1
while auswahl != 5:
    eingabe = input(ueberschrift + begruessung + moeglichkeit_1 + moeglichkeit_2 + moeglichkeit_3 + moeglichkeit_4 + beenden)
    if len(eingabe) != 1 or eingabe not in '12345':
        print('\nUngültige Auswahl!\n')
        continue
    
    auswahl = int(eingabe)
        
    if auswahl == 1:
        print(betrag_eingeben() * euro_zu_dollar_faktor, '\n')
            
    elif auswahl == 2:
        print(betrag_eingeben() * dollar_zu_euro_faktor, '\n')
    
    elif auswahl == 3:
        print(betrag_eingeben() * euro_zu_p_pesos_faktor, '\n')
        
    elif auswahl == 4:
        print(betrag_eingeben() * p_pesos_zu_euro_faktor, '\n')
    
    else:
        print('Servus!')