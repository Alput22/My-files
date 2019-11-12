#%%
import pygame
import sys
import time
from Snek import Snaek
from Snakefood import Food

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500 + 20,500 + 20))
        pygame.display.set_caption("Snake Game")
        self.fps = pygame.time.Clock()
        self.score = 0 
        self.snake = Snaek()
        self.food = Food()
 
    def _checkEvents(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover()
         
                self.pressed = pygame.key.get_pressed()

                if self.pressed[pygame.K_RIGHT]:
                    self.snake.changeDirTo('RIGHT')
                elif self.pressed[pygame.K_LEFT]:
                    self.snake.changeDirTo('LEFT')
                elif self.pressed[pygame.K_UP]:
                    self.snake.changeDirTo('UP')
                elif self.pressed[pygame.K_DOWN]:
                    self.snake.changeDirTo('DOWN')
                elif self.pressed[pygame.K_ESCAPE]:
                    self.gameover()
            self._updateScreen()
    def _updateScreen(self):        
        foodPos = self.food.SpawnFood()
        if(self.snake.move(foodPos)==1):
            self.score+=1
            self.food.setFoodOnScreen(False)
 
        self.window.fill(pygame.Color(225,225,225))
        for x in range(0, 510, 10):     #Used to draw the walls and their colors
            pygame.draw.rect(self.window, (0,0,225), [x, 0, 10, 10])
            pygame.draw.rect(self.window, (0,0,225), [x, 510, 10, 10])
 
        for x in range(0, 510, 10):
            pygame.draw.rect(self.window, (0,0,225), [0, x, 10, 10])
            pygame.draw.rect(self.window, (0,0,225), [510, x, 10, 10])
 
        for pos in self.snake.getBody():    #Draws the snake and food along with their colors
            pygame.draw.rect(self.window,pygame.Color(0,125,0),pygame.Rect(pos[0],pos[1],10,10))
            pygame.draw.rect(self.window,pygame.Color(225,150,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
     
        if(self.snake.checkCollision()==1):  #If it returns 1 in checkCollision then game over
            self.gameover()
    
        pygame.display.set_caption("Snake | Score: " + str(self.score))
        pygame.display.flip()
        self.fps.tick(15)    #Used to control how fast the game runs
    def runGame(self):
        self._checkEvents()

    def gameover(self): #When it's game over it will display a text and quit the game
        self.font = pygame.font.SysFont('Candara', 30)
        self.score_text = self.font.render("Congrats you got " + str(self.score) + " points!",4,(255,0,0))
        self.window.blit(self.score_text,(100,250))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
        
if __name__ == "__main__":
    sg = SnakeGame()
    sg.runGame()