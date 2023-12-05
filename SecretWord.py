import random

class SecretWord:
    __turns = 0
    __word = ''
    __lost = 0
    __won = 0

    #Class constructor
    def __init__(self):
        file=open("Dictionary.txt","r") # Read in files from text file
        file.seek(0)
        self.word_list = file.readlines() # Read all lines and store it in a list

        selection = random.randint(0, len(self.word_list)-1) # Obtain a random index
        self.word = self.word_list[selection]  #Store word from random index
        self.turns = 8

        self.hidden_word = ''
        for i in range(0, len(self.word)):
            self.hidden_word = self.hidden_word + str(' _ ')


    #Method to print out current progress on word
    def getHiddenWord(self):
        return self.hidden_word


    # Method to handle a user guess
    def guess(self, user_guess):
        self.turns -= 1
        for char in self.word: 
            if char in self.word:
                print(char, end=" ")
            else:
                print(" _ ")
                self.turns -= 1
                if self.turns == 0:
                    self.lost = 1
        


    def getTurns(self):
        return self.turns
    
    def hasWon(self):
        return self.won
    
    def hasLost(self):
        return self.lost