import random
import time

score = 0

while True:
    try:
        user_choice = input("Predict the number of the dice 1-6: ")
        if user_choice.lower() == 'done': break
        dice_roll = random.randint(1,6)

        print("Rolling dice...")
        time.sleep(1)

        if int(user_choice) == dice_roll:
            print("Congrats")
            score = score + 1
        else:
            print("Unlucky, number on dice was",dice_roll)
            score = score - 1
        print("Your score so far is",score)
    except:
        print("ERROR")
        quit()
