# Samuel Jensen, Knock Knock Joke Blackbelt, 9/28/2017

# Get user's name
name = input("Hi what's your name?")

# Ask user if they want to hear a joke
hearJoke = input("Nice to meet you " + name + ", would you like to hear a knock knock joke?")


# Define asking function
def askJoke(response):
    # If user says 'yes' continue joke
    if response == "yes":
        whoThere = input("Knock knock")
        return whoThere
    # If not, commend them, and quit
    elif response == "no":
        print("Good, anyone with any sense of humor wouldn't want to hear a knock knock joke")
    # If neither, chastise them for not being straightforward
    else:
        misunderstand = input("Please answer yes or no. Would you like to hear a knock knock joke?")
        askJoke(misunderstand)


# Define who is there function
def whoIs(response):
    # If response is equal to the user input in lowercase, continue joke
    if response.lower == "who's there" or "who is there":
        inquisition = input("The Spanish inquisition")
    # Otherwise start again
    else:
        misunderstand = input("Do you know how a knock knock joke works?")
        askJoke(misunderstand)


# Call asking function
whoIs(askJoke(hearJoke))
