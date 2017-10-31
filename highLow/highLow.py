# Samuel Jensen High Low Project 10/13/2017
# Generates random int from 1-100 and helps user guess until success

# Import the Random library
import random

# Generate random int
randInt = random.randint(1, 100)

# Get user guess
print("I'm thinking of a number from 1-100 \n"
      "Guess and I'll tell you if you're too \n"
      "high, too low, or guessed it!")

# Set iterations to 0 at start of program
iterations = 0

# Set loop to keep going
keepGoing = True

while keepGoing == 1:
    # Get user guess
    guess = input("What is your guess? ")

    # Convert guess to int
    guess = int(guess)

    # Increment iteration each loop
    iterations += 1

    # If user guess is correct quit and congratulate them
    if guess == randInt:
        # Stop the loop
        keepGoing = 0
        # Congratulate user
        print("You got it! The number was {}, it took you {} turns to guess it".format(randInt, iterations))
    elif guess > randInt:
        # If guess is larger, tell user
        print("Your guess was too large!")
    elif guess < randInt:
        # If guess is smaller, tell user
        print("Your guess was too small!")
    else:
        # This condition should never be met but if somehow it is
        # then the program won't crash but the loop will stop
        print("Something went wrong... bye")
        keepGoing = 0
