import asyncio

from telegram import Update
from telegram.ext import CallbackContext

from constants import states
from database.reciepe_table import get_single_recipe
from database.user_table import add_favourite
from keyboards.replies import back_button, main_reply_keyboard
from utils.recipe_inline_formater import recipe_saver
from utils.recipe_post_formater import single_recipe_formater


# callback recipe
def get_recipes_callback_handler(update: Update, context: CallbackContext):
    recipe_id = update.callback_query.data
    result = asyncio.run(get_single_recipe(recipe_id))
    update.callback_query.answer()

    update.callback_query.message.reply_text(text=single_recipe_formater(result),
                                             reply_markup=recipe_saver(recipe_id))

    return states.MANAGE_RECIPE


# message recipe
def get_recipes_message_handler(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", reply_markup=back_button())
        return states.RECIPES

    if update.message.text == "Back":
        update.message.reply_text("Click one of the buttons in the below", reply_markup=main_reply_keyboard())
        return states.MENU


# callback manage recipe
def manage_recipe_callback_handler(update: Update, context: CallbackContext):
    recipe_id = update.callback_query.data
    asyncio.run(add_favourite(user_id=update.callback_query.from_user.id, recipe_id=recipe_id))
    update.callback_query.answer("Recipe has been successfully added to your favourites list")
    update.callback_query.message.delete()
    return states.RECIPES


# message manage recipe
def manage_recipe_message_handler(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", reply_markup=back_button())
        return states.MANAGE_RECIPE

    if update.message.text == "Back":
        # context.bot.delete_message(chat_id=update.callback_query.message.chat_id,
        #                            message_id=update.callback_query.message.message_id)
        update.message.reply_text("Click one of the buttons in the below", reply_markup=main_reply_keyboard())
        return states.MENU
