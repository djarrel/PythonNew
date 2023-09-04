import random

# hangman game
name = input("What is your name? ")
print(f"Welcome to Hangman {name}!\nYou have 3 chances")

words = ["KENYA", "UGANDA", "TANZANIA", "BURUNDI", "RWANDA", "ETHIOPIA", "SOUTHSUDAN",
          "SOMALIA"]

secret_word = random.choice(words)
print(secret_word)

display_word = []
for i in secret_word:
    display_word += "_"
print(display_word)

num = 0 
game_over = False 

while not game_over:
    guess = input("Guess a letter ").upper()    
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        if num >= 3:
            print(f"{name} you loser \nThe word is {secret_word}")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print(f"{name} You win!")
        game_over = True