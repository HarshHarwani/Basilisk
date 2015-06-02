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
pygame.display.set_caption('Basilisk')
img=pygame.image.load ('snake.png')
block_size=2
snake_block_size=20
direction="right"
FPS=15
font=pygame.font.SysFont(None,25)

#this function returns the textSurface and rectange of the textSurface on which actual text is written.
def text_objects(text,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    

#this function takes a message and displays it to the screen.
def message(message,color,y_displace=0):
    textSurf,textRect=text_objects(message,color)
    textRect.center=(display_width/2,display_height/2+y_displace)
    gameDisplay.blit(textSurf,textRect)
    
#this funtion defines draws all elements of the snake,the elements are there in the sankeList
def snake(snake_block_size,snakeList):
        if direction=='right':
            head=pygame.transform.rotate(img,270)
        if direction=='left':
            head=pygame.transform.rotate(img,90)
        if direction=='up':
            head=img
        if direction=='down':
            head=pygame.transform.rotate(img,180)
        gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
        for element in snakeList[:-1]:
             pygame.draw.rect(gameDisplay,green,[element[0],element[1],snake_block_size,snake_block_size])


# Main Game Loop
def gameLoop():
    global direction
    gameExit=False
    gameOver=False
    crashedInto=False
    lead_x=display_width/2
    lead_y=display_height/2
    x_change=10
    y_change=0
    x_apple=round(random.randrange(0,display_width-snake_block_size))
    y_apple=round(random.randrange(0,display_height-snake_block_size))
    snakeList=[]
    snakeLength=1
    while not gameExit:
        while gameOver is True:
            gameDisplay.fill(white)
            if not crashedInto:
                message("Game Over",red,-50)
                message("Press C to play again or q to quit",black,50)
            if crashedInto:
                message("You crashed into yourself Broooo..!!",red,-50)
                message("Press C to play again or q to quit",black,50)
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
                    direction='left'
                elif event.key==pygame.K_RIGHT:
                    x_change=snake_block_size
                    y_change=0
                    direction='right'
                elif event.key==pygame.K_UP:
                    y_change=-snake_block_size
                    x_change=0
                    direction='up'
                elif event.key==pygame.K_DOWN:
                    y_change=snake_block_size
                    x_change=0
                    direction='down'
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
                crashedInto=True
        snake(snake_block_size,snakeList)
        pygame.display.update()
        if lead_x>=x_apple and lead_x<x_apple+snake_block_size or lead_x+snake_block_size>x_apple and lead_x+snake_block_size<x_apple+snake_block_size:
            if lead_y>=y_apple and lead_y<y_apple+snake_block_size or lead_y+snake_block_size>y_apple and lead_y+snake_block_size<y_apple+snake_block_size:
                x_apple=round(random.randrange(0,display_width-snake_block_size))
                y_apple=round(random.randrange(0,display_height-snake_block_size))
                snakeLength+=1
        clock.tick(FPS) 
    pygame.quit()
    quit()
gameLoop()
