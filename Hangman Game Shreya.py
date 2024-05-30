#TASK 1 - HANGMAN GAME
#https://github.com/ShreyaTejan/CodeAlpha_tasks

import time

#rules of game
#welcoming the user
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

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=" "),    

        else:
    
        # if not found, print a dash
            print ("_ ",end=" "),     
       
        # and increase the failed counter with one
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
 
    # print wrong
        print ("Sorry " + name, "that's incorrect.")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You lost," + name,"\n Better luck next time!"  )
