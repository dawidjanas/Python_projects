import funct

while True:
    user_choice = input("Menu: \n 1.Check crypto price - enter crypto name. \n 2.Add your crypto - you can compare current price to price when you bought \n 3.Check current price with your price \n")

    if int(user_choice) == 1:
        name = input("Enter crypto name: \n")
        funct.price_check(name)
        continue
    elif int(user_choice) == 2:
        name = input("Enter crypto name: \n")
        funct.add_crypto(name)
        continue
    elif int(user_choice) == 3:
        name = input("Enter crypto name: \n")
        funct.check_user_crypto_price(name)
        quit()
