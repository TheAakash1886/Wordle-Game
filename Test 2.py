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
        
    @patch('builtins.input', side_effect = ['slave'])
    def test_right_word_length(self, mock_inputs) -> None :
        """Test when the word length is 0 - Positive"""
        self.assertTrue(UI.WordLength("Hello"))
         
    @patch('builtins.input', side_effect = ['slave'])
    def test_wrong_word_length(self, mock_inputs) -> None :
        """Test when the word length is 0 - Negative"""
        self.assertFalse(UI.WordLength("Hello"))
        
    @patch('builtins.input', side_effect = ['slave'])
    def test_word_guessed(self, mock_inputs) -> None :
        """Test if the word has already been guessed before - Positive"""
        self.assertTrue(UI.GuessedWord("slave", "slave"))
         
    @patch('builtins.input', side_effect = ['slave'])
    def test_word_not_guessed(self, mock_inputs) -> None :
        """Test if the word has already been guessed before - Negative"""
        self.assertFalse(UI.GuessedWord("Hello","Slave"))
        
    
if __name__ == '__main__':
    unittest.main()