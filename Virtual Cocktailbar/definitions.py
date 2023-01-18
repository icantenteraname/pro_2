import json


def safe(name, ingredients, instructions, description, tools):
    new_recipe = {"name": name, "ingredients": ingredients, "instructions": instructions, "description": description, "tools": tools}
    with open("database_recipes.json", "r+", encoding="UTF-8") as file:
        file_data = json.load(file)  # load existing data
        file_data[name] = new_recipe  # add new dictionary entry
        file.seek(0)  # sets file's current position at offset otherwise the JSON update is only appendet at the end (assumption: seek sets the index to 0 and the data is filled up from index[0])
        json.dump(file_data, file, indent=2, ensure_ascii=False)  # convert back to JSON, 'Umlaute' not in ascii
    return


def recipes_saved_open():  # hier wird die Datei mit den gespeicherten Rezepten geöffnet
    with open('database_recipes.json', 'r', encoding='utf-8') as database:
        recipes_saved = json.load(database)
    return recipes_saved


def find_with_ingredient(data, ingredients):
    found = []
    for _, row in data.iterrows():  # iterate over rows
        needed = row['ingredients'].split(',')  # split up all ingredients so that they are individual
        for i in needed:  # for each needed ingredient
            f = False  # f is only a placeholder
            for ing in ingredients:  # check if any of the user ingredients match
                if ing.lower() in i.lower():  # case insensitivity so that if white wine is entered a recipe with dry white wine is also shown
                    f = True
                    break
            if not f:
                break
        if not f:
            continue
        found.append(row['name'])  # add found drink
    return found
