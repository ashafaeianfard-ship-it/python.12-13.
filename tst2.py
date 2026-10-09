
import random

print("Choose a number between 1 and 100.")

low = 1
high = 100

while low <= high:
    guess = random.randint(low, high)

    print("My guess is:", guess)

    answer = input("Is your number higher, lower, or correct? ")

    if answer == "correct":
        print("I guessed it!")
        break

    elif answer == "higher":
        low = guess + 1

    elif answer == "lower":
        high = guess - 1

    else:
        print("Please type higher, lower, or correct.")