# DS5100FinalProject

## Montecarlo Simulation Package
### Author: Connor Nickol
### Email: can2hr@virginia.edu

## Package Synopsis

### Installing the Package
This package contain 3 classes that together work to run a montecarlo simulation. To install the package first download this repository and then, within the command line, change your directory to be the file of the repository. Then run the line pip install . 

### Importing the Package into Python
That line will install the package. To import the package use import DS5100FinalProject within a python file. Then use from DS5100FinalProject import montecarlo to specify the class file with the code. From there use DS5100FinalProject.montecarlo."insert class or method here" to run code from the montecarlo file. 

### Instantiating the die class
The die class takes in the faces you want to use for rolling as a list.
```
import pandas as pd
import numpy as np
import DS5100FinalProject as fp
from DS5100FinalProject import montecarlo

die = fp.montecarlo.Die(1,2,3,4)

# Once your die is instantiated you can call:

die.show_results()

# to see the current set of faces and weights for each face. Note that default weight is 1 for each face
```
Once you have created your die you can use the method die.change_weight(side, new_weight) to change the weight of a specific face.
```
die.change_weight(1,5)
```

### Instantiating the game class
The second class called Game() works to roll the dice the user creates.
```
# The user must input a list of the weights they want to use. Each list in the list must be the same length and the die will all use the same faces that the user created with the die class

game = Game([[1,2,3,4],[1,1,1,1],[4,3,2,1]])

# This would instantiate a game with 3 dice of the weights specified all with the faces 1,2,3,4
```
### Rolling the created die
```
# Once you've instantiated your dice use game.play(num_rolls,die) to roll all of the dice.
# For example if you want 1000 rolls use

game.play(1000,die)

# Where die is your created die object you made earlier.

```
### Looking at the output
```
# Use the show method to see the output of the rolls
output = game.show()
output
```
### Analyzing the output
```
# Use the analyzer class to analyze the results of the rolls, need to instantiate it
# Takes in the your output from game.show() and also your game object
analyze = Analyzer(output,game)
```
### Use the jackpot method to count the number of rolls that resulted in all the same face
```
analyze.jackpot()
```
### Use the combo method to see all the unique combinations rolled
```
analyze.combo()
```
### Use the face_counts_per_roll method to see a summary of the number of faces rolled for each roll
```
# Need to input your die object
analyze.face_counts_per_roll(die)
```
## API Description
### List of classes and their methods

### Die class: 

class Die():
    '''
    Purpose: This class works to create and roll a N sided die that has W weights.
    
    Input: The only required input is the number of faces or sides the user wants on the die. Option inputs include faces other than numbers 1 through N, different weights for certain faces, and the number of rolls a user wants.
    
    Output: There is no general output but users can call the show_results() method to see the currents weights and sides.
    '''
   
### Die class methods:
change_weight(side,new_weight):
        '''
        Purpose: Take a side and a new weight and changes the weight of the side to the new weight.
        
        Input: A side and a new weight.
        
        Output: None
        '''
        
dice_roll(n_rolls=1):
        '''
        Purpose: Rolls the dice 1 or more times and stores the results.
        
        Input: Number of rolls the user wants. Default is 1.
        
        Output: None
        '''
        
 show_results():
        '''
        Purpose: Returns to the user the current faces and weights.
        
        Input: None
        
        Output: Dataframe with current faces and weights
        '''
### Game class:
class Game():
    '''
    Purpose: Roll one or more dice of the same kind a number of times.
    
    Input: List of die weights with the same number of sides.
    
    Output: Dataframe with results of all the rolls. 
    '''
### Game class methods
play(rolls,die):
        '''
        Purpose: Rolls the die a number of times.
        
        Input: Number of rolls and the instantiated die class.
        
        Output: None
        '''
show(form = "wide"):
        '''
        Purpose: Shows the user the result of the rolls of the play method.
        
        Input: Option input of "narrow" will output the table in narrow form. The default form is wide.
        
        Output: Returns a table with the results of the rolls. 
        '''
### The Analyzer class:
class Analyzer():
    '''
    Purpose: This class works to analyze the results of the rolls from the Game class.
    
    Input: The table from the show method of the Game class and the instantiated Die class.
    
    Output: Multiple tables for number of jackpots, unique combos, and face counts.
    '''
### Analyzer class methods
jackpot():
        '''
        Purpose: Count and create a table of the number of jackpots that occured from the rolling of the die. 
        
        Input: None
        
        Output: Number of jackpots and table listing them.
        '''
        
combo():
        '''
        Purpose: Find the unique combos of dice faces rolled and output them in a table.
        
        Input: None
        
        Output: Table with all of the unique combos.
        '''
        
face_counts_per_roll(game):
        '''
        Purpose: Count the number of each face that was rolled for a given roll of all the die.
        
        Input: The already instantiated Die class.
        
        Output: Table consisting of the counts of each face rolled for a given dice roll.
        '''

## Manifest

