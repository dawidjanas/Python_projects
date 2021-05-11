import random

def Char_split(word):
    return [char for char in word]

words = ['dog','cat','car','cow','apple']
rnd = random.randint(0,len(words) - 1)
word = Char_split(words[rnd])

hp = 7
score = 0
temp_score = 0
underscores = list()

for i in range(len(word)):
    underscores.append(" _ ")

print(underscores)


while hp > 0 and " _ " in underscores:
    user_char = input("Enter ONE letter to guess the word: ")

    for char in range(len(word)):
        if user_char == word[char]:
            underscores[char] = user_char
            temp_score = 1
        elif not temp_score > 0:
            temp_score = 0 
        
    if temp_score > 0:
        score = score + (temp_score * 5)
    else:
        print("Wrong letter")
        hp = hp - 1
        score = score - 5
        print("Your HP:", hp)
    print(underscores)
    temp_score = 0

print("Your score: ", score)


