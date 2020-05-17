import sqlite3
from crawl import get_most_seller_list

con = sqlite3.connect('script.db')
cursor = con.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Games (game TEXT, price TEXT,discount TEXT, final_price TEXT)")


def add_games():
    for game in steam_most_seller_list:
        game_name = game['game']
        price = game['original_price']
        discount = game['discount_rate']
        final_price = game['final_price']
        cursor.execute("INSERT INTO Games (game, price, discount, final_price)VALUES (?,?,?,?)", [
            game_name, price, discount, final_price
        ])


        con.commit()


steam_most_seller_list = get_most_seller_list()
print(steam_most_seller_list)
create_table()
add_games()
con.close()