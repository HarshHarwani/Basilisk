import pygame
import time
import random
pygame.init()
#Declaring all the variables
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
block_size=2
snake_block_size=10
FPS=15
font=pygame.font.SysFont(None,25)
###

#this function takes a message and displays it to the screen.
def message(message,color):
    screen_text=font.render(message,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])

def snake(snake_block_size,snakeList):
        for element in snakeList:
             pygame.draw.rect(gameDisplay,green,[element[0],element[1],snake_block_size,snake_block_size])

def gameLoop():
    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2
    x_change=0
    y_change=0
    x_apple=round(random.randrange(0,display_width-snake_block_size)/10.0)*10.0
    y_apple=round(random.randrange(0,display_height-snake_block_size)/10.0)*10.0
    snakeList=[]
    snakeLength=1
    while not gameExit:
        while gameOver is True:
            gameDisplay.fill(white)
            message("Game Over,Press C to play again or q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-snake_block_size
                    y_change=0
                elif event.key==pygame.K_RIGHT:
                    x_change=snake_block_size
                    y_change=0
                elif event.key==pygame.K_UP:
                    y_change=-snake_block_size
                    x_change=0
                elif event.key==pygame.K_DOWN:
                    y_change=snake_block_size
                    x_change=0
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
        lead_x+=x_change
        lead_y+=y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,[x_apple,y_apple,snake_block_size,snake_block_size])
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]
        for element in snakeList[:-1]:
            if element==snakeHead:
                gameOver=True
        snake(snake_block_size,snakeList)
        pygame.display.update()
        if lead_x==x_apple and lead_y==y_apple:
            x_apple=round(random.randrange(0,display_width-snake_block_size)/10.0)*10.0
            y_apple=round(random.randrange(0,display_height-snake_block_size)/10.0)*10.0
            snakeLength+=1
        clock.tick(FPS) 
    pygame.quit()
    quit()

gameLoop()
