import json


def format_recipes(list_recipe: []):
    message = ""

    for recipe in list_recipe:
        message += str(recipe[1]).capitalize() + "\n\n"
        #
        # ingredients = json.loads(recipe[2])
        # measurements = json.loads(recipe[3])
        #
        # for i in range(len(ingredients)):
        #     message += ingredients[i] + "\t"
        #     message += measurements[i] + "\n"

    return message


def single_recipe_formater(recipe):
    message = ""

    ingredients = json.loads(recipe[2])
    measurements = json.loads(recipe[3])

    for i in range(len(ingredients)):
        message += ingredients[i] + "\t"
        message += measurements[i] + "\n"

    return message
