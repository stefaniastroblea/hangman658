import random 
favourite_fruits = ["strawberry","raspberry","banana","apple","pineapple"]
word_list = favourite_fruits
print(word_list)
random_word = random.choice(word_list)
word = random_word
print(word)
guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
   print("Good guess!")
else:  
   print("Oops!That is not a valid input!")  