""" crypto.py
    Implements a simple substitution cypher
"""

alpha = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
key =   list(" XPMGTDHLYONZBWEARKJUFSCIQV")

def menu():
    print("Decoder Menu \n"
          "0) Quit \n"
          "1) Encode \n"
          "2) Decode")

    return(input("Type the number of which action you'd like to do: "))

def encode(message):
    message = message.upper()                                           # Convert message to upper case
    message = list(message)                                             # Convert message to list

    result = list()                                                     # Create empty list

    for i in range(len(message)):                                       # Loop through the length of message
        result.append(key[alpha.index(message[i])])                     # Each loop add the value in key which corresponds with
                                                                        # the index in alpha of the ith value of message
    result = ''.join(result)                                            # Convert result to string
    return(result)                                                      # Return the result string

def decode(message):
    message = message.upper()                                           # Convert message to upper case
    message = list(message)                                             # Convert message to list

    result = list()                                                     # Create empty list

    for i in range(len(message)):                                       # Loop through the length of message
        result.append(alpha[key.index(message[i])])                     # Each loop add the value in alpha which corresponds with
                                                                        # the index in key of the ith value of message
    result = ''.join(result)                                            # Convert result to string
    return (result)                                                     # Return the result string


def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = input("text to be encoded: ")
            print(encode(plain))
        elif response == "2":
            coded = input("code to be decyphered: ")
            print (decode(coded))
        elif response == "0":
            print ("Thanks for doing secret spy stuff with me.")
            keepGoing = False
        else:
            print ("I don't know what you want to do...")

main()