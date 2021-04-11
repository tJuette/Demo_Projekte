# Demo_Projekte
Mir wurden am 16 Dezember 2020 von der Firma, bei der Mitte Oktober ein Vorstellungsgespräch stattgefunden hatte, 
zwei Aufgaben gestellt und vier Stunden Zeit gegeben um meine Quellcodes einzuschicken. Anschließend gab es eine 
Webex-Konferenz in der ich meine Lösungen vorstellte und erklärte. 

Das Ziel der ersten Aufgabe war es, ein Kommandozeilen-Programm zu entwerfen, dass vom Benutzer zwei Ziffern und 
das Symbol für eine der vier Grundrechenarten annimmt und das Ergebnis ausgibt, wobei nur Divisonen ohne Rest 
möglich sein sollten. Ein Programm welches lief bis der Benutzer es abbrach wurde nicht gefordert.

Bei der zweiten Aufgabe sollte im Terminal ein Menü erscheinen welches dem Benutzer die Auswahl zwischen vier
Wechselkursen oder dem Beenden des Programms per Nummerneingabe gibt. Es sollten nur Ganzzahlen für die 
Beträge eingegeben werden können, die dann entsprechend der Auswahl des Benutzers umrechnet werden. Ursprünglich 
befanden sich in jeder der vier Auswahlmöglichkeiten dieselben ineinander verschachtelten Schleifen, womit ich 
das DRY-Prinzip verletzte. Da ich noch Zeit hatte habe ich diese in zwei Funktionen ausgelagert, insgesamt
war ich mit dem Ergebnis zufrieden. Allerdings habe ich eine Eingabe von Nichts (=None) nicht berücksichtigt und
noch einige Artefakte von der ursrpünglichen Version drin gelassen, dies wurde in der verbesserten Variante 
korrigiert.

