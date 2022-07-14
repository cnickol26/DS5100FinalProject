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
