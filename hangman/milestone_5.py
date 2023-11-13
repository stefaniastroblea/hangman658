import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

# Example usage
word_list = ['apple', 'banana', 'cherry', 'durian']
hangman = Hangman(word_list)

print(hangman.word)
print(hangman.word_guessed)
print(hangman.num_lives)
print(hangman.word_list)
print(hangman.list_of_guesses)
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
     guess = guess.lower()
     if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1
     else:
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives remaining.")


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)

            self.list_of_guesses.append(guess)

# Example usage
word_list = ['apple', 'banana', 'cherry', 'durian']
hangman = Hangman(word_list)

hangman.ask_for_input()

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        # Rest of the class implementation...

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations!!!!!! You won!")
            break

# List of words to pass as argument to play_game function
word_list = ["apple", "banana", "cherry", "durian", "elderberry"]

# Call play_game function to play the game
play_game(word_list)
