from flask import Flask, render_template, request, redirect, url_for
import json
import plotly.express as px
import plotly
from plotly.offline import plot
import pandas as pd
from definitions import safe, find_with_ingredient, recipes_saved_open

data = pd.read_json('database_recipes.json')  # read JSON file
data = data.transpose()  # swap rows and columns

# wenn es nicht mehr geht und man abgeben muss, einfach Problem in Kommentar schildern und erklären

app = Flask("Virtual Cocktailbar")

list_of_ingredients = []


# Vorhandene Rezepte anzeigen
@app.route("/")
def my_recipe_book():
    return render_template("recipe_book.html", data=data.transpose(), seitentitel="My Recipe Book")  # simply display the table


# Neues Rezept hinzufügen
@app.route("/add", methods=["GET", "POST"])
def add_new_recipe():
    if request.method == "GET":
        return render_template("recipe_form.html", seitentitel="Add Recipe")

    if request.method == "POST":
        if "safe" in request.form:  # check if a new recipe has been submitted
            name = request.form.get("new_name")  # get text entries
            ingredients = request.form.get("new_ingredients")
            instructions = request.form.get("new_instructions")
            description = request.form.get("new_description")
            tools = request.form.get("new_tools")
            safe(name, ingredients, instructions, description, tools)  # recipe to JSON file
            data = pd.read_json('database_recipes.json')  # read JSON file
            data = data.transpose()  # swap rows and columns
        return redirect("/add")


# Auswertung
@app.route("/chart")
def chart():
    # hier wird die Funktion um die Datenbank zu öffnen, ausgeführt und die Daten werden umgewandelt, damit diese in einem Balkendiagramm aufgezeichnet werden
    evaluation_saved = recipes_saved_open()
    # leeres Dictionary wird erstellt
    counts = {}
    # for-loop für alle values
    for _, entry in evaluation_saved.items():
        # name der Aktivität wird genommen und in Variable items umgewandelt
        entered_ingredient = entry.get("ingredient")
        entered_ingredient = str(entered_ingredient)
        items = entered_ingredient.split(",")
        # for loop für alle items wird ausgeführt
        for item in items:
            # wenn item schon in counts ist, dann wird die Anzahl des items um eins erhöht
            if item in counts:
                counts[item] += 1
            # wenn es das item noch nicht gibt, dann wird das item hinzugefügt und die Anzahl ist eins
            else:
                counts[item] = 1

    # counts Liste sieht so aus und diese werden dann in Balkendiagramm angezeigt
    # counts = {'Wandern Calanda': 2, 'Wandern xyz': 10}
    fig = px.bar(x=list(counts.keys()), y=list(counts.values()))
    # mit plotly.io.to_html wird die Grafik als div angezeigt.
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)

    # auswertung HTML wird angezeigt und div wird mitgegeben.
    return render_template('evaluation.html', viz_div=div)


@app.route("/search", methods=["GET", "POST"])
def search():
    temp = data
    if request.method == 'POST':
        if "ingredients" in request.form:  # check if an ingredient has been entered...
            list_of_ingredients.append(request.form.get('ingredients'))  # if so, add it to the list
            list_of_drinks = find_with_ingredient(data, list_of_ingredients)  # get list of all drinks with no more than these ingredients
            temp = data[data['name'].isin(list_of_drinks)]  # get the reduced database
    return render_template('search.html', data=temp.transpose(), seitentitel="Search Recipe")  # display the reduced database


"""
            for key in all_recipes:
                if (all_recipes[key] == drink_name):
                    return(all_recipes[key])
                else:
                    return("This recipe is not in the book.")


    if request.method == "POST":
        drink_name = request.form['drink_name']
        print(f"Request Form drink_name: {drink_name}")
        all_recipes = read_recipes()
        for drink_name in all_recipes.keys():
            return(all_recipes.values())
"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)
