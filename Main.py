from SecretWord import *

# Main.py

test = SecretWord()

while(True):
    print("Guess a character: ") 
    guess = input()

    if guess:
        test.guess(guess[0])
    else:
        print("Invalid Input")
    
    break



