from cProfile import run
from json import load
from msilib.schema import Class
from time import sleep
import pygame
import random
import math
from pygame import mixer

SIZE = 40

class Snake:
    def __init__(self,parent_surface,length):
        self.snaIMG  = pygame.image.load("bee.png")
        self.length = length
        self.x = 100
       
        self.y = 200

        self.parent_suraface = parent_surface
        self.direction = " "

    def draw_snake(self):
        for i in range(self.length):
            self.parent_suraface.blit(self.snaIMG,(self.x,self.y))

    def updir(self):
        self.direction = "up"
    
    def downdir(self):
        self.direction = "down"
    
    def leftdir(self):
        self.direction = "left"
    
    def rightdir(self):
        self.direction = "right"


    def walking(self):
        
        if self.direction is "up":
            self.y -= 0.1
            self.draw_snake()
        
        if self.direction is "down":
            self.y += 0.1
            self.draw_snake()
        
        if self.direction is "left":
            self.x -= 0.1
            self.draw_snake()
        
        if self.direction is "right":
            self.x += 0.1
            self.draw_snake()
        
class Apple:
    def __init__(self,surface):
        self.appleicon = pygame.image.load("apple.png")
        self.surface = surface
        self.x= random.randint(200,500)
        self.y = random.randint(200,500)

    
    def draw_apple(self):
        self.surface.blit(self.appleicon,(self.x,self.y))

        
class Collison:
    def __init__(self):
        
        self.score = 0
        
    def is_collison(self,x1,x2,y1,y2):
        self.x1,self.x2,self.y1,self.y2 = x1,x2,y1,y2
        
        self.distance = math.sqrt((math.pow(self.x1-self.x2,2))+(math.pow(self.y2-self.y1,2)))
        
        
        if self.distance < 50:
            return True
        else:
            return False

            
          



    
        
        


        
        
    

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Bumble")
        self.icon = pygame.image.load("beeico.png")
        pygame.display.set_icon(self.icon)
        self.snake = Snake(self.surface,3)
        self.apple = Apple(self.surface)
        self.collison = Collison()
        self.score = 0
        self.scoretext = pygame.font.Font("freesansbold.ttf",32)
        self.gameovertext = pygame.font.Font("freesansbold.ttf",50)
        mixer.music.load('back.mp3')
        mixer.music.play()
        
        


        
    def run(self):
        Run = True

        while Run:
            self.surface.fill((124,255,0))
            self.snake.draw_snake()
            self.apple.draw_apple()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Run = False
                    if event.key == pygame.K_UP:
                        self.snake.updir()
                    if event.key == pygame.K_DOWN:
                        self.snake.downdir()
                    if event.key == pygame.K_LEFT:
                        self.snake.leftdir()
                    if event.key == pygame.K_RIGHT:
                        self.snake.rightdir()
            
            self.snake.walking()
            if self.snake.x <=0 or self.snake.x >= 800 or self.snake.y <=0 or self.snake.y >=600:
                self.gametextrender = self.gameovertext.render("GAMEOVER",True,(255,255,255))
                self.surface.blit(self.gametextrender,(250,190))
                self.apple.x = 2000



            state = self.collison.is_collison(self.snake.x,self.apple.x,self.snake.y,self.apple.y)
            if state:
                to = mixer.Sound('explosion.wav')
                to.play()
                self.score += 1
                self.apple.x= random.randint(200,500)
                self.apple.y = random.randint(200,500)
            self.scoretextrender = self.scoretext.render("Score:"+str(self.score),True,(255,255,255))
            self.surface.blit(self.scoretextrender,(10,10))
          
                

                    
            pygame.display.update()
        


    

      

if __name__ == "__main__":
    game = Game()
    game.run()
   

