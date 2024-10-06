import asyncio

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from constants import states
from constants.constants import INGREDIENTS, MEASUREMENTS
from database.reciepe_table import add_recipe
from keyboards.replies import done_button, main_reply_keyboard


# give name
def giving_name_to_recipe(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", )
        return states.NAMING_RECIPE

    context.user_data['name'] = update.message.text

    ingredient = context.user_data.get(INGREDIENTS, [])

    if not ingredient:
        update.message.reply_text("Please enter first ingredient of recipe", )
    else:
        update.message.reply_text("Please enter next ingredient of recipe", reply_markup=done_button())

    return states.ADD_INGREDIENT


# add ingredient
def add_ingredient_to_recipe(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", )
        return states.ADD_INGREDIENT

    ingredient = context.user_data.get(INGREDIENTS, [])

    if update.message.text == "Done":
        name = context.user_data['name']
        meas = context.user_data[MEASUREMENTS]
        asyncio.run(add_recipe(name=name, ingredients=ingredient, measurement=meas))
        update.message.reply_text(name + " has been successfully added to recipe list",
                                  reply_markup=main_reply_keyboard())
        return states.MENU

    else:
        ingredient.append(update.message.text)
        context.user_data[INGREDIENTS] = ingredient

        update.message.reply_text("Now add quantity of the ingredient that you entered before to recipe",
                                  reply_markup=ReplyKeyboardRemove())
        return states.ADD_MEASUREMENT


# add meas
def add_measurement_to_recipe(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", )
        return states.ADD_MEASUREMENT

    meas = context.user_data.get(MEASUREMENTS, [])
    meas.append(update.message.text)

    context.user_data[MEASUREMENTS] = meas

    update.message.reply_text("Please enter next ingredient of recipe", reply_markup=done_button())

    return states.ADD_INGREDIENT
