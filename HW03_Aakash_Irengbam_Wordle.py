from pickletools import stringnl_noescape

import HW03_Aakash_Irengbam_Dictionary   #import the other modules to use their functions
import HW03_Aakash_Irengbam_UI
import Database as db

db_logging = db.SQDatabase()
def main():                                                       #define the main function
    RightWord = []                                                       
    RightWord = HW03_Aakash_Irengbam_Dictionary.randomword()      #call to the dictionary to generate the random word
    HW03_Aakash_Irengbam_Dictionary.removeWord(RightWord)
    #HW03_Aakash_Irengbam_UI.userinterface(RightWord)              #send the generated random word to the User Interface
    Inter = HW03_Aakash_Irengbam_UI.Interface(RightWord)
    Inter.userinterface()
    
if __name__ == "__main__":                                        #run the main function
    main()
    db_logging.analyze("2022-04-28 00:00:00.000000",
                        "2022-04-29 00:00:00.000000")
    db_logging.DatabaseClose()
