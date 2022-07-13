import numpy as np
import pandas as pd

class Die:
    '''
    Purpose: This class works to create and roll a N sided die that has W weights.
    
    Input: The only required input is the number of faces or sides the user wants on the die. Option inputs include faces other than numbers 1 through N, different weights for certain faces, and the number of rolls a user wants.
    
    Output: There is no general output but users can call the show_results() method to see the currents weights and sides.
    '''
    def __init__(self,n_sides):
        '''
        Takes an array of faces as an input. 
        '''
        self.weights = np.ones(len(n_sides))
        self.n_sides = n_sides
        self._die = pd.DataFrame({
            'side': self.n_sides,
            'weights': self.weights
        })
    
    def change_weight(self,side,new_weight):
        '''
        Purpose: Take a side and a new weight and changes the weight of the side to the new weight.
        
        Input: A side and a new weight.
        
        Output: None
        '''
        if side in self._die.values:
            def isfloat(num):
                try:
                    float(num)
                    return True
                except ValueError:
                    return False
            test = isfloat(new_weight)
            if test == True:
                pos = self._die[self._die["side"]==side].index.values
                self._die.loc[pos , "weights"] = float(new_weight)
            else:
                print("Inputted weight is not a float")
        else:
            print("That face is not an option")
    
    def dice_roll(self,n_rolls=1):
        '''
        Purpose: Rolls the dice 1 or more times and stores the results.
        
        Input: Number of rolls. Default is 1.
        
        Output: None
        '''
        results = []
        for i in range(n_rolls):
            result = self._die.side.sample(weights=self._die.weights).values[0]
            results.append(result)
        self.results = pd.Series(results)
    
    def show_results(self):
        '''
        Purpose: Returns to the user the current faces and weights.
        
        Input: None
        
        Output: Dataframe with current faces and weights
        '''
        return self._die
    
class Game():
    '''
    Purpose: Roll one or more dice of the same kind a number of times.
    
    Input: List of die weights with the same number of sides.
    
    Output: Dataframe with results of all the rolls. 
    '''
    
    def __init__(self,old_games):
        '''
        Takes in the list of die weights
        '''
        self.old_games = old_games
        self._all_results = pd.DataFrame({})
        
    def play(self,rolls,die):
        '''
        Purpose: Rolls the die a number of times.
        
        Input: Number of rolls and the instantiated die class.
        
        Output: None
        '''
        num = 0
        for each in self.old_games:
            num += 1
            sides = die._die["side"].values
            for i in range(0,len(each)):
                die.change_weight(sides[i],each[i])  
            die.dice_roll(rolls)
            self._all_results[num] = die.results
        
    def show(self,form = "wide"):
        '''
        Purpose: Shows the user the result of the rolls of the play method.
        
        Input: Option input of "narrow" will output the table in narrow form. 
        
        Output: Returns a table with the results of the rolls. 
        '''
        self._all_results.index.name = "roll_num"
        if form == "wide":
            return(self._all_results)
        elif form == "narrow":
            return(self._all_results.T.stack())
        else:
            print("Inputted value is not an option. Try 'wide' or 'narrow' instead.")
            
class Analyzer():
    '''
    Purpose: This class works to analyze the results of the rolls from the Game class.
    
    Input: The table from the show method of the Game class and the instantiated Die class.
    
    Output: Multiple tables for number of jackpots, unique combos, and face counts.
    '''
    
    def __init__(self,old_game,game):
        '''
        Takes in the table from the show method of the Game class and the instantiated Die class.
        '''
        self.old_game = old_game
        self.type = type(self.old_game.iloc[:,0][0]) is str
    
    def jackpot(self):
        '''
        Purpose: Count and create a table of the number of jackpots that occured from the rolling of the die. 
        
        Input: None
        
        Output: Number of jackpots and table listing them.
        '''
        num_jackpot = 0
        jackpots = pd.DataFrame()
        for i in range(0,len(self.old_game)):
            row = self.old_game.iloc[i]
            if len(set(row)) == 1:
                num_jackpot += 1
                temp = pd.DataFrame([row])
                jackpots = pd.concat([jackpots,temp])
        print(num_jackpot)
        return jackpots

    def combo(self):
        '''
        Purpose: Find the unique combos of dice faces rolled and output them in a table.
        
        Input: None
        
        Output: Table with all of the unique combos.
        '''
                
        unique_combos = pd.DataFrame()
        for i in range(0,len(self.old_game)):
            row = self.old_game.iloc[i]
            sorted_rows = pd.DataFrame([sorted(row)])
            unique_combos = pd.concat([unique_combos,sorted_rows])
            unique_combos_sorted = unique_combos.groupby(unique_combos.columns.tolist(),as_index=False).size()
        return unique_combos_sorted
    
    def face_counts_per_roll(self,game):
        '''
        Purpose: Count the number of each face that was rolled for a given roll of all the die.
        
        Input: The already instantiated Die class.
        
        Output: Table consisting of the counts of each face rolled for a given dice roll.
        '''
        faces = game._die.values[:,0]
        face_counts = pd.DataFrame(columns = faces)
        for each in range(0,len(self.old_game)):
            row = self.old_game.iloc[each]
            my_list = []
            for i in faces:
                my_list.append(sum(row == i))
            face_counts.loc[each] = my_list 
        return face_counts
