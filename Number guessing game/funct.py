import random 

def Number_generetor(diff):
    if diff.lower() == "begginer":
        print("Number genereted between 0:20.")
        return random.randint(0, 20)
    elif diff.lower() == "intermediate":
        print("Number genereted between 0:100.")
        return random.randint(0, 100)
    elif diff.lower() == "expert":
        print("Number genereted between 0:20.")
        return random.randint(0, 1000)

def Number_check(number, choice):
    if choice < number:
        print("Genereted number is higher than yours")
        return 0
    elif choice > number:
        print("Genereted number is lower than yours")
        return 0
    elif choice == number:
        print("Congratulations!!!")
        return 1
