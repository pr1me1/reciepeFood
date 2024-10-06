import sqlite3

import aiosqlite

from constants.constants import FOO_DATABASE_NAME, USER, FOOD


async def add_favourite(user_id, recipe_id):
    async with aiosqlite.connect(FOO_DATABASE_NAME) as db:
        await db.execute(f"insert into {USER}(telegram_id, recipe_id) values ('{user_id}', '{recipe_id}')")
        await db.commit()


async def get_favourites(user_id):
    async with aiosqlite.connect(FOO_DATABASE_NAME) as con:
        result = await con.execute(
            f"select {FOOD}.id, {FOOD}.name, {FOOD}.ingredient, {FOOD}.measurement from {USER} JOIN {FOOD} on {USER}.recipe_id = {FOOD}.id where {USER}.telegram_id = '{user_id}'")
        result = await result.fetchall()
        await con.commit()

    return result


async def delete_favourite(user_id, recipe_id):
    async with aiosqlite.connect(FOO_DATABASE_NAME) as con:
        result = await con.execute(f"delete from {USER} where recipe_id = '{recipe_id}' and telegram_id = '{user_id}'")
        await con.commit()
