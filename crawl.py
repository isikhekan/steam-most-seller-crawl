import requests
from bs4 import BeautifulSoup


def get_steam_game_table(url):
    steam_url = url
    r = requests.get(steam_url)
    r.raise_for_status(),
    soup = BeautifulSoup(r.content, "html.parser")
    steam_most_seller_table = soup.find_all("div", {"id": "TopSellersTable"})
    game_table = steam_most_seller_table[0].contents[len(steam_most_seller_table[0].contents) - 6]
    return game_table.find_all("a")


def get_most_seller_list(page=0, steam_game_data_list=[]):
    url = 'https://store.steampowered.com/games/#p=3&tab=TopSellers'
    sanitized_game_table = get_steam_game_table(url)
    steam_game_data = {
        "game": None,
        "original_price": None,
        "final_price": None,
        "discount_rate": None
    }

    for count in range(len(sanitized_game_table)):
        game = sanitized_game_table[count]
        steam_game_data['game'] = game.find_all("div", {"class": "tab_item_name"})[0].text
        steam_game_data['final_price'] = game.find_all("div", {"class": "discount_final_price"})[0].text
        if len(game.find_all("div", {"class": "discount_original_price"})) > 0:
            steam_game_data['original_price'] = game.find_all("div", {"class": "discount_original_price"})[0].text
            steam_game_data['discount_rate'] = game.find_all("div", {"class": "discount_pct"})[0].text
        steam_game_data_list.append(steam_game_data)
        steam_game_data = {
            "game": None,
            "original_price": None,
            "final_price": None,
            "discount_rate": None
        }
        if count == len(sanitized_game_table) - 1 and page < 3:
            page += 1
            get_most_seller_list(page, steam_game_data_list)
    return steam_game_data_list
