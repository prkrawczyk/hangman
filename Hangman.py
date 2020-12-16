#HANGMAN
#Author: Patryk Krawczyk

#Game Instructions 
print("********************************************")
print("            Welcome to Hangman              ")
print("")
print("                Instructions:               ")
print("    Fill in the missing blanks of the word  ")    
print("********************************************")
print("")

#Imports random words from seperate file
import random
with open("words.txt", "r") as f:
    words = f.readlines()
word = random.choice(words)[:-1]
letter_in_word = len(word)
print(f"This is a {letter_in_word} letter word")

#Max amout of tries
attempts = 0
max_errors = 4

#Letters in array
guesses = []
done = False 

#Loop, Fills Letters
while not done:
    print("")
    print("")
    for letter in word:
        if letter.lower() in guesses: 
            print(letter, end=" ")
        else: 
            print("_", end= " ")

    print("")
    
    #Asks for letter and verifies if in word
    guess = input(f"Guess a letter: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        print("")
        print(f"The letter {guess} was not in the word. Max Errors left: {3 - attempts}")
        attempts += 1
        print("     -------")
        print("     |     |")
        print("     |    " + (" O" if attempts > 0 else ""))
        print("     |    " + ("/|\\" if attempts > 1 else ""))
        print("     |    " + (" |" if attempts > 2 else ""))
        print("     |    " + ("/ \\" if attempts > 3 else ""))
        print(" --------")
        if attempts >= max_errors:            
            break
                
    #Stops game if correct or incorrect
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

#Messages once game is completed
if done:
    print(f"Congradulations you found the word! The word was: {word}")
else: 
    print(f"Game Over! The word was: {word}")