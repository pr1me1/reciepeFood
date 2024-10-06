from telegram import Bot
from telegram.ext import Dispatcher, ConversationHandler, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handlers.add_recipe_handler import *
from handlers.main_handler import *
from handlers.recipes_handler import *
from handlers.saved_handlers import *

bot = Bot(token='7338253696:AAHksCn6_vL9Y7wuWIIId503nhvYvkXqSCw')
dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CommandHandler("start", start_bot)
        ],
        states={
            states.MENU: [
                MessageHandler(Filters.text & ~Filters.command, menu_handler)
            ],
            states.NAMING_RECIPE: [
                MessageHandler(Filters.text & ~Filters.command, giving_name_to_recipe)
            ],
            states.ADD_INGREDIENT: [
                MessageHandler(Filters.text & ~Filters.command, add_ingredient_to_recipe)
            ],
            states.ADD_MEASUREMENT: [
                MessageHandler(Filters.text & ~Filters.command, add_measurement_to_recipe)
            ],
            states.RECIPES: [
                CallbackQueryHandler(get_recipes_callback_handler),
                MessageHandler(Filters.text & ~Filters.command, get_recipes_message_handler)
            ],
            states.MANAGE_RECIPE: [
                CallbackQueryHandler(manage_recipe_callback_handler),
                MessageHandler(Filters.text & ~Filters.command, manage_recipe_message_handler)
            ],
            states.SAVED: [
                CallbackQueryHandler(saved_callback_handler),
                MessageHandler(Filters.text & ~Filters.command, saved_message_handler)
            ],
            states.SAVED_MANAGER: [
                CallbackQueryHandler(saved_manager_callback_handler),
                MessageHandler(Filters.text & ~Filters.command, saved_manager_message_handler)
            ]

        },
        fallbacks=[]
    )
)
