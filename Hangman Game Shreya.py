#TASK 1 - HANGMAN GAME
#https://github.com/ShreyaTejan/CodeAlpha_tasks

import time

#rules of game
#user welcome
print("Welcome to the Hangman Game")

name = input("Player 01 enter your name: ")

print("-------RULES--------")
print("--------------------")
print(name , " , you get 10 chances to guess the word selected letterwise")



print ("Hello, " + name, "\nLet's play hangman ◡‿◡ ")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#the selected word is CODEALPHA
word = ("codealpha")

#create empty variable
guesses = ''

#number of turns
turns = 10

# Create a while loop

while turns > 0:         

    # counter starting with zero
    failed = 0             

    # for every character in the word    
    for char in word:      

    # see if the character is in the users guess
        if char in guesses:    
    
        # print the character
            print (char,end=" "),    

        else:
    
        # if not found:
            print ("_ ",end=" "),     
       
        # also increase failed counter with one
            failed += 1    

    # if failed is equal to zero
    # print You Won
    if failed == 0:
        print("\nYou guessed it. \nThe word is: " + word, "\nHurrayyy!!! You won!!")
    # exit the script
        break            
    # ask the user go guess a character
    guess = input("\nGuess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
        print ("Sorry " + name, "that's incorrect.")  
 
    # turns left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
            print ("You lost," + name,"\n Better luck next time!"  )
