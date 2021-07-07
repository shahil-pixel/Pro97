# mam I did it myself,I referred to another project for the import
# random because it wasn't taught in class but I did the rest myself

import random
chances = 0
number = random.randint(1,9)
print("Number guessing game")

while chances < 5:
    guess = int(input("Guess a number (between 1 and 9): "))
    print (guess)
    if (guess == number):
        print("Congratulations you won!")
    elif(guess > number):
        print("Your number is too high,guess a number lesser than ",guess)
    elif(guess < number):
        print("Your number is too low,guess a number higher than ",guess)
    
    chances = chances + 1

if not chances < 5:
    print("You lost the game,the number is ",number)