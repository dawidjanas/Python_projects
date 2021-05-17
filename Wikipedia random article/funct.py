import wikipedia 
import webbrowser
import sqlite3

def random_articles():
    conn = sqlite3.connect('wikipedia_articles.sqlite')
    cur = conn.cursor()

    while True:

        wiki_random = wikipedia.random(pages = 1)
        print("Wikipedia random article:", wiki_random)
        choice = input("Do you want to read it (yes/no)? ")
        print("If you are done type 'done'.")
    
        if choice.lower() == 'yes':
            wiki_url = wikipedia.page(wiki_random)
            webbrowser.open(wiki_url.url, new = 2)

            cur.execute('INSERT INTO read_articles(Title, Link) VALUES (?, ?)', (wiki_random, wiki_url.url))
            conn.commit()

        elif choice.lower() == 'no': 
            cur.execute('INSERT INTO not_read_articles(Title, Link) VALUES (?, ?)', (wiki_random, wiki_url.url))
            conn.commit()

        elif choice.lower() == 'done': break
    cur.close()


def view_database():
    conn = sqlite3.connect('wikipedia_articles.sqlite')
    cur = conn.cursor()

    user_choice = input("Do you want to search your 'read' articles or 'not read'? \n")

    if user_choice.lower() == 'read':
        cur.execute('SELECT Title FROM read_articles')
        rows = cur.fetchall()

        for line in rows:
            print(line)

    elif user_choice.lower() == 'not read':
        cur.execute('SELECT Title FROM not_read_articles')
        rows = cur.fetchall()

        for line in rows:
            print(line)
    cur.close()

