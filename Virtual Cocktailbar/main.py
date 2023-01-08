from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Virtual Cocktailbar")

@app.route('/', methods=["GET", "POST"])

def add_new_recipe():
 if request.method == "GET":
  return render_template("recipe_form.html")

 if request.method == "POST": #Daten werden abgeschickt (welche Zutaten ich hab)
  ingredients_in_stock = request.form["ingredients"]
  with open("database_recipes.json") as datei:
   suggestions = json.load(datei)



if __name__ == "__main__":
 app.run(debug=True, port=5000)