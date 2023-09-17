#Partially Completed Paint Program
#Created By Dr. Mo on 11/2019



import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("dunking game")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
clock = pygame.time.Clock() #set up clock

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
click = False

#ball variables
ballx = 200
bally = 200

bVx = 3
bVy = 5

madeGoal = False


#gameloop###################################################
while madeGoal == False:

    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        click = True

    if event.type == pygame.MOUSEBUTTONUP:
        click = False

        
    #physics Section------------------------------
    

        
    #reset ball's position to left side if it goes off the right
    if ballx  > 830:
        ballx = -30
    
    #bounce ball up if mouse is clicked
    if click == True:
        bVy = -8
        click = False
        bVx = 3
    else:
        bVy += .5 #gravity
    
    #collision with basket
    if ballx > 730 and ballx <770 and bally >300 and bally<350:
        print("Goal!")
        madeGoal = True
    
    elif ballx > 700 and ballx<800 and bally >300 and bally <350:
        bVx *=-1
        bVy *=-1
        
    
    

    #update ball position
    ballx += bVx
    bally += bVy
    
    #don't let ball go through floor
    if bally + 30 > 800:
        bally = 800 - 30
    
 
    #render section---------------------------------------------
    screen.fill((0,0,0)) #wipe screen black
    
    
    #the "basket"

    pygame.draw.rect(screen, (0,100,200), (700, 300,200,50))

    
    #the ball
    pygame.draw.circle(screen, (200, 100, 0), (ballx, bally),30)


        
    pygame.display.flip()
    

#end game loop##############################################

screen.fill((200,200,0)) #wipe screen black
print("GOAL!")

pygame.draw.rect(screen, (0,100,200), (700, 300,200,50))

pygame.draw.circle(screen, (200, 100, 0), (ballx, bally),30)

pygame.display.flip()
pygame.time.delay(5000)

pygame.quit()

