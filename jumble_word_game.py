import random

words = ("python", "jumble", "easy", "bingiz", "answer", "rainbow", "Killer", "difficult")
pick_word = random.choice(words)
correct = pick_word
jumble = ""

while pick_word:
    position = random.randrange(len(pick_word))
    jumble += pick_word[position]
    pick_word = pick_word[:position] + pick_word [(position + 1):]

    while jumble == pick_word:
        position = random.randrange(len(pick_word))
        jumble += pick_word[position]
        pick_word = pick_word[:position] + pick_word[(position + 1):]

print("The jumbled word is:", jumble)

guess = input("Guess the word: ")
while guess != correct:
    print("wrong answer")
    guess = input("Guess the word: ")

print("Correct answer")

