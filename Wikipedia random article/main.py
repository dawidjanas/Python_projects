import funct

while True:
    menu_choice = input("Wikipedia menu: \n 1.Random wikipedia article \n 2.View your articles \n 3.Exit \n")
    try: 
        menu_number = int(menu_choice)
    except:
        print("ERROR: Not a number")
        continue
    if menu_number == 1:
        funct.random_articles()
        print('\n')
        continue
    elif menu_number == 2:
        funct.view_database()
        print('\n')
        continue
    elif menu_number == 3:
        print("Thank you for using my little program")
        quit()
