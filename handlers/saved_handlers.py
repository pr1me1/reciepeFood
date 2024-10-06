import asyncio

from telegram import Update
from telegram.ext import CallbackContext

from constants import states
from constants.admins import ADMINS
from database.reciepe_table import get_single_recipe
from database.user_table import delete_favourite
from keyboards.replies import back_button, main_reply_keyboard
from utils.recipe_inline_formater import recipe_saver, recipe_deleter
from utils.recipe_post_formater import single_recipe_formater


# callback saved
def saved_callback_handler(update: Update, context: CallbackContext):
    recipe_id = update.callback_query.data
    result = asyncio.run(get_single_recipe(recipe_id))
    update.callback_query.answer()

    update.callback_query.message.reply_text(text=single_recipe_formater(result),
                                             reply_markup=recipe_deleter(recipe_id))

    return states.SAVED_MANAGER


# message handler
def saved_message_handler(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", reply_markup=back_button())
        return states.SAVED

    if update.message.text == "Back":
        update.message.reply_text("Click one of the buttons in the below",
                                  reply_markup=main_reply_keyboard(ADMINS.__contains__(update.message.from_user.id)))
        return states.MENU


# callback saved manager
def saved_manager_callback_handler(update: Update, context: CallbackContext):
    recipe_id = update.callback_query.data
    asyncio.run(delete_favourite(user_id=update.callback_query.from_user.id, recipe_id=recipe_id))
    update.callback_query.answer("Recipe has been successfully removed from your favourites list")
    update.callback_query.message.delete()
    return states.SAVED


def saved_manager_message_handler(update: Update, context: CallbackContext):
    if not update.message.text:
        update.message.reply_text("Please enter info in text version", reply_markup=back_button())
        return states.SAVED_MANAGER

    if update.message.text == "Back":
        # context.bot.delete_message(chat_id=update.callback_query.message.chat_id,
        #                            message_id=update.callback_query.message.message_id)
        update.message.reply_text("Click one of the buttons in the below",
                                  reply_markup=main_reply_keyboard(ADMINS.__contains__(update.message.from_user.id)))
        return states.MENU
