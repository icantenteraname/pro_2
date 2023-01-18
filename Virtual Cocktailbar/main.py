from flask import Flask, render_template, request, redirect
import json
import plotly.express as px
import plotly
import pandas as pd
from definitions import safe, find_with_ingredient, recipes_saved_open

data = pd.read_json('database_recipes.json')  # read JSON file
data = data.transpose()  # swap rows and columns


app = Flask("Virtual Cocktailbar")

list_of_ingredients = []


# display all recipes
@app.route("/")
def my_recipe_book():
    list_of_ingredients = []  # every time my recipe book is visited this list is cleared
    return render_template("recipe_book.html", data=data.transpose(), seitentitel="My Recipe Book")


# add new recipe to database
@app.route("/add", methods=["GET", "POST"])
def add_new_recipe():
    list_of_ingredients = []  # every time my recipe book is visited this list is cleared
    if request.method == "GET":
        return render_template("recipe_form.html", seitentitel="Add Recipe")

    if request.method == "POST":
        if "safe" in request.form:  # check if a new recipe has been submitted
            name = request.form.get("new_name")
            ingredients = request.form.get("new_ingredients")
            instructions = request.form.get("new_instructions")
            description = request.form.get("new_description")
            tools = request.form.get("new_tools")
            safe(name, ingredients, instructions, description, tools)  # recipe to JSON file
            data = pd.read_json('database_recipes.json')  # read JSON file again with new recipe in it
            data = data.transpose()  # swap rows and columns
        return redirect("/add")


# Evaluation
@app.route("/chart")
def chart():
    list_of_ingredients = []  # every time my recipe book is visited this list is cleared
    # hier wird die Funktion um die Datenbank zu öffnen, ausgeführt und die Daten werden umgewandelt, damit diese in einem Balkendiagramm aufgezeichnet werden
    evaluation_saved = recipes_saved_open()
    # leeres Dictionary wird erstellt
    counts = {}
    # for-loop für alle values
    for _, entry in evaluation_saved.items():
        # name der Aktivität wird genommen und in Variable items umgewandelt
        items = entry.get("description")
        # entered_ingredient = str(entered_ingredient)
        # items = entered_ingredient.split(",")
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
    return render_template('evaluation.html', viz_div=div, seitentitel="Evaluation")


# search recipe with available ingredients
@app.route("/search", methods=["GET", "POST"])
def search():
    temp = data  # dataset of all recipes with my ingredients
    if request.method == 'POST':
        if "ingredients" in request.form:  # check if an ingredient has been entered
            entered_ingredients = request.form.get('ingredients').split(', ')  # split ingredients so that every ingredient can be checked alone
            for ing in entered_ingredients:
                list_of_ingredients.append(ing)  # entered ingredients is added to list with all user ingredients
            list_of_drinks = find_with_ingredient(data, list_of_ingredients)  # get list of all drinks with no more than the user ingredients
            temp = data[data['name'].isin(list_of_drinks)]  # get the reducd database (every recipe with a name out of the list of drinks)
    return render_template('search.html', data=temp.transpose(), seitentitel="Search Recipe")  # display the reduced database


if __name__ == "__main__":
    app.run(debug=True, port=5000)
