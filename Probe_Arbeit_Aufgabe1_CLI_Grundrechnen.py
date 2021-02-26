#!/usr/bin/env python3

# Mir wurden am 16 Dezember 2020 von der Firma, bei der Mitte Oktober ein Vorstellungsgespräch stattgefunden hatte, 
# zwei Aufgaben gestellt und vier Stunden Zeit gegeben um meine Quellcodes einzuschicken. Anschließend gab es eine 
# Webex-Konferenz in der ich meine Lösungen vorstellte und erklärte. 
# Das Ziel der ersten Aufgabe war es, ein Kommandozeilen-Programm zu entwerfen, dass vom Benutzer zwei Ziffern und 
# das Symbol für eine der vier Grundrechenarten annimmt und das Ergebnis ausgibt, wobei nur Divisonen ohne Rest 
# möglich sein sollten. Ein Programm welches lief bis der Benutzer es abbrach wurde nicht gefordert.

def grundrechnen_version_1(operation : str):
    operand_1, operand_2 = int(operation[0]), int(operation[2]) 
    if operation[1] == '+':
        return operand_1 + operand_2
    elif operation[1] == '-':
        return operand_1 - operand_2
    elif operation[1] == '*':
        return operand_1 * operand_2
    elif operation[1] == '/':
        if operand_1 % operand_2 != 0:
            return 'Ungültige Eingabe!'
        else:
            return operand_1 / operand_2
    
def grundrechnen_version_2(operation : str):
    operand_1, operand_2 = int(operation[0]), int(operation[2])
    if operation[1] == '+':
        operator = lambda x, y : x + y
    elif operation[1] == '-':
        operator = lambda x, y : x - y
    elif operation[1] == '*':
        operator = lambda x, y : x * y
    elif operation[1] == '/':
        if operand_1 % operand_2 != 0:
            return 'Ungültige Eingabe'
        else:
            operator = lambda x, y : x / y
    return operator(operand_1, operand_2)

# Die ersten beiden Funktionen lieferte ich ab, wobei ich nicht ganz zufrieden war. Die dritte, elegantere 
# Funktion kam mir erst Tage später in den Sinn. Bei dem abgegebenen Programm war zudem die Fehlerkontrolle in jeder der
# beiden Funktionen enthalten. Ich habe sie hier ins Hauptprogramm verlagert damit der Unterschied der dritten
# Funktion zu den anderen besser zur Geltung kommt.

def grundrechnen_version_3(operation : str):
    operationen = {'+' : lambda x, y : x + y, '-' : lambda x, y : x - y, '*' : lambda x, y : x * y, '/' : lambda x, y : x // y}
    operand_1, operator, operand_2 = int(operation[0]), operation[1], int(operation[2])
    if operator == '/' and operand_1 % operand_2 != 0:
        return "Ungültige Eingabe!"
    return operationen[operator](operand_1, operand_2)    


eingabe = input('Geben Sie eine Ziffer, einen Operator für eine der vier Grundrechenarten (+, -, * und /) und noch eine Ziffer ein,\n(Divisionen sind nur ohne Rest möglich):\n').replace(' ', '')
if len(eingabe) != 3:
    operation = "Es dürfen nur zwei Ziffern und ein Operator eingegeben werden!" 
elif eingabe[0] not in "123456789" or eingabe[2] not in "123456789" or eingabe[1] not in "+-*/":
    operation = "Sie müssen einen Operator (+, -, * oder /) zwischen zwei Ziffern von 1-9 eingeben!"
else:
    operation = eingabe

print(grundrechnen_version_1(operation))
print(grundrechnen_version_2(operation))
print(grundrechnen_version_3(operation))

