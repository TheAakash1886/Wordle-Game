import HW03_Aakash_Irengbam_Dictionary as Dictionary        #import the other modules to use their functions
import HW03_Aakash_Irengbam_Wordle as Wordle
import HW03_Aakash_Irengbam_UI as UI
import unittest                               #import the unittest
from unittest.mock import patch

class WordleTest(unittest.TestCase):
    def test_in_dictionary(self) -> None :                        
        """Test if the word is in the dictionary - Positive"""
        self.assertTrue(Dictionary.checking("hello"))
        
    def test_not_in_dictionary(self) -> None :
        """Test if the word is in the dictionary - Negative"""
        self.assertFalse(Dictionary.checking("stave"))
        
    def test_no_word_length(self) -> None :
        """Test when the word length is 0 - Positive"""
        self.assertFalse(UI.WordLength(""))
         
    def test_some_word_length(self) -> None :
        """Test when the word length is 0 - Negative"""
        self.assertTrue(UI.WordLength("hell"))
        
    def test_word_guessed(self) -> None :
        """Test if the word has already been guessed before - Positive"""
        self.assertTrue(UI.GuessedWord("slave", "slave"))
         
    def test_word_not_guessed(self) -> None :
        """Test if the word has already been guessed before - Negative"""
        self.assertFalse(UI.GuessedWord("hello","slave"))
        
    def test_word_correct_format(self) -> None :
        """Test if the word meets requirements - Positive"""
        self.assertFalse(UI.AuthorizedWord("slave"))
         
    def test_word_incorrect_word_format(self) -> None :
        """Test if the word meets requirements - Negative"""
        self.assertTrue(UI.AuthorizedWord("m1rror"))
        
    def test_correct_word(self) -> None :
        """Test if the word is correct - Positive"""
        self.assertTrue(UI.CorrectWord("slave", "slave"))
         
    def test_word_incorrect_word(self) -> None :
        """Test if the word is correct - Negative"""
        self.assertFalse(UI.CorrectWord("ghost", "slave"))
        
    
if __name__ == '__main__':
    unittest.main()