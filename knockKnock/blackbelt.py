# Samuel Jensen, Knock Knock Joke Blackbelt, 9/28/2017
# Checks user input, gets frustrated when user doesn't go with the joke, unnecessary recursion

# Get user's name
name = input("Hi what's your name?")

# Ask user if they want to hear a joke
hearJoke = input("Nice to meet you " + name + ", would you like to hear a knock knock joke?")

# Define asking function
def askJoke(response):
    # If user says 'yes' continue joke
    if response == "yes":
        whoThere = input("Knock knock")

        # Convert whoThere to lowercase in case user capitalized
        whoThere = whoThere.lower()

        # If user continues the joke, continue
        if whoThere == "who's there" or whoThere == "who is there":
            inquisition = input("The Spanish inquisition")

            # Convert inquisition to lowercase in case user capitalized
            inquisition = inquisition.lower()

            # Check if user input continues the joke
            if inquisition == "the spanish inquisition who" or inquisition == "the spanish inquisition who?":
                print("No one expects the Spanish Inquisition!")
            # If not, ragequit
            else:
                print("I don't think you really understand how these jokes work")
        # Otherwise start again
        else:
            misunderstandJoke = input("Do you know how a knock knock joke works?")
            askJoke(misunderstandJoke)

    # If not, commend them, and quit
    elif response == "no":
        print("Good, anyone with any sense of humor wouldn't want to hear a knock knock joke")
        return "no"
    # If neither, chastise them for not being straightforward
    else:
        misunderstandYesNo = input("Please answer yes or no. Would you like to hear a knock knock joke?")
        askJoke(misunderstandYesNo)

# Call function using user input
askJoke(hearJoke)
