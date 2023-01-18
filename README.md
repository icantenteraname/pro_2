# Virtual Cocktailbar
## Problemstellung / Motivation
Das Programm "Virtual Cocktailbar" soll den Nutzern Rezepte für alkoholische Getränke vorschlagen, die sie Zuhause einfach nachmachen können.
Oftmals weiss man nicht genau, was man trinken soll und greift immer wieder zum gleichen Cocktail. Dieses Problem soll dieses Programm lösen und es soll den eigenen Cocktailhorizont erweitern.

Ich selbst mixe sehr gerne Cocktails und besitze eine voll ausgestattete Bar zuhause. Es ist mir leider nur immer zu dumm lange nach Rezepten für neue Drinks zu suchen und so mache ich mehr oder weniger immer die gleichen Drinks. Dieses Programm hilft mir dabei meine Ressourcen so gut als möglich zu verwenden und mit geringem Zeitaufwand neue Rezepte zu entdecken.

## Betrieb
Als zusatzpakete werden in dem Code für die Virtual Cocktailbar die im Unterricht installierten Pandas und Plotly verwendet. Um den Code korrekt ausführen zu können müssen diese Pakete vorhanden sein.

## Benutzung
Die Hauptfunktion der virtuellen Cocktailbar ist die Ausgabe von Rezepten basierend auf den verfügbaren Zutaten, welche vom Nutzer angegeben wird. Mit dem Rezeptevorschlag soll auch gleich eine Mix-Anleitung angezeigt werden und es soll ersichtlich sein, welche Mixing-Tools man dafür benötigt.

Zusätzlich besteht die Option, dass man die das Rezeptbuch der Cocktails erweitern kann und eigene Rezepte hinzufügen kann. So ist sichergestellt, dass einem die Cocktails nicht ausgehen werden, da man die Datenbank selbst erweitern kann. Auf der Home-Seite ist stets eine Liste vorhanden, die alle Rezepte aus der Datenbank anzeigt. So besteht zudem die Möglichkeit, dass man den Prozess umdreht und sich nicht von den Zutaten Zuhause, sondern von den verschiedenen Rezepten inspirieren lässt.

## Architektur
### Ablaufdiagramm
<img src="C:\Users\dittl\Documents\DBM_PRO2_HS22\pro2_projekt\Virtual Cocktailbar\images\Ablaufdiagramm Virtual Cocktailbar.png"/>

## Ungelöste/unbearbeitete Probleme
Momentan werden nur Rezepte angezeigt, für die mal alle Zutaten bereits besitzt. Eine nützliche Funktion wäre gewesen, wenn man auch Rezepte hätte anzeigen können, für die man noch nicht alle Zutaten besitzt. Spannend wäre gewesen, wenn es diese Zutaten auch noch speziell hervorgehoben hätte und man aus diesen dann eine Einkaufsliste erstellen könnte.

Ausserdem wäre es für die Startseite nützlich, wenn sich alle Rezepte automatisch alphabetisch sortieren, damit man ein spezifisches Rezept schneller findet.

Ein leider nur halb gelöstes Problem erscheint bei der Eingabe von Zutaten zur Suche für das passende Rezept. Die Liste der Zutaten wird erst bereinigt, wenn man in eine andere Seite in der Navigation hinein geht. Wenn man auf der Search Recipe Seite bleibt, wird es einem die Drinks basierend auf allen bisher eingegebenen Zutaten ausgeben.
