attempt = 0               #To keep count of number of attempts made by user
RightWord = "sonar"       #The correct word to be guessed by user

GuessedWordList = []             #To keep track of the words guessed by the user and notify if the same word has been guessed before
CorrectSpot = []          #To store and show the letters that are in the correct spot for the user
IncorrectSpot = []        #To store and show the letters that are in the incorrect spot for the user
DoesntExist = []          #To store and show the letters that dont exist in the word guessed by the user


while(attempt<6):         #To limit the number of attempts of the user to 6
    guess = input("Enter your 5 letter word guess:  ")    #Take the input from the user 
    if(guess in GuessedWordList):          #Check if the word has already been guessed
        print("This was a previous guess please try again")   
    else:   
        if((len(guess) > 5) or (len(guess) < 5) or (guess.isalpha() == False)):   #To check if input has been according to the guidelines
            print("The input should be 5 letters and alphabets only")
            continue
        elif guess == RightWord:
            print("This is the correct word")
            break
        else:
            i = 0
            for i in range(5):
                if guess[i] in RightWord:                       #Check if letter exists in the correct word
                    if RightWord[i]==guess[i]:                  #Check if any alphabets match between the two in the correct spot
                        CorrectSpot.append(guess[i])
                    else:
                        IncorrectSpot.append(guess[i])          
                else:
                    DoesntExist.append(guess[i])
                i+=1
        print("The following letters are in the incorrect spot", IncorrectSpot)   #Print the alphabets in the incorrect spot
        print("The following letters are in the correct spot", CorrectSpot)       #Print the alphabets in the correct spot
        print("The following letters are not in the right word", DoesntExist)     #Print the alphabets not in the right word
    IncorrectSpot.clear()                 #Clear the list for the next attempt
    CorrectSpot.clear()
    DoesntExist.clear()                   
    attempt+=1                            #Increment the value of attempt to keep track of the number of guesses
    GuessedWordList.append(guess)
    
    
#Pseudocode

#while attempt less than 6 do       
# guess = input("Enter your 5 letter word guess  ")     
# if guess in WordList          
#    print "This was a previous guess please try again"   
# else   
#   if length of guess > 5 or length of guess < 5 or guess is not an alphabet   
#       print "The input should be 5 letters and alphabets only" 
#           continue
#   else if guess is equal to RightWord
#       print "This is the correct word" 
#       break
#   else
#       i = 0
#       for i := 0 to 4 do
#           if guess[i] in RightWord
#               if RightWord[i] is equal to guess[i]                  
#                   add guess[i] to correct spot list
#               else
#                   add guess[i] to incorrect spot list
#           else
#               add guess[i] to doesnt exist list
#       i+=1
#   print incorrect spot list  
#   print correct spot list       
#   print doesnt exist list     
#clear incorrect spot list                 
#clear correct spot list
#clear doesnt exist list                   
#increment attempt count by 1                            
#add the word to guessed word list
            