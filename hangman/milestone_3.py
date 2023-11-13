#creating a while loop and setting its condition to be true
while True:
#user have to guess a letter and assign it to a variable called guess
    guess = input("Guess a letter:")
#check if the guess is a single alphabethical letter
    if len(guess) == 1 and guess.isalpha():
#if guess passed then loop will have to break
       break
    else:
#if guess is wrong then print error
        print("Invalid letter.Enter a single alphabethical character.")
#if statement to find out if the guess its in the word
import random 
favourite_fruits = ["strawberry","raspberry","banana","apple","pineapple"]
word_list = favourite_fruits
print(word_list)
random_word = random.choice(word_list)
word = random_word
print(word)
if guess in word :
    print(f"Good guess!{guess}it is in the word.")
else:
    print(f"Sorry.{guess} it is not in the word and you shall try again.")  
#define check_guess
def check_guess(guess):
 #convert the guess into lower parameter
 guess = guess.lower()   
 #checking if the guess it s in the word
 if guess in word:
    print(f"Good guess!{guess} it is in the word.")
 else:
    print(f"Sorr, {guess} it is not in the word and you shall have another try.")   

def ask_for_input():
       guess = input("Guess a letter:")
check_guess(guess)

ask_for_input()       
              
