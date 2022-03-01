import random
import os

f = open("/Users/aakashirengbam/Downloads/words.txt", "r")       #open the text file
wordlist = f.read()                                              #read the text file
wordslist = wordlist.split("\n")
f.close()
f = open("wordListNew.txt", "w")
for x in wordslist:
    if len(x) == 5:                                              #only read text file if the length of the letter is 5 words
        #newList.append(x.lower())
        f.write(f"{x.lower()}\n")
f.close()
f = open("wordListNew.txt", "r")
content = f.read()
newList = content.split("\n")
        
        
def randomword():                                                #choose a random word from the dictionary 
    RightWord = random.choice(newList)    
    return RightWord

def checking(y):                                                 #check if the user entered word exists in the dicionary
    if y in newList:
        return True
    else:
        return False
    
def removeWord(word):
    with open("wordListNew.txt", "r") as f:
        lines = f.readlines()
    with open("wordListNew.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != word:
                f.write(line)
    if(os.stat("wordListNew.txt").st_size == 0):
        resetWords()

def resetWords():
    f = open("wordListNew.txt", "w")
    f.write(newList)
    f.close()