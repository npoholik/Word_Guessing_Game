from SecretWord import *

# Main.py

test = SecretWord()

while( (not test.hasLost()) or (not test.hasWon()) ):
    print("The hidden word is: " + test.getHiddenWord())
    print("You have " + str(test.getTurns() - test.getFails()) + " attempts remaining")
    print("Guess a character: ") 
    guess = input()

    if guess:
        test.guess(guess[0])
    else:
        print("Invalid Input")

    if test.hasLost():
        print("You have lost...")
        print("The word was " + test.getHiddenWord())
        break
    elif test.hasWon():
        print("YOU WIN!")
        print("You guessed " + test.getHiddenWord() + " with " + str(test.getFails()) + " wrong attempts")
        break

    print(test.hasWon())

