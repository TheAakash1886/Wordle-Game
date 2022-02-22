import HW03_Aakash_Irengbam_Dictionary
def WordLength(guess):
    if(len(guess) == 0):
        return False
    else:
        return True
    
def GuessedWord(guess, GuessedWordList):              #Check if the word has already been guessed
    if(guess in GuessedWordList):
        return True
    else:
        return False
    
def AuthorizedWord(guess):                            #To check if input has been according to the guidelines
    if((len(guess) > 5) or (len(guess) < 5) or (guess.isalpha() == False)):
        return True
    else:
        return False
    
def CorrectWord(guess, RightWord):                    #check if the entered word is correct
    if(guess == RightWord):
        return True
    else:
        return False  

def userinterface(RightWord):
    
    GuessedWordList = []     #To keep track of the words guessed by the user and notify if the same word has been guessed before
    attempt = 0
    CorrectPosition = 0
    IncorrectGuess = 0
    IncorrectPosition = 0
    Win = 0
    while(attempt<6):         #To limit the number of attempts of the user to 6

        guess = input("Enter your 5 letter word guess:  ").lower()    #Take the input from the user
        if(WordLength(guess) == False):
            quit()
        if(GuessedWord(guess, GuessedWordList) == True):          
            print("This was a previous guess please try again")
        else:
            if((AuthorizedWord(guess) == True) or (HW03_Aakash_Irengbam_Dictionary.checking(guess) == False)):   #To check if input has been according to the guidelines
                print("The input should be 5 letters and alphabets and in dictionary only")
                continue
            elif (CorrectWord(guess, RightWord) == True):           
                print("This is the correct word")
                Win+=1
                break
            else:                              #to check the condtions on if and where the entered letter locations match with the correct word
                letter_counts: dict = {}
                appraisal = []

                for letter in RightWord:
                    if letter in letter_counts.keys():
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1

                for index in range(len(RightWord)):
                    if guess[index] == RightWord[index]:
                        appraisal.append(' ')
                        letter_counts[RightWord[index]] -= 1
                        CorrectPosition+=1
                    else:
                        appraisal.append('"')
                        IncorrectGuess+=1

                for index in range(len(RightWord)):
                    if guess[index] != RightWord[index]:
                        if guess[index] in letter_counts:
                            if letter_counts[guess[index]] > 0:
                                letter_counts[guess[index]] -= 1
                                appraisal[index] = "'"
                                IncorrectPosition+=1

                print(" "*33 + ''.join(appraisal))
        attempt+=1
        GuessedWordList.append(guess)
    else:                                                                #if the number of attempts have exceeded 6 enter the condition
        print("Failed in 6 tries no more tries left, try again next time")
    print("The game statistics were as follows:\n")
    print("Attempts: ", attempt, "\n")
    print("Incorrect position: ",IncorrectPosition, "\n")
    print("Correct position: ", CorrectPosition, "\n")
    print("Incorrect guess: ", IncorrectGuess, "\n")
    print("Win count", Win)