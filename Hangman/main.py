import random

def Char_split(word):
    return [char for char in word]

words = ['cat', 'dog', 'cow', 'car', 'plane']
rnd = random.randint(0,len(words) - 1)
word = Char_split(words[rnd])

hp = 7
score = 0
underscores = list()

for i in range(len(word)):
    underscores.append(" _ ")

print(underscores)

while hp > 0 and " _ " in underscores:
    user_char = input("Enter ONE letter to guess the word: ")

    if user_char in word:
        word_index = word.index(user_char)
        underscores[word_index] = user_char
        score = score + 5
    else:
        print("Wrong letter")
        hp = hp - 1
        score = score - 5
        print("Your HP:", hp)
    print(underscores)

print("Your score: ", score)
