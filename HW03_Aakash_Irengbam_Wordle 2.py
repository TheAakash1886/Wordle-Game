from pickletools import stringnl_noescape

import HW03_Aakash_Irengbam_Dictionary   #import the other modules to use their functions
import HW03_Aakash_Irengbam_UI


def main():                                                       #define the main function
    RightWord = []                                                       
    RightWord = HW03_Aakash_Irengbam_Dictionary.randomword()      #call to the dictionary to generate the random word
    HW03_Aakash_Irengbam_UI.userinterface(RightWord)              #send the generated random word to the User Interface
    
if __name__ == "__main__":                                        #run the main function
    main()
