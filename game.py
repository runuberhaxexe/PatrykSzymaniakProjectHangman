import random
def pregame1():
    words = ['dominik', 'spyder', 'pycharm', 'java']
    word = random.choice(words)
    return word
def pregame2():
    try:
        tries = input("How many tries would you like to get? [Default is 5]: ")
        int(tries)
    except ValueError:
        tries = 5
    return tries
def hangman(word, tries):
    win = False
    guessed = []
    print("The word is " + str(len(word)) + " letters long.")
    print(len(word) * '*')
    while tries > 0:
        print("You've " + str(tries) + " tries left")
        guess = input("Guess the word itself or one of it's letters: ")
        if len(guess) == 1:
            if guess in guessed:
                print(" You've guessed that letter before.")
            elif guess in word:
                guessed.append(guess)
                print("You've guessed a letter!")

            else:
                print("You've guessed wrong...")
                tries -= 1
        elif len(guess) == len(word):
            if guess == word:
                print("Congratulations! You've guessed the word!")
                win = True
                tries = 0
                guessed = word
            else:
                print("Oh no... it's not the word you're searching for...")
                tries -= 1
        else:
            print("The input is not the full word nor a letter.")
        preview=''
        for letter in word:
            if letter in guessed:
                preview += letter
            else:
                preview += '*'
        print(preview)
        if len(guessed) == len(word):
            win = True
            tries = 0
    if win == False:
        return "You lost..."
    else:
        return "You won!"
print(hangman(pregame1(),pregame2()))