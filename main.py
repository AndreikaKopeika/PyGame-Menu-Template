# Game menu template go to resources to change button actions
from Resources import *

print('Starting game...')
pygame.init() # starting menu

BG, button_image = LoadSomeThings() #loading BG and button img

start_button = Button(350, 200, button_image, 0.5) # you can do it for your own buttons
run = True 
while run: # run while not closed
    SCREEN.blit(BG, (0,0))
    if start_button.draw() == True: # draw button returns True when you press it
        NewGameButtonAction() # Button action go to resources 19 to change action
    for event in pygame.event.get(): # get event
        if event.type == pygame.QUIT: # if event == quit run = False
            run = False
    pygame.display.update() # updating game

pygame.quit() # closing game