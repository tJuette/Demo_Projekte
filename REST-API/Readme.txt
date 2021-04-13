Dieses Demonstrations-Projekt einer REST-API mit graphischer Benutzeroberfläche (PyQt5) ermöglicht es dem Benutzer: 
        
        - die NY Times - Bestseller - Liste, bestehend aus mehreren JSON-Objekten und -Arrays runterzuladen, formatiert 
          im Textfeld auszugeben und/oder abzuspeichern 
        
        - diese in XML umzuwandeln, im Textfeld auszugegeben und/oder abzuspeichern. Diese Datei ist wohlgeformt 
          und lässt sich auch im Browser öffnen. 
        
        - für die Informationen der 15 Bücher in dem XML-String eine Tabelle in einer anzugebenden MySQL-Datenbank zu 
          erstellen, und für jedes einen Datensatz zu übertragen. 


Der Hintergrund zu diesem Projekt ist folgender, Ende Juni 2020 wurde ich das erste Mal von einem potentiellen Ausbildungsbetrieb zur Probe-Arbeit eingeladen. Zuerst sollte ich in C# nur eine einfache GUI erstellen, ein Fenster mit Textfeld und Knopf, der von einer Partner-API eines namhaften Versandhändlers Verkaufsinformationen im JSON-Format abruft und im Textfeld ausgibt. Das war die Minimal-Anforderung, und dank WPF und Google(HttpRequest) leicht umzusetzen. Dann sollte ich die JSON-Datei "von Hand" in XML umwandeln und an die MSSQL-Datenbank der Firma übermitteln. Mit SQL hatte ich mich schon beschäftigt, und von der GUI Informationen an die Datenbank zu übermitteln war auch kein Problem, aber an den für mich zu dem Zeitpunkt unvertrauten JSON- und XML-Formaten scheiterte ich.

Mittlerweile kann ich aber auch mit diesen Formaten und generell der Verarbeitung von Zeichenketten recht gut umgehen, daher beschloss ich, mich ein wenig
mit PyQt5 zu beschäftigen und dieses Demo-Projekt umzusetzen. Den API-Key für die NY Times Bestseller hatte ich schon, und da das abgefragte Dokument ähnlich komplex ist wie die abgerufenen Verkaufsinformationen bei der Probe-Arbeit im Juni 2020, eigenete es sich ebensogut für eine Demo. 

Bei der Probe-Arbeit sollte die Übertragung dann im XML-Format stattfinden, da MySQL anders als MSSQL keine Option dafür anbietet, und es hier ohnehin nur darum 
geht den Umgang mit verschiedenen Formaten zu demonstrieren, habe ich auf jeglichen Bezug der Datenbank-Inhalte zu XML (etwa Tags und Inhalte als "Blob" in einem 
Feld abzuspeichern) verzichtet.

Bei der FP-Variante wurden die meisten Schleifen bei der Erstellung des XML-Strings durch List-Comprehensions ersetzt, was immerhin die 42 Zeilen Code auf 16 reduziert. Tatsächlich ist es auch möglich alle Schleifen durch List-Comprehensions zu ersetzen und den Abschnitt auf 8 Zeilen zu reduzieren, das Ergebnis ist aber sehr unleserlich:

xml_string='<?xml version="1.0" encoding="UTF-8"?>\n<bestsellers>\n'+''.join([f'\t<{k}>{v}</{k}>\n' for k, v in xml_notation_dic.items() if k != 'results'])+\
'\t<results>\n'+''.join([f'\t\t<{k}>{v}</{k}>\n' for k, v in xml_notation_dic['results'].items() if k not in ('books', 'corrections')])+'\t\t<books>\n'+\
''.join([''.join([3*'\t'+'<book>\n']+[4*'\t'+f'<{k}>{v}</{k}>\n' for k, v in book.items() if k not in ('isbns', 'buy_links', 'book_uri')]+[4*'\t'+'<isbns>\n']+
[5*'\t'+'<i10_i13>\n'+''.join([6*'\t'+f'<{k}>{v}</{k}>\n' for k, v in i.items()])+5*'\t'+'</i10_i13>\n' for i in book["isbns"]]+[4*'\t'+'</isbns>\n']+
[4*'\t'+'<buy_links>\n']+[5*'\t'+'<store>\n'+''.join([6*'\t'+f'<{k}>{v}</{k}>\n' for k, v in i.items()])+5*'\t'+'</store>\n' for i in book['buy_links']]+
[4*'\t'+'</buy_links>\n']+[4*'\t'+f'<{k}>{v}</{k}>\n' for k, v in book.items() if k == 'book_uri']+[3*'\t'+'</book>\n']) for book in 
xml_notation_dic['results']['books']])+'\t\t</books>\n'+''.join(['\t\t<corrections>\n']+[3*'\t'+f"{i}\n" for i in xml_notation_dic['results']['corrections']]+\
['\t\t</corrections>\n'])+'\t</results>\n</bestsellers>'

