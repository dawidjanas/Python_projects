import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sqlite3
import datetime
import ssl

def Steam_price_search(user_game):
    status = 0
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()

    #Input + dostosowanie do wyszukiwania na steamie
    game = user_game.replace(" ", "+").lower()

    #Pobieranie daty - ważne przy kreowaniu wykresu 
    stu = datetime.datetime.today()
    date = datetime.datetime.strftime(stu, '%d-%m-%Y')

    steam_search_url = f'https://store.steampowered.com/search/?term={game}'
    steam_search_connection = urllib.request.urlopen(steam_search_url).read()
    steam_search_soup = BeautifulSoup(steam_search_connection, 'html.parser')
    steam_id_search = steam_search_soup.find('a', {'class' : 'search_result_row ds_collapse_flag', 'data-ds-appid': True})['data-ds-appid']

    #Wyszukiwanie strony gry przez ID + nazwa gry
    steam_game_url = f'https://store.steampowered.com/app/{int(steam_id_search)}/{game}/'
    steam_game_connection = urllib.request.urlopen(steam_game_url).read()
    steam_game_soup = BeautifulSoup(steam_game_connection, 'html.parser')

    #Szukanie: nazwy gry, ceny gry, ocen gry
    #W przypadku gier Free-to-Play pokazuje cenę np. bundle pack, DLC itp.
    temp_name = steam_game_soup.find('div', {'class' : 'apphub_AppName'}).text
    try:
        temp_price = steam_game_soup.find("div", {"class": "discount_final_price"}).text
    except:
        temp_price = steam_game_soup.find("div", {"class": "game_purchase_price price"}).text
    temp_reviews = steam_game_soup.find('span', {'class': "game_review_summary positive"}).text

    #Usuwanie białych spacji - Steam ma ###### formatowanie ceny 
    game_name = temp_name.strip()
    game_price = temp_price.strip()
    game_reviews = temp_reviews.strip()

    #Dodawania rekordów do bazy danych
    cur.execute('INSERT INTO Game (id, Title, Reviews, link) VALUES (?, ?, ?, ? )',(steam_id_search, game_name, game_reviews, steam_game_url))
    cur.execute('INSERT INTO Price (game_id, value, date) VALUES (?, ?, ? )', (steam_id_search, game_price, str(date)))
    conn.commit()
    status = 1
    print(status)

    cur.close()