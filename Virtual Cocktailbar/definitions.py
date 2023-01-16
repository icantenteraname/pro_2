import json
import pandas as pd

"""
def read_out():
    with open("database_recipes.json", "r") as open_file:  # geht mit json datenbank nicht
        content = open_file.read()
    return content


def load_recipes():
    recipes = read_out()
    recipes_list = recipes.split("\n")
    new_list = []
    for entry in recipes_list:
        name, instructions, ingredients, description, tools = entry.split(",")
        new_list.append([name, ingredients, instructions, description, tools])
    return new_list
"""

def safe(name, ingredients, instructions, description, tools):
    new_recipe = {"name": name, "ingredients": ingredients, "instructions": instructions, "description": description, "tools": tools}
    with open("database_recipes.json", "r+", encoding="UTF-8") as file:
        file_data = json.load(file)  # load existing data
        file_data[name] = new_recipe  # add new dictionary entry
        file.seek(0)  # Sets file's current position at offset
        json.dump(file_data, file, indent=2, ensure_ascii=False)  # convert back to JSON, 'Umlaute' not in ascii
    return

def recipes_saved_open():  # hier wird die Datei mit den gespeicherten Rezepten geöffnet
    try:
        with open('database_recipes.json', 'r', encoding='utf-8') as database:
            # Inhalt der Datenbank wird als Dictionary datenbank_vorschlaege gespeichert.
            recipes_saved = json.load(database)
    except:
        # wenn kein Eintrag, wird es als leeres Dictionary gespeichert
        recipes_saved = {}

    return recipes_saved

"""
def read_recipes(drink_name):
    with open("database_recipes.json") as csv_file:
        all_recipes = csv.DictReader(csv_file)  # resource: https://blog.finxter.com/convert-csv-to-dictionary-in-python/#:~:text=The%20best%20way%20to%20convert,to%20the%20specific%20row%20value.
        if drink_name in all_recipes.key():
            return all_recipes.get(drink_name)
        else:
            return "This drink is not in the book."
"""

def find_with_ingredient(data, ingredients):
    found = []
    for _, row in data.iterrows():  # iterate over rows
        needed = row['ingredients'].split(',')  # split up all ingredients
        for i in needed:  # for each needed ingredient...
            f = False
            for ing in ingredients:  # we check if any of our ingredients match
                if ing.lower() in i.lower():  # lower() method for case insensitivity
                    f = True
                    break
            if not f:
                break
        if not f:
            continue
        found.append(row['name'])  # add found drink
    return found
