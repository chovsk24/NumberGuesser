#nuber guesser
import time
import random

gameRun = True
guessEngine = True
score = "0" 

while gameRun == True:
    randomNumber = (random.randint(1, 10))
    
    print("I am thinking of a number from 1 through 10!\n")
    print("Can you guess it?\n")

    guessNumber = input(":")
    guessNumber = int(guessNumber)
    
    if guessNumber == randomNumber:
        print("You Won!\n")
    else:
        print("You Lost!\n")
        time.sleep(.5)
        
        
        
        
