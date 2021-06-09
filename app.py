#nuber guesser
import random

score = 0 

print("I am thinking of a number from 1 through 100!\n\nIf it's too high, or too low I will tell you.\n\nCan you guess it?\n")

randomNumber = (random.randint(1, 100))

while True:
    
    guessNumber = input(":")
    guessNumber = int(guessNumber)
    
    if guessNumber < randomNumber:
        print("Too Low!")
        score = score + 1
    if guessNumber > randomNumber:
        print("Too High!")
        score = score + 1
    if guessNumber == randomNumber:
        print("You Won!\n")
        score = str(score)
        print("It took you " + score + " attemps! God you're pathetic.\n\n")
        
