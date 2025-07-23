'''
PROJECT: 2 - THE PERFECT GUESS

We are going to write a program that generates a random number and asks the user to guess it.

If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

Hint: Use the random module.'''
import random

n = random.randint(1,100)
a= -1
guesses=0
print("You are Ready to play the Game :\n\n \U0001F607\n")
while(a!=n):
    guesses += 1
    a = int(input("Guess a Number :"))
    if(a>n):
        print("Lower Number Please")
    else:
        print("Higher Number Please")

print(f"You have Guessed the Number at {guesses} attempt")
print("Thankyou for playing the game \U0001F618\U0001F618\U0001F618")
