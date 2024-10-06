from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def recipe_inline_button(recipe_list: []):
    keys = []

    for recipe in recipe_list:
        keys.append([InlineKeyboardButton(text=str(recipe[1]).capitalize(), callback_data=recipe[0])])

    return InlineKeyboardMarkup(keys)


def recipe_saver(recipe):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="Add to favourite", callback_data=recipe)], ])


def recipe_deleter(recipe):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="Remove from saved", callback_data=recipe)], ])
