#%%

class Snaek():
    def __init__(self):
        self.position = [100,50]    #The initial position and path of the snake
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        
 
    def changeDirTo(self,dir):  #Makes it so the snake can't turn to the opposite direction
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        elif dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        elif dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        elif dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"
         
    def move(self,foodPos): 
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + 10
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - 10
        elif self.direction == "UP":
            self.position[1] = self.position[1] - 10
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + 10
        self.body.insert(0,list(self.position)) #Add the new body when it moves
         
        if self.position == foodPos:
            return 1
        else:
            self.body.pop() #remove the last body
            return 0
 
     
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 20: #If it hits the walls then game over
            return 1 
        elif self.position[1] > 490 or self.position[1] < 20:
            return 1
        for part in self.body[1:]:  #If it hits the body then game over
            if self.position == part:
                return 1
        return 0
 
    def getHeadPosition(self):
        return self.position
     
    def getBody(self):
        return self.body
