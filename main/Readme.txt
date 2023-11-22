Hi,

Die Datei die für die Pfadberechnug und Darstellung ausgefürt werden muss ist PyGame.py .

Die Beobachterstartposition kannst du in Zeile 257(der PyGame.py datei) ändern.  Steht im Moment auf [1,12,0] 

Anmerkung zu den Koordinaten der Punkt (0;0) ist in der linken oberen Ecke und die y-Achse zeigt nach unten.
Dies ist der Kompatibilität mit den fertigen TSP und A* Implementationen geschuldet.

Die Sichtweite des Beobachters kannst du in Zeile 264(der PyGame.py datei) einsetellen.   Steht im Moment auf 25

Die "Welt"  wird ab Zeile 128(der PyGame.py datei) via den Methoden aus Worldcreation.py erstellt.
Wenn du also die Welt verändern möchtest kannst du dich da orientieren.

Falls du die Ergebnisse der unfertigen Verbesserung sehen willst musst du in der Datei pathwitklos.py in
Zeile 368 eine # vor die drei """-Zeichen setzen dann dürfte der entsprechende Programmteil nicht mehr
auskomentiert sein. Das nartürlich speichern und PyGame.py erneut ausführen.

Random.py ist die Ausführung der Tests und die Diagramme dazu werden in plotfortesting.py erstellt.
Also  plotfortesting.py ausführen wenn du die Diagramme sehen möchstest.