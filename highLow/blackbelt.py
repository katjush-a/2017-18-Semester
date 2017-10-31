# Samuel Jensen High Low Blackbelt 10/13/2017
# Asks user to come up with a number between 1-100
# and tries to guess it

# Import Random library
import random

# Greet user
print("Hi! Think of a random number between 1-100 and I'll try to guess it! \n"
      "If my guess is too high type H \n"
      "If my guess is too low type L \n"
      "If I guess your number type Y")

# Set loop to keep going
keepGoing = 1

# Set iterations to 0 at start
iterations = 0

# Set min and max guess values
minimum = 0
maximum = 100

while keepGoing == 1:
    # Generate guess
    guess = random.randint(minimum, maximum)

    # Increment iterations each loop
    iterations += 1

    # Get feedback about number
    response = input("My guess is: {}, how is my guess? ".format(guess))

    # If guess is correct stop loop
    if response == 'Y':
        print("Hooray I guessed it in {} tries! ".format(iterations))
        keepGoing = 0
    # If guess is too high, set max to one less than that value and guess again
    elif response == 'H':
        maximum = guess - 1
        print("Hmm, okay...")
    # If guess is too low, set min to one more than that value and guess again
    elif response == 'L':
        minimum = guess + 1
        print("Hmm, okay...")
    # If user doesn't enter valid input ask for it
    else:
        print("I need to know if my guess was too high, low, or correct")
