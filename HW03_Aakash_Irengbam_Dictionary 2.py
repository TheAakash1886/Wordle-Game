import random

f = open("/Users/aakashirengbam/Downloads/words.txt", "r")       #open the text file
wordlist = f.read()                                              #read the text file
wordslist = wordlist.split("\n")
newList = []
for x in wordslist:
    if len(x) == 5:                                              #only read text file if the length of the letter is 5 words
        newList.append(x.lower())
        
def randomword():                                                #choose a random word from the dictionary 
    RightWord = random.choice(newList)    
    return RightWord

def checking(y):                                                 #check if the user entered word exists in the dicionary
    if y in newList:
        return True
    else:
        return False