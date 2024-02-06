import random

def choose_word():
    words = ["Beekeeper", "Gardener", "Hamburger", "Apple", "unworthy","Harry Potter","Interstaller","Pirates of the Caribbean",
             "Witchcraft","Rhythm","Jockey","Jiujitsu","Buffalo","Bookworm"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ""
    word=word.lower()
    for letter in word:
        if letter in guessed_letters:
            display += letter
        elif letter==" ":
            display += " "
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                attempts -= 1
        else:
            print("Please enter a valid single letter.")

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        print("Attempts left:", attempts)

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()