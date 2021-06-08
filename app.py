#nuber guesser
import random

gameRun = True
score = "0" 

print("I am thinking of a number from 1 through 100!\n")
print("If it's too high, or too low I will tell you.\n")
print("Can you guess it?\n")

while gameRun == True:
    randomNumber = (random.randint(1, 100))
    
    guessNumber = input(":")
    guessNumber = int(guessNumber)
    
    if guessNumber < randomNumber:
        print("Too Low!")
        
    if guessNumber > randomNumber:
        print("Too High!")
    
    if guessNumber == randomNumber:
        print("You Won!")
