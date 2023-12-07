import random

class SecretWord:
    __turns = 0
    __fails = 0
    __word = ''
    __lost = 0
    __won = 0
    __prev_guesses = []

#################################################################################
    #Class constructor
    def __init__(self):
        file=open("Dictionary.txt","r") # Read in files from text file
        file.seek(0)
        self.__word_list = file.readlines() # Read all lines and store it in a list

        selection = random.randint(0, len(self.__word_list)-1) # Obtain a random index
        self.__word = self.__word_list[selection]  #Store word from random index
        self.__word = self.__word.rstrip()     # Remove white space from selected word 
        self.__turns = 8

        self.__hidden_word = ''
        for i in range(0, len(self.__word)):
            self.__hidden_word = self.__hidden_word + '_'

#################################################################################

    #Method to print out current progress on word
    def getHiddenWord(self):
        return self.__hidden_word

#################################################################################

    # Method to handle a user guess
    def guess(self, user_guess):
        
        if user_guess.casefold() in self.__prev_guesses:
            print("Already Guessed Character...")
            self.__fails += 1

        elif (self.__word.find(user_guess.capitalize()) != -1) or (self.__word.find(user_guess.casefold()) != -1):
            temp = ''
            print("You Guessed the Letter " + user_guess + "!")
            self.__prev_guesses.append(user_guess.casefold())
            for i in range(0, len(self.__word)):
                if (self.__word[i] == user_guess.capitalize()) or (self.__word[i] == user_guess.casefold()):
                    temp = temp + self.__word[i]
                else:
                    temp = temp + self.__hidden_word[i]
            self.__hidden_word = temp

        else:
            print("Incorrect Guess!")
            self.__prev_guesses.append(user_guess.casefold())
            self.__fails += 1
        

        if self.__fails >= self.__turns:
            self.__lost = 1
        elif self.__hidden_word == self.__word:
            self.__won = 1

#################################################################################

    def getTurns(self):
        return self.__turns
    
    def getFails(self):
        return self.__fails
    
#################################################################################

    def hasWon(self):
        return self.__won

#################################################################################
    
    def hasLost(self):
        return self.__lost
    

    def getWord(self):
        return self.__word