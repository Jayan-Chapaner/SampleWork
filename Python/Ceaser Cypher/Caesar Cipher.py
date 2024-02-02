'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

# create dictionary of letters as a string because using the ASCII method will not allow us to loop round if we pass "z" 
# get size of dictionary in the event numbers are also added to the dictionary and or the the size changes
dictionary = "abcdefghijklmnopqrstuvwxyz"
dictionarySize = len(dictionary)

# function to produce either cypherText or plainText as resultText
def encrypt_decrypt(selection, shiftKey, message):
    resultText = ""
    if selection == "d":
        shiftKey = -shiftKey # make shift key negative for decryption
    for char in message:
        char = char.lower() # make characters lower case so dictionary can be used
        if char.isalnum(): # check that character is alpha numeric so can be used in cypher if not leave as is
            index = dictionary.find(char)
            if index == -1: #chech if char is not in dictionary, if not leave as is
                resultText += char
            else:
                newIndex = index + shiftKey # get new index to produce new char
                if newIndex >= dictionarySize: # if the index goes past z loop back to a
                    newIndex -= dictionarySize
                elif newIndex < 0:
                    newIndex += dictionarySize # if index comes before a loop to z
                resultText += dictionary[newIndex] # create plane or cypher text letter by letter
        else:
            resultText += char # leave special characters as is
    return resultText.upper() # return cypher or plain text

# run in a loop so as to not keep relaunching the program
running = True

while running:

    selection = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ").lower() #input validation for selection
    if selection == "e" or selection == "d":
        keyword = ""
        if selection == "e": # change key word so to encrypt or decrypt so message prompt makes sense
            keyword = "Encrypt"
        else:
            keyword = "Decrypt"
        shiftKey = (input("Please enter the key (0 to 26) to use.\n> ")) 
        if shiftKey.isnumeric() and (int(shiftKey) >= 0 and int(shiftKey) <= 26): # input validation for shift (numeric, non negative and < 27)
            message = input(f"Enter the message to {keyword}.\n> ") # get message
            print(keyword + "ed Message is:\n" + encrypt_decrypt(selection, int(shiftKey), message)) # create output and display to user
            repeat = input("\nDo you want to go again, y/n?\n> ").lower() # ask to loop or break 
            if repeat == "n":
                running = False
        else:
            input("Error invalid key, Press Enter to try again") # error handling for shift key
    else:
        input("Error invalid Selection, Press Enter to try again") # error handling for selection
