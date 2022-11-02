import random

from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/hello')
def hello_world():
    auswahl = ["Fabian", "Markus", "Franz", "Mandy"]
    ausgewaehlter_name = random.choice(auswahl)
    return render_template('hello.html', name=ausgewaehlter_name)

@app.route('/greet_all')
def greet_all():
    namen = ["Anna", "Hannah", "Milena", "Sabrina", "Tamara"]
    return render_template('hello_all.html', alle_namen=namen)

@app.route('/hallo') #app.route ist URL, die ausgeführt wird
def hallo_welt():
    unsere_namen = ["Anna", "Hannah", "Milena", "Sabrina", "Tamara"]
    auswahl_unsere_namen = random.choice(unsere_namen)
    return render_template('hello.html', neue_namen=auswahl_unsere_namen) #das, was auf der Webseite ausgegeben wird


if __name__ == "__main__":
    app.run(debug=True, port=5000)