#%%
import random

class Food():
    def __init__(self): #Setting the food in a random location
        self.position = [random.randint(4,46)*10,random.randint(4,46)*10]
        self.FoodOnScreen = True
 
    def SpawnFood(self):
        if self.FoodOnScreen == False:  #If the food is eaten then it will spawn again in another location
            self.position = [random.randrange(4,46)*10,random.randrange(4,46)*10]
            self.FoodOnScreen = True
        return self.position
     
    def setFoodOnScreen(self,b):
        self.FoodOnScreen = b