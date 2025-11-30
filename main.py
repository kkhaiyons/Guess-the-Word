import random

words = ['milkshake', 'semi', 'computer', 'kitana', 'snowman', 'television', 'candy', 'apple', 'school','makayla']

def update_dashes(word, dashes, guess):
    for i in range(len(word)):
        if word[i] == guess:
            dashes[i] = guess
    return dashes

def get_guess(word):
    dashes = ["-"] * len(word)
    guessed_letters = set()
    tries = 0

    while tries < 10 and "-" in dashes:
        print("Here's your word:\n" + " ".join(dashes))
        guess = input("Try to guess it: ").lower()

        if guess == word:
            print("Wow that was quick! You guessed the word! " + "\033[1m\033[95m" + word + "\033[0m")
            return

        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried that...")
            else:
                guessed_letters.add(guess)
                if guess in word:
                    print("Correct!")
                    update_dashes(word, dashes, guess)
                    print(" ".join(dashes))
                else:
                    tries += 1
                    print("That sucks! You have " + str(10 - tries) + " tries left.")
        elif len(guess) > 1:
            print("One at a time please!!!")
        else:
            print("Only letters!")

    if "-" not in dashes:
        print("Yay, you guessed the word! " + "\033[1m\033[95m" + word + "\033[0m")
    else:
        print("You lose! The word was: " + "\033[1m\033[91m" + word.upper() + "\033[0m")
        print("\033[1m\033[91mGAME OVER\033[0m")

def main():
    print("\033[1m\033[95m" +"Welcome to guess the word!" + "\033[0m")
    wrong_attempts = 0
    while True:
        choice = input("Play? Y/N: ").lower()
        if choice == "y":
            word = random.choice(words)
            get_guess(word)
        elif choice == 'n':
            print("Aww goodbye. :(")
            break
        else:
            wrong_attempts += 1
            if wrong_attempts == 1:
                print("Huh? Y or N???:")
            elif wrong_attempts == 2:
                print("I said y or n !")
            elif wrong_attempts == 3:
                print("Do you know how to work a keyboard??")
            elif wrong_attempts == 4:
                print("Oh I see...")
            else:
                print("Whatever")

main()