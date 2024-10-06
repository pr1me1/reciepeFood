import json

import aiosqlite

from constants.constants import FOOD, FOO_DATABASE_NAME


#
# def create_food_table():
#     con = sqlite3.connect(FOO_DATABASE_NAME)
#     cursor = con.cursor()
#
#     cursor.execute(
#         f"""CREATE TABLE IF NOT EXISTS {FOOD}(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name text NOT NULL,
#             ingredient text NOT NULL,
#             measurement text NOT NULL
#         )"""
#     )
#
#     con.commit()
#     cursor.close()
#     con.close()


async def add_recipe(name: str, ingredients: [], measurement: []):
    ingredients = str(json.dumps(ingredients))
    measurement = str(json.dumps(measurement))

    query = f"INSERT INTO {FOOD}(name, ingredient, measurement) VALUES ('{name}', '{ingredients}', '{measurement}')"

    async with aiosqlite.connect(FOO_DATABASE_NAME) as con:
        cursor = await con.execute(
            query
        )
        await con.commit()
        await cursor.close()
        await con.close()


async def get_all_recipes():
    async with aiosqlite.connect(FOO_DATABASE_NAME) as con:
        cursor = await con.execute(f"select * from {FOOD}")
        results = await cursor.fetchall()
        await con.commit()
        await cursor.close()
        await con.close()
    return results


async def get_single_recipe(recipe_id):
    async with aiosqlite.connect(FOO_DATABASE_NAME) as con:
        cursor = await con.execute(f"select * from {FOOD} where id = '{recipe_id}'")
        results = await cursor.fetchone()
        await con.commit()
        await cursor.close()
        await con.close()

    return results
