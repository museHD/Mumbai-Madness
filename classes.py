#-----IMPORT LIBRARIES-----#

import pygame
import os
import time

#-----MAIN PLAYER CAR OBJECT FOR DODGE GAME-----#
#pygame.init()
class player(pygame.sprite.Sprite):
    pSprite = pygame.image.load(os.path.join('images', 'car.png')).convert_alpha()
    pImg = pygame.Surface((129,264)).convert_alpha()
    pygame.transform.scale(pSprite, (129,264),pImg)

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.boost = False
        self.movingL = False
        self.movingR = False
        self.slow = False
        

    def draw(self, win):
        win.blit(self.pImg,(self.x,self.y))
        self.hitbox = (self.x+5, self.y, 115, 255)
        
        #---MOVE CAR RIGHT BY 15---#

        if self.slow == True:
            carSpeed = 10
            
        elif self.slow == False:
            carSpeed = 18
        if self.movingR:
            self.x += carSpeed
            self.movingR = False
            if self.slow == True:
                self.hitbox = (self.x-5, self.y, 115,255)
            elif self.slow == False:
                self.hitbox = (self.x-13, self.y, 115,255)

     
        #---MOVE CAR LEFT BY 15---#
            
        elif self.movingL:
            self.x -= carSpeed
            self.movingL = False
            if self.slow == True:
                self.hitbox = (self.x+15, self.y, 115,255)
            elif self.slow == False:
                self.hitbox = (self.x+23, self.y, 115, 255)
        #---MOVE CAR LEFT BY 15 IF X VAL IS NEGATIVE---#
        self.slow = False    
        while self.x < 25:
            self.x = self.x + carSpeed

        #---MOVE CAR RIGHT BY 15 IF X VAL IS > WINDOW---#
        while 890 < self.x:
            self.x = self.x - carSpeed

        #pygame.draw.rect(win,(0,255,0),self.hitbox,2) #--- DRAWING HITBOXES

#-----HOLES FOR DODGE-----#
        
class hole(object):

    hSprite = pygame.image.load(os.path.join('images', 'hole.png')).convert_alpha()
    hImg = pygame.Surface((150, 175)).convert_alpha()
    pygame.transform.scale(hSprite, (150,175), hImg)
    
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width-10,height-10)

    def draw(self, win):
        self.hitbox = (self.x + 25, self.y + 35 , 110, 110)
        win.blit(self.hImg, (self.x, self.y))
        #pygame.draw.rect(win ,(255,0,0), self.hitbox, 2) <-----# DRAW HOLE HITBOX

    def collide(self, rect):
       
        # rect[0] is X of player; rect[2] is width of player
        #self.hitbox[0] is x of obj; self.hitbox[2] is width of obj

        self.xval = self.hitbox[0] + self.hitbox[2]
        self.yval = self.hitbox[1] + self.hitbox[3]
        
        

            # rect[1] is player y pos; rect[3] is height of player
        if self.hitbox[1] < rect[1] + rect[3] < self.yval or self.hitbox[1] < rect[1] <self.yval :
            if self.xval > rect[0] + 2 > self.hitbox[0] or self.hitbox[0] < rect[0] + rect [2] < self.xval:
                return True

        return False
            
class txtBtn(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, text, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        try:
            self.useFont = pygame.font.Font('fonts/%s'%(self.font),self.height)
        except:
            self.useFont = pygame.font.SysFont('Arial', self.height)
        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()        
    def draw(self, win):
        
        self.measure = self.useFont.render(self.text, True, (1,1,1))
        measureWidth = self.measure.get_width()        
        activate = False
        mouseX,mouseY = pygame.mouse.get_pos()
        if self.x - measureWidth/2 < mouseX < self.x + measureWidth/2 and self.y < mouseY < self.y + self.height:
            colour = (255,255,255)
            activate = True
        else:
            colour = (0, 0, 0)
            activate = False
        if self.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            #print("detected!")
            pass

        self.button = self.useFont.render(self.text, True, colour)
        win.blit(self.button, (self.x-measureWidth/2,self.y))
        btnWidth = self.button.get_width()

    def hoverCheck(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        self.measureHOVER = self.useFont.render(self.text, True, (1,1,1))
        measureWidthHOVER = self.measure.get_width()               
        if self.x - measureWidthHOVER/2< mouseX < self.x + measureWidthHOVER/2 and self.y < mouseY < self.y + self.height:
            return True
        else:
            return False