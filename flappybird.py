import pygame
from sys import exit
import random

game_width = 360
game_Height = 640

# setting mannie bird xD
bird_x = game_width/8
bird_y = game_Height/2
bird_width = 34
brid_height = 24

class Bird (pygame.Rect):
   def __init__(self , img):
      pygame.Rect.__init__(self ,bird_x  ,bird_y , bird_width , brid_height)
      self.img = img 
    

pipe_x = game_width
pipe_y = 0
pipe_width = 64
pipe_height = 512


class Pipe(pygame.Rect):
   def __init__(self,img):
      pygame.Rect.__init__(self,pipe_x,pipe_y,pipe_width,pipe_height)
      self.img = img 
      self.passed = False


#game images
background_image = pygame.image.load("flappybirdbg.png")
bird_image = pygame.image.load("flappybird.png")
bird_image = pygame.transform.scale(bird_image,(bird_width, brid_height))
top_pipe_img = pygame.image.load("toppipe.png")
top_pipe_img = pygame.transform.scale(top_pipe_img, (pipe_width, pipe_height))
bottom_pipe_img = pygame.image.load("bottompipe.png")
bottom_pipe_img = pygame.transform.scale(bottom_pipe_img, (pipe_width , pipe_height))



#logic
bird = Bird(bird_image)
pipes = []
velocity_x = -2 # dx/dt move pipes to the left speed (sim bird moving right)
velocity_y = 0 #BIRDIE Movement
gravity = 0.4
score = 0
GAME_OVER = False

def draw():
   window.blit(background_image, (0,0) )
   window.blit(bird_image , bird)



   for pipe in pipes :
      window.blit(pipe.img , pipe)

    


   text_str = str(int(score))
   if GAME_OVER:
      text_str = "MaNn Over " + text_str
      
   text_font = pygame.font.SysFont("Comic Sans MS" , 45)
   text_render = text_font.render(text_str , True, "black")
   window.blit(text_render,(5,0))
    

 
def move():
   global velocity_y,score,GAME_OVER
   velocity_y += gravity 
   bird.y += velocity_y
   bird.y = max(bird.y,0)

   if bird.y > game_Height :
      GAME_OVER = True
      return 





   
   for pipe in pipes :
      pipe.x += velocity_x


      if not pipe.passed and bird.x > pipe.x + pipe_width:
          score += 0.5 #because 2pipes 0.5+0.5 = 1
          pipe.passed = True
  
      if bird.colliderect(pipe):
         GAME_OVER = True
         return

   while len(pipes) > 0 and pipes[0].x < - pipe_width:
      pipes.pop(0) #remove pipe which birdie cleared

      
      
         
      

def create_pipes():
    random_pipe_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2)
    opening_space = game_Height/4

    top_pipe = Pipe(top_pipe_img)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_img )
    bottom_pipe.y = top_pipe.y + pipe_height + opening_space
    pipes.append(bottom_pipe)




    print(len(pipes))




pygame.init()
window = pygame.display.set_mode((game_width,game_Height))
pygame.display.set_caption("Manny Bird") #MAnn is my name lol
clock = pygame.time.Clock()

create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer,1500) #marks every 1.5se





while True: #game loop inmaking
   for event in pygame.event.get():
      if event.type == pygame.QUIT :
         pygame.quit()
         exit()
      if event.type == create_pipes_timer and not GAME_OVER:
         create_pipes()
         
      if event.type == pygame.KEYDOWN:
          if event.key in ( pygame.K_SPACE , pygame.K_x, pygame.K_UP):
              velocity_y = -5

              #reset game 
              if GAME_OVER:
                 bird.y = bird_y
                 pipes.clear()
                 score = 0 
                 GAME_OVER = False
   


   if not GAME_OVER : 
      
      move()     
      draw()
      pygame.display.update()

      clock.tick(60) #60fps



  
   
