#nuber guesser
import random

attempts = 0 

print("I am thinking of a number from 1 through 100!\n\nIf it's too high, or too low I will tell you.\n\nCan you guess it?\n")

randomNumber = (random.randint(1, 100))

while True:
    
    guessNumber = input(":")
    guessNumber = int(guessNumber)
    
    if guessNumber < randomNumber:
        print("Too Low!")
        attempts = attempts + 1

    if guessNumber > randomNumber:
        print("Too High!")
        attempts = attempts + 1

    if guessNumber == randomNumber:
        print("You Won!\n")
        attempts = str(attempts)

        print("It took you " + attempts + " attemps! God you're pathetic.\n\n")
        break
        
