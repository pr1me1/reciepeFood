import asyncio

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from constants import states
from constants.admins import ADMINS
from database.reciepe_table import get_all_recipes
from database.user_table import get_favourites
from keyboards.replies import main_reply_keyboard, back_button
from utils.recipe_inline_formater import recipe_inline_button
from utils.recipe_post_formater import format_recipes


# start
def start_bot(update: Update, context: CallbackContext):
    update.message.reply_text("Hi you've used our bot before",
                              reply_markup=main_reply_keyboard(ADMINS.__contains__(update.message.from_user.id)))

    return states.MENU


# menu
def menu_handler(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", reply_markup=main_reply_keyboard())
        return states.MENU

    if update.message.text == "Foods list":
        update.message.reply_text("Here all the recipes that added by admins:", reply_markup=back_button())
        recipes = asyncio.run(get_all_recipes())

        update.message.reply_text(text=format_recipes(recipes), reply_markup=recipe_inline_button(recipes))
        return states.RECIPES

    if update.message.text == "Add recipe":
        update.message.reply_text(
            "You are adding recipe to database. You must firstly add name and measurement of ingredient of recipe. After adding them all click the button \"Done\" in the below",
            reply_markup=ReplyKeyboardRemove())
        return states.NAMING_RECIPE

    if update.message.text == "Saved ones":
        favs = asyncio.run(get_favourites(update.message.from_user.id))
        if not favs:
            update.message.reply_text("Your favourite list is empty", reply_markup=main_reply_keyboard())
            return states.MENU
        else:
            update.message.reply_text("Here your favorite recipes: ", reply_markup=back_button())
            update.message.reply_text(format_recipes(favs), reply_markup=recipe_inline_button(favs))
            return states.SAVED
