from ssl import create_default_context
import urllib.request, urllib.parse, urllib.error
import sqlite3
from bs4 import BeautifulSoup

def price_check(crypto_name):
    crypt_value_change_site = ''

    url = f"https://coinmarketcap.com/currencies/{crypto_name}/"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    crypto_price = soup.find('div', {'class' : 'priceValue___11gHJ'}).text
    crypt_value_change = soup.find('span', {'style' : 'font-size:14px;font-weight:600;padding:5px 10px'}).text
    crypt_symbol = soup.find('small', {'class' : 'nameSymbol___1arQV'}).text

    if soup.find('span', {'class' : 'icon-Caret-up'}) in soup.find('span', {'style' : 'font-size:14px;font-weight:600;padding:5px 10px'}):
        crypt_value_change_site = '+'
    elif soup.find('span', {'class' : 'icon-Caret-down'}) in soup.find('span', {'style' : 'font-size:14px;font-weight:600;padding:5px 10px'}):
        crypt_value_change_site = '-'

    print("Crypto symbol:", crypt_symbol)
    print("Current crypto price:", crypto_price)
    print("Change value:", crypt_value_change_site + crypt_value_change)
    return crypto_price
    

def add_crypto(crypto_name):
    conn = sqlite3.connect('user.sqlite')
    cur = conn.cursor()

    temp = price_check(crypto_name)
    current_price = temp[1:].replace(',','').replace('.','')

    cur.execute("INSERT INTO Crypto (Name, Value) VALUES (?, ?)", (crypto_name, current_price))
    conn.commit()
    cur.close()


def check_user_crypto_price(crypto_name):
    conn = sqlite3.connect('user.sqlite')
    cur = conn.cursor()

    cur.execute(f'''SELECT Value FROM Crypto WHERE Name = '{crypto_name}' ''')
    user_price = cur.fetchone()

    temp = price_check(crypto_name)
    current_price = temp[1:].replace(',','').replace('.','')
    change = 100 * ((float(current_price) - float(user_price[0]))/abs(user_price[0]))

    print("Your change value:",change,'%')

    conn.commit()
    cur.close()
