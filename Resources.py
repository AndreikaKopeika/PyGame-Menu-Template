DevMode = False # Dev mode... doesn't do much thing leave false
import pygame
import time
print('------------------------------------------------------------------------------')
print('Loading code dependencies...')

def LoadSomeThings(): # Importing all needed stuff (add what you need)
    loadstarttime = time.time()
    print('------------------------------------------------------------------------------')
    print('Loading BG...')
    BG = pygame.image.load('assets/Background.jpg') # Import BG
    print('BG loaded...')
    print('loading other assets...')
    button_image = pygame.image.load('assets/New Game Button.png') # Import button image
    print(f'Done in {round(time.time() - loadstarttime, 3)} seconds!') # delete if you want
    print('------------------------------------------------------------------------------')
    return BG, button_image # returning all imported things

def NewGameButtonAction(): # Button actions
    print('Buttonpress')
def LoadGameButtonAction(): # Placeholders
    pass
def SettingsButtonAction(): # Placeholders
    pass

class Button(): # button class for creating own buttons
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if DevMode:
                    print('Button click')
                self.clicked = True
                time.sleep(0.1)
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

print('Starting window...')

if DevMode == True: # Dev mode lets you set your own resolution
    SCREEN = pygame.display.set_mode((int(input('Height: ')), int(input('Width: '))))
else: 
    SCREEN = pygame.display.set_mode((1280, 720)) # 1280 720
pygame.display.set_caption('Super game')