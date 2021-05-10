import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sqlite3
import datetime

def Steam_id(user_game):
    try:
        game_list = dict()
        status = 0

        #Sprawdzanie AppID z bazy danych Steama
        conn_select = sqlite3.connect('steam_database.sqlite')
        cur_select = conn_select.cursor()

        #Pobieranie AppID
        cur_select.execute(f"SELECT appid, name FROM mytable WHERE name LIKE '%{user_game}%'")
        rows = cur_select.fetchall()
        for key,value in rows:
            game_list[key] = value

        #Lista gier pdoobnych do tego co wpisał użytkwonik
        for key,value in game_list.items():
            print("AppID:", key, "Title:", value)

        #Wybór z listy dostępnych tytułów 
        steam_id_search = input("Pick the specific game from the list - pick AppID: ")

        cur_select.close()
        status = 1
        print(status)
        return steam_id_search
    except:
        print(status)

def Steam_price_insert(appid):
    try:
        status = 0

        #Dodawanie gier, które użytkownik chce followować
        conn_insert = sqlite3.connect('price_database.sqlite')
        cur_insert = conn_insert.cursor()
        
        #Pobieranie daty - ważne przy kreowaniu wykresu 
        stu = datetime.datetime.today()
        date = datetime.datetime.strftime(stu, '%d-%m-%Y')

        #Wyszukiwanie strony gry przez ID + nazwa gry
        steam_game_url = f'https://store.steampowered.com/app/{int(appid)}/'
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
        cur_insert.execute('INSERT INTO Game (id, Title, Reviews, link) VALUES (?, ?, ?, ? )',(appid, game_name, game_reviews, steam_game_url))
        cur_insert.execute('INSERT INTO Price (game_id, value, date) VALUES (?, ?, ? )', (appid, game_price, str(date)))
        conn_insert.commit()

        cur_insert.close()
        status = 1
        print(status)
    except:
        print(status)