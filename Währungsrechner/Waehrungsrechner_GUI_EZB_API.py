import sys, urllib.request, json, datetime
from decimal import Decimal, getcontext
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QLineEdit, QLabel, QApplication, QMessageBox
from PyQt5.QtCore import QRect

class Waehrungsrechner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 317)
        self.setWindowTitle("Währungsrechner mit Kursen der Europäischen Zentralbank")
        self.setObjectName("fenster")
        try:
            json_string = urllib.request.urlopen("https://api.exchangeratesapi.io/latest").read().decode("utf-8")
            self.raten = {"EUR":json.loads(json_string)}
        except BaseException as err:
            QMessageBox.about(self, "Fehler", f"{err}")
            app.quit()
        
        namen = ["Euro", "Kanadischer Dollar", "Hongkong-Dollar", "Isländische Krone", "Philippinischer Peso", 
                 "Dänische Krone", "Ungarischer Forint", "Tschechische Krone", "Australischer Dollar", "Rumänischer Leu",
                 "Schwedische Krone", "Indonesische Rupiah", "Indische Rupie", "Brasilianischer Real", "Russischer Rubel",
                 "Kroatische Kuna", "Japanischer Yen", "Thai Baht", "Schweizer Franken", "Singapur-Dollar", "Polnischer Zloty",
                 "Bulgarischer Lew", "Türkische Lira", "Chinesischer Yuan", "Norwegische Krone", "Neuseeland-Dollar", 
                 "Südafrikanischer Rand", "US-Dollar", "Mexikanischer Peso", "Israelischer Schekel", "Britischer Pfund", 
                 "Südkoreanischer Won", "Malaysischer Ringit"]

        iso = ["EUR"]
        for key in self.raten['EUR']['rates']:
            iso.append(key)
        self.waehrungen = dict(zip(namen, iso))

        self.ursprungswaehrung = QComboBox(self)
        self.ursprungswaehrung.setGeometry(QRect(15, 100, 210, 22))
        self.ursprungswaehrung.setObjectName("basis")
        self.endwaehrung = QComboBox(self)
        self.endwaehrung.setGeometry(QRect(425, 100, 210, 22))
        self.endwaehrung.setObjectName("endprodukt")
        for k in sorted(self.waehrungen):
            self.ursprungswaehrung.addItem(k)
            self.endwaehrung.addItem(k)
      
        knopf_umrechnen = QPushButton("Umrechnen", self)
        knopf_umrechnen.setGeometry(QRect(255, 100, 141, 61))
        knopf_umrechnen.setObjectName("kn_1")
        knopf_umrechnen.clicked.connect(self.umrechnen)            
        
        self.eingabe = QLineEdit(self)
        self.eingabe.setGeometry(QRect(15, 140, 210, 21))
        self.eingabe.setObjectName("eingabe")
        self.ausgabe = QLineEdit(self)
        self.ausgabe.setGeometry(QRect(425, 140, 210, 21))
        self.ausgabe.setObjectName("ausgabe")
        self.ausgabe.setReadOnly(True)
        
        zeit = datetime.datetime.strptime(self.raten['EUR']['date'], '%Y-%m-%d')
        zeitpunkt = zeit.strftime("%d.%m.%Y")
        datum = QLabel(self)
        datum.setGeometry(QRect(210, 30, 250, 31))
        datum.setObjectName("datum")
        datum.setText(f"Wechselkurse vom {zeitpunkt}")

        knopf_beenden = QPushButton("Beenden", self)
        knopf_beenden.setGeometry(QRect(555, 270, 80, 30))
        knopf_beenden.setObjectName("kn_2")
        knopf_beenden.clicked.connect(self.beenden)

    # Die Wechselkurse für den EURO werden mit dem Starten des Programms im Dictionary "raten" unter dem Schlüssel "EUR" gespeichert. Hat man
    # einen Betrag mit maximal einem Komma eingeben, überprüft die Methode "umrechnen" ob sich die Ausgangswährung im Dictionary "raten" befindet.
    # Wenn ja wird die Ausgangswährung mit der Umrechnungsrate der Endwährung multipliziert. Befindet sich die Ausgangswährung nicht in "raten",
    # wohl aber die Endwährung, wird der Betrag durch den Umrechnungsfaktor "Endwährung zu Ursprungswährung" geteilt. Nur wenn beides nicht
    # möglich ist, werden von der Web-API der EZB die Umrechnungsraten der ausgewählten Ursprungswährung angefordert, und unter dem Schlüssels des  Dies soll Traffic minimieren.   
    
    def umrechnen(self):
        if not self.eingabe.text():
            QMessageBox.about(self, "Fehler", "Sie müssen einen Betrag eingeben!")
            return
        elif self.ursprungswaehrung.currentText() == self.endwaehrung.currentText():
            QMessageBox.about(self, "Fehler", "Sie müssen eine Währung auswählen in die umgerechnet werden soll!")
            return
        
        basis = self.waehrungen[self.ursprungswaehrung.currentText()]
        resultat = self.waehrungen[self.endwaehrung.currentText()]
        eingabe = ""
        for i in self.eingabe.text():
            if i in "0123456789,":
                eingabe += i
        if eingabe.count(",") > 1:
            QMessageBox.about(self, "Fehler", "Sie können maximal ein Komma eingeben!")
            return
        eingabe = Decimal(eingabe.replace(",", "."))
        
        if self.raten.get(basis):
            self.ausgabe.setText((str(round(eingabe * Decimal(self.raten[basis]['rates'][resultat]), 2))).replace(".", ","))
        elif self.raten.get(resultat):
            self.ausgabe.setText((str(round(eingabe / Decimal(self.raten[resultat]['rates'][basis]), 2))).replace(".", ","))
        else:
            try:
                json_string = urllib.request.urlopen(f"https://api.exchangeratesapi.io/latest?base={basis}").read().decode("utf-8")
                self.raten[basis] = json.loads(json_string)
            except BaseException as err:
                QMessageBox.about(self, "Fehler", f"{err}")
                return
            self.ausgabe.setText((str(round(eingabe * Decimal(self.raten[basis]['rates'][resultat]), 2))).replace(".", ","))
        
    def beenden(self):
        bestaetigung = QMessageBox()
        bestaetigung.setIcon(QMessageBox.Question)
        bestaetigung.setWindowTitle("Programm beenden")
        bestaetigung.setText("Das Programm wirklich beenden?")
        bestaetigung.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if bestaetigung.exec() == QMessageBox.Ok:
            app.quit()

stylesheet = """
#datum
{
    font-size: 12pt;
    font-family: monospace;
}
#basis, #endprodukt
{
    font-size: 9pt;
    font-family: arial;
}
#eingabe, #ausgabe
{
    font-size: 9pt;
    font-family: monospace;
}
#kn_1
{
    background-color: #5B8266;
    color: 'white';
    font-size: 10pt;
    font-weight: 900;
}
#kn_2
{
    background-color: #E26D5C;
    color: 'white';
    font-size: 10pt;
    font-weight: 900;
}
"""

app = QApplication(sys.argv)
win = Waehrungsrechner()
win.setStyleSheet(stylesheet)
win.show()
sys.exit(app.exec_())

        

