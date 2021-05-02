import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sqlite3
import ssl
import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

date = datetime.datetime.today()
stu = datetime.datetime.strftime(date, '%d-%m-%Y')

prices = dict()

#STWORZYĆ MODEL BAZY DANYCH 

while True:
    games = input("Enter game name you want to check - (if you are done type 'done'): ")
    if games == 'done': break

    #POSZUKAC NARZEDZIA DO WYSZUKANIA ID GRY ALBO W INNY SPOSOB SZUKAC ICH NA STEAMIE
    url = f'https://store.steampowered.com/app/1237970/Titanfall_2/'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    temp_name = soup.find('div', {'class' : 'apphub_AppName'}).text
    temp_price = soup.find("div", {"class": "game_purchase_price price"}).text

    game_name = temp_name.strip()
    game_price = temp_price.strip()

    prices[game_name] = game_price

for key, value in prices.items():
    print("Game:", key, "Price:", value, "Date:", str(stu))


