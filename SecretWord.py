import random

class SecretWord:

    def __init__(self):
        file=open("Dictionary.txt","r") # Read in files from text file
        file.seek(0)
        self.word_list = file.readlines() # Read all lines and store it in a list
    
        selection = random.randint(0, len(self.word_list)-1) # Obtain a random index
        self.word = self.word_list[selection]  #Store word from random index

        print(self.word)




