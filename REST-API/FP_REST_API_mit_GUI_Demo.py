#!/usr/bin/env python3
import PyQt5, sys, json, urllib.request, pathlib, xml.sax.saxutils, pymysql.cursors
import xml.etree.ElementTree as ET
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton, QMessageBox, QWidget, QGridLayout, QPlainTextEdit, QLineEdit, QFileDialog 
from PyQt5.QtCore import Qt

class MeinHauptFenster(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("New York Times Bestseller Liste")
        self.resize(1040, 720)
        self.ausgabefeld = QPlainTextEdit()
        self.ausgabefeld.setReadOnly(True)
        self.ausgabefeld.setObjectName("ausgabe")
        self.setObjectName("fenster")
        
        haupt_container = QWidget(self)
        haupt_gitter = QGridLayout()
        haupt_container.setLayout(haupt_gitter)
        self.setCentralWidget(haupt_container)
        haupt_gitter.addWidget(self.ausgabefeld, 0, 0)
        haupt_gitter.setColumnStretch(0, 5)
        haupt_gitter.setRowStretch(0, 20)
        
        eingabe_container = QWidget(haupt_container)
        eingabe_gitter = QGridLayout()
        eingabe_container.setLayout(eingabe_gitter)
        haupt_gitter.addWidget(eingabe_container, 1, 0)
        haupt_gitter.setRowStretch(1, 4)

        self.json_zeichenkette_roh = ""
        self.xml_zeichenkette_formatiert = ""

        knopf_json_holen = QPushButton("JSON-Zeichenkette runterladen", eingabe_container)
        knopf_json_holen.setFixedWidth(300)
        knopf_json_holen.setObjectName("kn1")
        knopf_json_holen.clicked.connect(self.json_runterladen)
        knopf_json_anzeigen = QPushButton("JSON-Zeichenkette formatiert anzeigen", eingabe_container)
        knopf_json_anzeigen.setFixedWidth(300)
        knopf_json_anzeigen.setObjectName("kn2")
        knopf_json_anzeigen.clicked.connect(self.json_anzeigen)
        knopf_json_speichern = QPushButton("Formatiertes JSON-Dokument abspeichern", eingabe_container)
        knopf_json_speichern.setFixedWidth(300)
        knopf_json_speichern.clicked.connect(self.json_speichern)
        knopf_json_speichern.setObjectName("kn3")
        
        eingabe_gitter.addWidget(knopf_json_holen, 0, 0, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(knopf_json_anzeigen, 1, 0, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(knopf_json_speichern, 2, 0, QtCore.Qt.AlignCenter)
        
        knopf_xml_generieren = QPushButton("Formatierte XML-Zeichenkette erstellen", eingabe_container)
        knopf_xml_generieren.setFixedWidth(300)
        knopf_xml_generieren.setObjectName("kn4")
        knopf_xml_generieren.clicked.connect(self.xml_generieren)
        knopf_xml_anzeigen = QPushButton("XML-Zeichenkette anzeigen", eingabe_container)
        knopf_xml_anzeigen.setFixedWidth(300)
        knopf_xml_anzeigen.setObjectName("kn5")
        knopf_xml_anzeigen.clicked.connect(self.xml_anzeigen)
        knopf_xml_speichern = QPushButton("Formatiertes XML-Dokument abspeichern", eingabe_container)
        knopf_xml_speichern.setFixedWidth(300)
        knopf_xml_speichern.setObjectName("kn6")
        knopf_xml_speichern.clicked.connect(self.xml_speichern)
                
        eingabe_gitter.addWidget(knopf_xml_generieren, 0, 1, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(knopf_xml_anzeigen, 1, 1, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(knopf_xml_speichern, 2, 1, QtCore.Qt.AlignCenter)
                
        knopf_mysql = QPushButton("MySQL-Tabelle erstellen und Daten\naus dem XML-Dokument übertragen", eingabe_container)
        knopf_mysql.setObjectName("kn7")
        knopf_mysql.setMinimumHeight(54)
        knopf_mysql.setFixedWidth(300)
        knopf_mysql.clicked.connect(self.xml_auf_mysql)
        
        eingabe_gitter.addWidget(knopf_mysql, 0, 2, 2, 1, QtCore.Qt.AlignCenter)
        
        self.feld_datenbank = QLineEdit(eingabe_container)
        self.feld_datenbank.setFixedWidth(300)
        self.feld_datenbank.setPlaceholderText("Datenbank")
        self.feld_host = QLineEdit(eingabe_container)
        self.feld_host.setFixedWidth(300)
        self.feld_host.setPlaceholderText("Host")
        self.feld_benutzername = QLineEdit(eingabe_container)
        self.feld_benutzername.setFixedWidth(300)
        self.feld_benutzername.setPlaceholderText("Benutzername")
        self.feld_passwort = QLineEdit(eingabe_container)
        self.feld_passwort.setFixedWidth(300)
        self.feld_passwort.setPlaceholderText("Passwort")
        self.feld_passwort.setEchoMode(QLineEdit.Password)
        self.feld_pw_wiederholen = QLineEdit(eingabe_container)
        self.feld_pw_wiederholen.setFixedWidth(300)
        self.feld_pw_wiederholen.setPlaceholderText("Passwort wiederholen")
        self.feld_pw_wiederholen.setEchoMode(QLineEdit.Password)

        eingabe_gitter.addWidget(self.feld_datenbank, 2, 2, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(self.feld_host, 3, 2, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(self.feld_benutzername, 4, 2, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(self.feld_passwort, 5, 2, QtCore.Qt.AlignCenter)
        eingabe_gitter.addWidget(self.feld_pw_wiederholen, 6, 2, QtCore.Qt.AlignCenter)
              
        knopf_beenden = QPushButton("Beenden", eingabe_container)
        knopf_beenden.setMaximumWidth(80)
        knopf_beenden.setMinimumHeight(46)
        knopf_beenden.setObjectName("kn9")
        knopf_beenden.clicked.connect(self.beenden)
        eingabe_gitter.addWidget(knopf_beenden, 5, 3, 2, 1, QtCore.Qt.AlignRight)
             
    def json_runterladen(self):
        url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=71SnZJgtL8tphapVGACnoGKnkntE6odB"
        try:
            self.json_zeichenkette_roh = urllib.request.urlopen(url).read().decode("utf-8")
            QMessageBox.about(self, "Erfolg", "Die JSON-Zeichenkette wurde heruntergeladen!")
        except BaseException as err:
            QMessageBox.about(self, "Fehler", f"{err}")

    def json_anzeigen(self):
        if not self.json_zeichenkette_roh:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die JSON-Zeichenkette herunterladen!")
            return
        self.ausgabefeld.insertPlainText(json.dumps(json.loads(self.json_zeichenkette_roh), indent=4))
          
    def json_speichern(self):
        if not self.json_zeichenkette_roh:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die JSON-Zeichenkette herunterladen!")
            return
        try:
            (pfad, _) = QFileDialog.getSaveFileName(self, directory=f"{pathlib.Path().cwd()}", filter="JSON Dateien (*.json)")
            if not pfad:
                return
            with open(pfad, "w") as dokument:
                json.dump(json.loads(self.json_zeichenkette_roh), dokument, indent=4)
            QMessageBox.about(self, "Erfolg", "Das JSON-Dokument wurde gespeichert!")
        except BaseException as err:
            QMessageBox.about(self, "Fehler", f"{err}")            
    
    def xml_generieren(self):
        if not self.json_zeichenkette_roh:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die JSON-Zeichenkette herunterladen!")
            return

        # xml.sax.saxutils.escape ersetzt einige Symbole im JSON-String durch XML-Notation. Eine Schleife durchläuft 11005 
        # Unicode-Symbole und ersetzt diese bei Anwesenheit im JSON-String ebenfalls durch die entsprechende XML-Notation. 
        # Daraus wird anschließend ein Dictionary erstellt.          
        unicode_zu_xml = xml.sax.saxutils.escape(self.json_zeichenkette_roh)
        for _ in range(11005):
            if len(hex(_)[2:]) == 1:
                if "\\u000" + str(hex(_)[2:]) in unicode_zu_xml:
                    unicode_zu_xml = unicode_zu_xml.replace("\\u000" + str(hex(_)[2:]), "&#x" + str(hex(_)[2:]) + ";")
            elif len(hex(_)[2:]) == 2:
                if "\\u00" + str(hex(_)[2:]) in unicode_zu_xml:
                    unicode_zu_xml = unicode_zu_xml.replace("\\u00" + str(hex(_)[2:]), "&#x" + str(hex(_)[2:]) + ";")
            elif len(hex(_)[2:]) == 3:
                if "\\u0" + str(hex(_)[2:]) in unicode_zu_xml:
                    unicode_zu_xml = unicode_zu_xml.replace("\\u0" + str(hex(_)[2:]), "&#x" + str(hex(_)[2:]) + ";")
            elif len(hex(_)[2:]) == 4:
                if "\\u" + str(hex(_)[2:]) in unicode_zu_xml:
                    unicode_zu_xml = unicode_zu_xml.replace("\\u" + str(hex(_)[2:]), "&#x" + str(hex(_)[2:]) + ";")
        xml_notation_dic = json.loads(unicode_zu_xml)
        
        # Ein XML-String wird erstellt, mit einer Mischung aus map(), filter(), List-Comprehensions und Schleifen werden aus dem Dictionary mit XML-Notation 
        # die Schlüssel als Tags und die Werte als Inhalt dieser Zeichenkette hinzugefügt. So ensteht ein vollständiges XML-Dokument als String. 
        xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n<bestsellers>\n'
        xml_string += "".join(map(lambda k : f"\t<{k}>{xml_notation_dic[k]}</{k}>\n", filter(lambda k : k != "results", xml_notation_dic))) + "\t<results>\n"
        xml_string += "".join(map(lambda k : f"\t\t<{k}>{xml_notation_dic['results'][k]}</{k}>\n", filter(lambda k : k != "books" and k != "corrections", xml_notation_dic['results'])))
        xml_string += "\t\t<books>\n"
        for book in xml_notation_dic['results']['books']:
            xml_string += "".join(["\t\t\t<book>\n"] + [f"\t\t\t\t<{k}>{v}</{k}>\n" for k, v in book.items() if k != "isbns" and k != "buy_links" and k != "book_uri"])
            xml_string += "\t\t\t\t<isbns>\n"
            for isbns in book["isbns"]:
                xml_string += "".join(["\t\t\t\t\t<i10_i13>\n"] + [f"\t\t\t\t\t\t<{k}>{v}</{k}>\n" for k, v in isbns.items()] + ["\t\t\t\t\t</i10_i13>\n"])
            xml_string += "\t\t\t\t</isbns>\n\t\t\t\t<buy_links>\n"
            for isbns in book["buy_links"]:
                xml_string += "".join(["\t\t\t\t\t<store>\n"] + [f"\t\t\t\t\t\t<{k}>{v}</{k}>\n" for k, v in isbns.items()] + ["\t\t\t\t\t</store>\n"])
            xml_string += "\t\t\t\t</buy_links>\n" + "".join([f"\t\t\t\t\t<{k}>{v}</{k}>\n" for k, v in book.items() if k == "book_uri"] + ["\t\t\t</book>\n"])
        xml_string += "\t\t</books>\n"
        xml_string += "\t\t<corrections>\n" + "".join(map(lambda k : f"\t\t\t{xml_notation_dic['results']['corrections'][k]}, ", 
                                                          xml_notation_dic['results']['corrections'])) + "\t\t</corrections>\n"
        xml_string = xml_string.replace(", </corr", "</corr")
        xml_string += "\t</results>\n</bestsellers>"
        self.xml_zeichenkette_formatiert = xml_string
        QMessageBox.about(self, "Erfolg", "Die formatierte XML-Zeichenkette wurde erstellt!")
            
    def xml_anzeigen(self):
        if not self.xml_zeichenkette_formatiert:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die formatierte XML-Zeichenkette erstellen!")
            return
        self.ausgabefeld.setPlainText(self.xml_zeichenkette_formatiert.expandtabs(4))            

    def xml_speichern(self):
        if not self.xml_zeichenkette_formatiert:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die formatierte XML-Zeichenkette erstellen!")
            return
        try:
            (pfad, _) = QFileDialog.getSaveFileName(self, directory=f"{pathlib.Path().cwd()}", filter="XML Dateien (*.xml)")
            if not pfad:
                return
            with open(pfad, "wt") as dokument:
                dokument.write(self.xml_zeichenkette_formatiert)
            QMessageBox.about(self, "Erfolg", "Das XML-Dokument wurde gespeichert!")
        except BaseException as err:
            QMessageBox.about(self, "Fehler", f"{err}")
        
    def xml_auf_mysql(self):
        if not self.xml_zeichenkette_formatiert:
            QMessageBox.about(self, "Fehler", "Sie müssen zuerst die formatierte XML-Zeichenkette erstellen!")
            return
        elif not self.feld_datenbank.text() or not self.feld_host.text() or not self.feld_benutzername.text() or not self.feld_passwort.text() or not  self.feld_pw_wiederholen.text():
            QMessageBox.about(self, "Fehler", "Sie müssen alle Felder für die MySQL-Datenbank ausfüllen, in der die Tabelle erstellt werden soll!")
            return
        elif self.feld_passwort.text() != self.feld_pw_wiederholen.text():
            QMessageBox.about(self, "Fehler", "Die Passwörter sind nicht identisch!")
            return
        bestaetigung = QMessageBox()    
        bestaetigung.setIcon(QMessageBox.Question)
        bestaetigung.setWindowTitle("Eingaben überprüfen")
        bestaetigung.setText(f"Sind alle Eingaben richtig?\n\nDatenbank\t:      {self.feld_datenbank.text()}\nHost\t\t:      {self.feld_host.text()}\nBenutzername\t:      {self.feld_benutzername.text()}\n")
        bestaetigung.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if bestaetigung.exec() == QMessageBox.Cancel:
            return
        
        # Einfache Anführungszeichen im String werden ersetzt, da diese in SQL für den Datentyp VARCHAR reserviert sind. Aus dem Datum des XML-Dokumentes wird entsprechend 
        # formatiert der Tabellenname erstellt, anschließend wird der SQL-Befehl zur Erstellung an die ausgewählte Datenbank geschickt.
        wurzel = ET.fromstring(self.xml_zeichenkette_formatiert.replace("'", "&#x2019;"))
        erstellt = wurzel.findtext("last_modified")
        tabellen_titel = erstellt[0:erstellt.find('T')].replace("-", "_")
        try:
            verbindung = pymysql.connect(host=self.feld_host.text(), user=self.feld_benutzername.text(), password=self.feld_passwort.text(), db=self.feld_datenbank.text(), charset='utf8mb4')
            with verbindung.cursor() as cur:
                sql = f"""CREATE TABLE IF NOT EXISTS {tabellen_titel} 
                         (
                            rank TINYINT PRIMARY KEY, 
                            rank_last_week TINYINT, 
                            weeks_on_list SMALLINT,
                            asterisk INT,
                            dagger INT, 
                            primary_isbn10 VARCHAR(10) UNIQUE,
                            primary_isbn13 VARCHAR(13) UNIQUE,
                            publisher VARCHAR(150),
                            description VARCHAR(500),
                            price DECIMAL(5,2),
                            title VARCHAR(150),
                            author VARCHAR(150),
                            contributor VARCHAR(150),
                            contributor_note VARCHAR(500),
                            book_image VARCHAR(200),
                            book_image_width INT,
                            book_image_height INT,
                            amazon_product_url VARCHAR(200),
                            age_group VARCHAR(50),
                            book_review_link VARCHAR(200),
                            first_chapter_link VARCHAR(200),
                            sunday_review_link VARCHAR(200),
                            article_chapter_link VARCHAR(200),
                            book_uri VARCHAR(200)
                         );"""
                cur.execute(sql)
                verbindung.commit()

            # Die Schleife beginnt für jedes <book>-Element einen String mit dem SQL-Befehl INSERT INTO..., der dann von zwei internen Schleifen um die Spaltennamen und 
            # Werte ergänzt, und als Datensatz an die ausgewählte Datenbank geschickt wird.       
            with verbindung.cursor() as cur:
                for book in wurzel.iter("book"):
                    sql_string = f"INSERT INTO {tabellen_titel} ("
                    for elem in book:
                        if elem.tag != "isbns" and elem.tag != "buy_links":
                            sql_string += f"{elem.tag}, "
                    sql_string += ") VALUES ("
                    sql_string = sql_string.replace(", )", ")")              
                    for elem in book:
                        if elem.tag != "isbns" and elem.tag != "buy_links":
                            if elem.text == None:
                                sql_string += "NULL, "
                            elif elem.tag != "rank" and elem.tag != "rank_last_week" and elem.tag != "weeks_on_list" and elem.tag != "asterisk" and elem.tag != "dagger" and elem.tag != "price" and elem.tag != "book_image_width" and elem.tag != "book_image_height":
                                sql_string += f"'{elem.text}', "
                            else:
                                sql_string += f"{elem.text}, "
                    sql_string += ");"
                    sql_string = sql_string.replace(", );", ");")
                    cur.execute(sql_string)
                    verbindung.commit()
            QMessageBox.about(self, "Erfolg", f'Die Tabelle "{tabellen_titel}" ist erstellt und die Daten aus dem XML-Dokument übertragen!')    
        except BaseException as err:
            QMessageBox.about(self, "Fehler", f"{err}")
        
    def beenden(self):
        bestaetigung = QMessageBox()
        bestaetigung.setIcon(QMessageBox.Question)
        bestaetigung.setWindowTitle("Programm beenden")
        bestaetigung.setText("Das Programm wirklich beenden?")
        bestaetigung.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if bestaetigung.exec() == QMessageBox.Ok:
            app.quit()

style_sheet = '''
#fenster
{
    background-color: #fefeeb;
}
#kn1, #kn2, #kn3
{ 
    color: grey; 
    background-color: black;
    font-weight: 600;
    font-size: 10pt;
}
#kn4, #kn5, #kn6
{ 
    color: white; 
    background-color: #CF5C36;
    font-weight: 600;
    font-size: 10pt;
}
#kn7, #kn8
{ 
    color: orange; 
    background-color: #476A6F;
    font-weight: 600;
    font-size: 10pt;
}
#lbl1, #lbl2, #lbl3, #lbl4
{ 
    font-weight: 600;
    font-size: 10pt;
}
#kn9
{ 
    color: white; 
    background-color: #c42021;
    font-weight: 600;
    font-size: 10pt;
}

#ausgabe
{
    color: #222725; 
    background-color: #fefaf9;
    font-size: 10pt;
    font-family: monospace;
}
'''

app = QApplication(sys.argv)
app.setStyleSheet(style_sheet)
win = MeinHauptFenster()
win.show()
sys.exit(app.exec_())