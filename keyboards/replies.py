from telegram import ReplyKeyboardMarkup, KeyboardButton


def main_reply_keyboard(is_admin=False):
    if is_admin:
        return ReplyKeyboardMarkup(
            [
                [KeyboardButton(text="Foods list")],
                [KeyboardButton(text="Add recipe")]
            ],
            resize_keyboard=True,
        )
    else:
        return ReplyKeyboardMarkup(
            [
                [KeyboardButton(text="Foods list")],
                [KeyboardButton(text="Saved ones")]
            ],
            resize_keyboard=True,
        )


def done_button():
    return ReplyKeyboardMarkup([[KeyboardButton(text="Done")]], resize_keyboard=True, )


def back_button():
    return ReplyKeyboardMarkup([[KeyboardButton(text="Back")]], resize_keyboard=True, )
