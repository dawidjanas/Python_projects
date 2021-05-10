import random 
import funct

print("Hello epic gamer.") 
try:
    user_difficulty = input("Choose difficulty (begginer, intermediate, expert): ")
    gnr = funct.Number_generetor(user_difficulty)
    genereted_number = int(gnr)
except:
    print("ERROR: you must choose difficulty")
    quit()

score = 100

while True:
    try:
        usr = input("Try to guess the number: ")
        user_guess = int(usr)
    except:
        print("ERROR: choice not a number, try again")
        continue
    if funct.Number_check(genereted_number, user_guess) == 1: break
    score = score - 5
    if score == 0: break

print("This is your score:", score)