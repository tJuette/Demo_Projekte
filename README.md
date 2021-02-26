# Demo_Projekte
Dieses Demonstrations-Projekt einer REST-API mit graphischer Benutzeroberfläche (PyQt5) ermöglicht es dem Benutzer: 
        
        - die NY Times - Bestseller - Liste in JSON runterzuladen, im Textfeld auszugeben und/oder abzuspeichern 
        
        - diese in XML umzuwandeln, im Textfeld auszugegeben und/oder abzuspeichern. Diese Datei ist wohlgeformt 
          und lässt sich auch im Browser öffnen. 
        
        - für die Informationen der 15 Bücher in dem XML-String eine Tabelle in einer anzugebenden MySQL-Datenbank zu 
          erstellen, und diese dorthin zu übertragen. 


Der Hintergrund zu diesem Projekt ist folgender, Ende Juni 2020 wurde ich das erste Mal von einem potentiellen Ausbildungsbetrieb zur Probe-Arbeit eingeladen. Zuerst 
sollte ich in C# nur eine einfache GUI erstellen, ein Fenster mit Textfeld und Knopf, der von einer Partner-API eines namhaften Versandhändlers Verkaufsinformationen 
im JSON-Format abruft und im Textfeld ausgibt. Das war die Minimal-Anforderung, und dank WPF und Google(HttpRequest) leicht umzusetzen. Dann sollte ich die JSON-Datei "von Hand" in XML umwandeln und an die MSSQL-Datenbank der Firma übermitteln. Mit SQL hatte ich mich schon beschäftigt, und von der GUI Informationen an die Datenbank 
zu übermitteln war auch kein Problem, aber an den für mich zu dem Zeitpunkt unvertrauten JSON- und XML-Formaten scheiterte ich.

Mittlerweile kann ich aber auch mit diesen Formaten und generell der Verarbeitung von Zeichenketten recht gut umgehen, daher beschloss ich, mich ein wenig
mit PyQt5 zu beschäftigen und dieses Demo-Projekt umzusetzen.

Bei der Probe-Arbeit sollte die Übertragung dann im XML-Format stattfinden, da MySQL anders als MSSQL keine Option dafür anbietet, und es hier ohnehin nur darum 
geht den Umgang mit verschiedenen Formaten zu demonstrieren, habe ich auf jeglichen Bezug der Datenbank-Inhalte zu XML (etwa Tags und Inhalte als "Blob" in einem 
Feld abzuspeichern) verzichtet. Fertig gestellt wurde es am 26.02.2020.

