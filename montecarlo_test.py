import numpy as np
import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class montecarloTestSuite(unittest.TestCase):
    # Tests all of the class methods
    
    def test_1_change_weight(self):
        # Take a given side and change the weight
        die = Die([1,2,3,4])
        die.change_weight(4,4)
        die._die
        output = die._die["weights"].values[3]
        
        correct = 4
        self.assertEqual(output,correct)

    def test_2_change_weight(self):
        # Passing a value that is not a side
        die = Die([1,2,3,4])
        output = die.change_weight(5,4)
        # Expecting "That face is not an option" to be printed to the console
     
    def test_3_change_weight(self):
        # Passing a value that cannot be made into a float
        die = Die([1,2,3,4])
        output = die.change_weight(4,"float")
        # Expecting "Inputted weight is not a float" to be printed to the console
    
    def test_4_dice_roll(self):
        # Making sure the dice rolls the correct number of times
        die = Die([1,2,3,4])
        die.dice_roll(5)
        output = len(die.results)
        
        correct = 5
        self.assertEqual(output,correct)
    
    def test_5_show_results(self):
        # Making sure that show_results prints an updated dataframe
        die = Die([1,2,3,4])
        die.change_weight(1,5)
        output = die.show_results()
        
        correct = pd.DataFrame({"side":[1,2,3,4],"weights":[5.0,1.0,1.0,1.0]})
        assert_frame_equal(output,correct)
        
    def test_6_play(self):
        # Takes an input of similar die objects, want to make sure here that the change weight method is working correctly for the inputted weights
        die = Die([1,2,3,4])
        game = Game([[5,3,2,1]])
        game.play(5,die)
        output = die.show_results()["weights"].values
        
        correct = np.array([5.,3.,2.,1.])
        self.assertEqual(output.tolist(),correct.tolist())
    
    def test_7_show(self):
        #Want to make sure the table is displaying in the narrow format correctly
        die = Die([1,2,3,4])
        game = Game([[1,1,1,1],[1,1,1,1]])
        game.play(5,die)
        results = game.show("narrow")
        output = len(results)
        
        correct = 10
        self.assertEqual(output,correct)
    
    def test_8_show(self):
        #Want to make sure the method only accepts narrow as an input with wide as the default
        die = Die([1,2,3,4])
        game = Game([[1,1,1,1]])
        game.play(5,die)
        output = game.show("long")
        # Expecting "Inputted value is not an option. Try 'wide' or 'narrow' instead." to be printed to the console 
        
    def test_9_jackpot(self):
        # Make sure that the method displays the correct number of jackpots
        test_df = pd.DataFrame({1:[1,2,3,3,5],2:[1,2,3,4,5],3:[1,2,3,4,5]})
        die = Die([1,2,3,4,5])
        game = Game([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        analyze = Analyzer(test_df,game)
        output = analyze.jackpot()
        # Expecting the number 4 to be printed to the console
    
    def test_10_combo(self):
        # Making sure that combo is correctly sorting the rows 
        test_df = pd.DataFrame({1:[2,1,3,4,5],2:[4,5,2,1,5],3:[1,2,3,4,5]})
        die = Die([1,2,3,4,5])
        game = Game([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        analyze = Analyzer(test_df,game)
        output = analyze.combo()
        correct = pd.DataFrame({0:[1,1,1,2,5],1:[2,2,4,3,5],2:[4,5,4,3,5],"size":[1,1,1,1,1]})
        
        assert_frame_equal(output,correct)
        
    def test_11_face_counts_per_roll(self):
        # Want to make sure that the face counter per roll method is giving the correct count
        test_df = pd.DataFrame({1:[2,1,3,4,5],2:[4,5,2,1,5],3:[1,2,3,4,5]})
        die = Die([1,2,3,4,5])
        game = Game([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        analyze = Analyzer(test_df,game)
        output = analyze.face_counts_per_roll(die)
        
        correct = pd.DataFrame({1.0:[1,1,0,1,0],2.0:[1,1,1,0,0],3.0:[0,0,2,0,0],4.0:[1,0,0,2,0],5.0:[0,1,0,0,3]})
        assert_frame_equal(output,correct)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)