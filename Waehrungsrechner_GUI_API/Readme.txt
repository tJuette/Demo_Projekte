Der alte Währungsrechner funktioniert nicht mehr, da man sich für die API jetzt doch registrieren muss. Die neue FP-Variante unterscheidet sich von der anderen nur dadurch, dass die Schleifen durch map()- und filter()-Funktionen ersetzt wurden. Dies spart hier nur vier Zeilen Code, aber immerhin.

Jedenfalls wird er nach wie vor mit dem Euro als Basis-Währung gestartet, er kann in alle Währungen umgerechnet werden oder alle Währungen in ihn. Die Sätze anderer Währungen werden nur bei Bedarf einmal abgerufen und in einem Dictionary gepspeichert, um Traffic zu reduzieren. 
