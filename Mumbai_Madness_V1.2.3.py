import pygame #Main module
from pygame.locals import*
import time
import os
import sys
import random
import pickle
import pygame_textinput


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()

clock.tick(60)

win = pygame.display.set_mode((1024,768),pygame.NOFRAME)
pygame.display.set_caption("Mumbai Madness v1.2.3")
icon = pygame.image.load(os.path.join('images', 'icon.jpg'))

pygame.display.set_icon(icon)

splashFont = pygame.font.Font('fonts/splashFont.ttf',65)
loading = splashFont.render("Loading...",True,(255,255,255))
win.blit(loading,(512-loading.get_width()/2,384-loading.get_height()/2))
splashP = pygame.image.load(os.path.join("images", "splash.png")).convert()

pygame.display.update()
time.sleep(0.8)

def fadeIn():
    pygame.time.delay(500)
    blankSurf = pygame.Surface((1024,768))
    blankSurf.fill((255,255,255))
    blankSurf.set_alpha(150)
    for h in range(0,255,5):
        blankSurf.set_alpha(h)
        pygame.display.flip()
        #clock.tick(60)
        win.blit(blankSurf,(0,0))
        pygame.event.pump()
        
def splashScreen():
    pygame.event.pump()
    clock.tick(60)
    splashTxt = splashFont.render("museHD's",True,(255,255,255))
    splash = pygame.Surface((1024,768)).convert()
    pygame.transform.scale(splashP, (1024,768), splash)
    splash.set_alpha(0)
    
    pygame.mixer.music.load('note1.mp3')
    pygame.mixer.music.play()
    txtSurf = pygame.Surface((1024,768)).convert()
    txtSurf.blit(splashTxt, (0,0))
    txtSurf.set_alpha(0)

    for x in range(255):
        pygame.event.pump()
        txtSurf.set_alpha(x)
        win.blit(txtSurf, (512 - splashTxt.get_width()/2, 200))
        pygame.display.flip()

    
    pygame.display.update()
    pygame.time.wait(1000)
    
    pygame.mixer.music.load('note1.mp3')
    pygame.mixer.music.play()




    for x in range(255):
        pygame.event.pump()
        splash.set_alpha(x)
        win.blit(splash,(0,0))
        win.blit(splashTxt, (512 - splashTxt.get_width()/2, 200))
        pygame.display.flip()

    win.blit(splash,(0,0))
    win.blit(splashTxt, (512 - splashTxt.get_width()/2, 200))
    pygame.display.update()
    

    pygame.display.flip()
    pygame.mixer.music.load('menu.mp3')




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
            self.useFont = pygame.font.SysFont('Arial',self.height)
        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()
        
    def draw(self, win):
        
        self.measure = self.useFont.render(self.text, True, (1,1,1))
        measureWidth = self.measure.get_width()        
        activate = False
        mouseX,mouseY = pygame.mouse.get_pos()
        if self.x - measureWidth/2 < mouseX < self.x + measureWidth/2 and self.y < mouseY < self.y + self.height:
            colour = (0,0,0)
            activate = True
        else:
            colour = (255,255,255)
            activate = False
        if self.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            #print("bosh") --- FOR TESTING; 18.10.19: WORKS
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

try:
    txtFont = pygame.font.Font('fonts/Fox Cavalier.otf', 60)
except:
    txtFont = pygame.font.SysFont('Arial',60)


     
#-----OBJECT CLASS FOR HIGH SCORE RECORDS. 3 IN USE-----#
        
class record(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    #---REPRESENTS CLASS VARIABLES EVERYWHERE ELSE---#
        
    def __repr__(self):
        return repr((self.name, self.score))
try:
    with open('data_01.dat','rb') as sav:
        players = pickle.load(sav)
        scores = pickle.load(sav)
        Top = pickle.load(sav)
        Mid = pickle.load(sav)
        Low = pickle.load(sav)
        print(scores)
        print(players)

    #scores = scores[0:2]
except:

    Top = record(" ",1)
    Mid = record(" ",2)
    Low = record(" ",3)
    scores = [Top.score, Mid.score, Low.score]
    players = [Top,Mid,Low]

#-----OBJECT CLASS FOR BUTTONS MADE FROM IMAGES. NAME BOTH IMG FILES WITH SAME-----#
#-----NAME AND ADD A '1' OR '2' AT THE END OF THEIR NAMES FOR HIGHLIGHTING-----#

    
class button(object):

    def __init__(self, x, y, width, height, image, win):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.surface = pygame.Surface((self.width, self.height)).convert_alpha
        self.load = pygame.image.load(os.path.join("images", "%s%s.png" % (str(self.image), str(2)))).convert_alpha()
        self.load = pygame.transform.smoothscale(self.load, (self.width, self.height))
        self.surface = pygame.transform.smoothscale(self.load, (self.width,self.height))
        self.load2 = pygame.image.load(os.path.join("images", "%s%s.png" % (str(self.image), str(1)))).convert_alpha()
        self.load2 = pygame.transform.smoothscale(self.load2, (self.width, self.height))

    #---CHECKS IF MOUSE POSITION COLLIDES WITH THE IMAGE---#  

    def hoverCheck(self):
        mX, mY = pygame.mouse.get_pos()
        
        if self.x < mX < self.x + self.width and self.y < mY <self.y + self.height:
            return True
        else:
            return False

    #---DRAW THE BUTTON---#
        
    def draw(self,win):
        self.hoverCheck()

        #---IF  MOUSE IS HOVERING OVER BUTTON---#
        
        if self.hoverCheck() == True:

            win.blit(self.load, (self.x, self.y))
        
        else:
                    
            win.blit(self.load2, (self.x,self.y))
            


play = button(25,100,250,100,"play", win)
instruction = button(25,225,500,100,"instruction",win)
high = button(25,350,500,100,"high", win)
info = button(25,475,250,100,"info",win)
exitButton = button(25,600,250,100,"exit",win)

MENUbg = pygame.image.load(os.path.join("images", "menuBG.png"))
hsBG = pygame.image.load(os.path.join("images", "highScoreBG.png"))
MENUbg = pygame.transform.smoothscale(MENUbg, (1024,768))
htp1 = pygame.image.load(os.path.join("images", "controlsBG.png"))
htp2 = pygame.image.load(os.path.join("images", "instructionBG.png"))

def drawButtons():
    play.draw(win)
    instruction.draw(win)
    high.draw(win)
    info.draw(win)
    exitButton.draw(win)

def fadeInBlack():
    blankSurf = pygame.Surface((1024,768))
    blankSurf.fill((0,0,0))
    blankSurf.set_alpha(0)
    for h in range(0,255,5):
        blankSurf.set_alpha(h)
        pygame.display.flip()
        #clock.tick(60)
        win.blit(blankSurf,(0,0))


def fadeToMain():
    blankSurf = pygame.Surface((1024,768))
    blankSurf.fill((255,255,255))
    blankSurf.set_alpha(255)

    win.blit(blankSurf,(0,0))

    for x in range(255,0,-20):

        win.blit(MENUbg,(0,0))
        drawButtons()
        blankSurf.set_alpha(x)

        #time.delay(0.02)
        clock.tick(60)

        win.blit(blankSurf,(0,0))
        pygame.display.flip()

def fadeToGame():
    pass
       
def exitLOOP():

    exitON = True
    while exitON == True:

        whiteInside = pygame.Surface((512,384))
        blackBorder = pygame.Surface((522,394))
        whiteInside.fill((150,150,150))
        blackBorder.fill((0,0,0))
        exitTxt1 = "Are you sure"
        exitTxt2 = "you want"
        txtExit1 = txtFont.render(exitTxt1, True,(255,255,255))
        txtExit2 = txtFont.render(exitTxt2, True,(255,255,255))
        exitTxt3 = "to exit?"
        txtExit3 = txtFont.render(exitTxt3, True,(255,255,255))

        win.blit(blackBorder,(256,192))
        win.blit(whiteInside,(261,197))
        win.blit(txtExit1,(270,200))
        win.blit(txtExit2,(350,250))
        win.blit(txtExit3,(350,300))
        
        yesBtn = txtBtn(360,470,50,70,'yes', 'Fox Cavalier.otf')
        yesBtn.draw(win)

        noBtn = txtBtn(670,470,50,70,'no', 'Fox Cavalier.otf')
        noBtn.draw(win)

        pygame.display.update()
        
        for event in pygame.event.get():

            if yesBtn.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
                               
            if noBtn.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                exitON = False
                
def hsLOOP():

    
    backBtn = txtBtn(140,40,75,50,'back','Fox Cavalier.otf')

    topScore = txtFont.render(Top.name + '  -  ' + str(Top.score), True,(0,0,0))
    midScore = txtFont.render(Mid.name + '  -  ' + str(Mid.score), True,(0,0,0))
    lowScore = txtFont.render(Low.name + '  -  ' + str(Low.score), True,(0,0,0))
    win.blit(hsBG, (0,0))
    win.blit(topScore,(50,50))
    win.blit(midScore,(50,100))
    win.blit(lowScore,(50,150))

    print(scores)
    print(players)
    
    runHS = True
    while runHS == True:
        win.blit(hsBG, (0,0))
        backBtn.draw(win)
        win.blit(topScore,(175,245))
        win.blit(midScore,(175,425))
        win.blit(lowScore,(175,600))
    

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if backBtn.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                runHS = False
            
        pygame.display.update()
    fadeIn()
    fadeToMain()

def htpLOOP():
    
    win.blit(htp1,(0,0))
    backBtn = txtBtn(140,35,75,50,'back','Fox Cavalier.otf')
    nxtBtn = txtBtn(762,655,75,50,'next','Fox Cavalier.otf')
    win.blit(htp1,(0,0))
    nxtBtn.draw(win)
    backBtn.draw(win)
    runHTP = True
    while runHTP == True:
        clock.tick(60)
        pygame.display.update()
        win.blit(htp1,(0,0))
        backBtn.draw(win)
        nxtBtn.draw(win)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if backBtn.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                runHTP = False
                fadeIn()
                fadeToMain()

            if nxtBtn.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                fadeIn()
                backBtn2 = txtBtn(250,650,75,50,'back','Fox Cavalier.otf')
                blankSurf = pygame.Surface((1024,768))
                blankSurf.fill((255,255,255))
                blankSurf.set_alpha(255)

                win.blit(blankSurf,(0,0))

                for x in range(255,0,-20):

                    win.blit(htp2,(0,0))
                    backBtn2.draw(win)
                    blankSurf.set_alpha(x)

                    clock.tick(60)

                    win.blit(blankSurf,(0,0))
                    pygame.display.update()

                runHTP2 = True
                while runHTP2 == True:
                    win.blit(htp2,(0,0))
                    playNow = button(700,635,250,85,"play", win)
                    playNow.draw(win)
                    backBtn2.draw(win)
                    pygame.display.update()

                    
                    for event in pygame.event.get():
                        
                        if playNow.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                            HTP2 = False
                            HTP = False
                            mainGame()
                        if event.type == pygame.QUIT:
                            runHTP2 = False
                            pygame.quit()
                            sys.exit()
                        if backBtn2.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
                            runHTP2 = False
                            pygame.display.update()
                            fadeIn()
                            
                            blankSurf.set_alpha(255)

                            win.blit(blankSurf,(0,0))

                            for x in range(255,0,-20):

                                win.blit(htp1,(0,0))
                                backBtn.draw(win)
                                nxtBtn.draw(win)
                                blankSurf.set_alpha(x)

                                clock.tick(60)

                                win.blit(blankSurf,(0,0))
                                pygame.display.update()

                    pygame.display.update()
                    clock.tick(60)

def fadeInText(text,y=200):
    text = splashFont.render(str(text),True,(255,255,255))

    txtSurff = pygame.Surface((1024,768)).convert()
    txtSurff.blit(text, (0,0))
    txtSurff.set_alpha(0)

    for x in range(255):
        pygame.event.pump()
        txtSurff.set_alpha(x)
        win.blit(txtSurff, (512 - text.get_width()/2, y))
        pygame.display.flip()


def infoLOOP():
    pygame.mixer.music.fadeout(1)
    pygame.mixer.music.load('info.mp3')
    pygame.mixer.music.play()
    fadeInBlack()

    pygame.event.pump()
    
    fadeInBlack()
    fadeInText('Inspired By Tech With Tim')
    time.sleep(1.5)
    fadeInBlack()
    fadeInText('Art by: Openartgame')
    fadeInText('kissClipart',300)
    fadeInText('FreePik',400)
    time.sleep(1)
    fadeInBlack()
    fadeInText('Created with Pygame')
    fadeInText('In Python',300)
    time.sleep(1)
    fadeInBlack()
    fadeInText('As a Year 9 IST Assignment',300)
    time.sleep(1)
    fadeInBlack()
    fadeInText('MuseHD Studios Presents')
    time.sleep(1)
    fadeInBlack()
    fadeInText('A MuseHD Production')
    time.sleep(1)
    fadeInBlack()
    pygame.event.pump()
    clock.tick(60)
    splashTxt = splashFont.render("MuseHD's",True,(255,255,255))
    #splashP = pygame.image.load(os.path.join("images", "splash.png")).convert()
    splash = pygame.Surface((1024,768)).convert()
    pygame.transform.scale(splashP, (1024,768), splash)
    splash.set_alpha(0)
    
    txtSurf = pygame.Surface((1024,768)).convert()
    txtSurf.blit(splashTxt, (0,0))
    txtSurf.set_alpha(0)

    for x in range(255):
        pygame.event.pump()
        txtSurf.set_alpha(x)
        win.blit(txtSurf, (512 - splashTxt.get_width()/2, 200))
        pygame.display.flip()

    
    pygame.display.update()
    #time.sleep(0.2)
    #pygame.time.wait(300)
    

    for x in range(255):
        pygame.event.pump()
        splash.set_alpha(x)
        win.blit(splash,(0,0))
        win.blit(splashTxt, (512 - splashTxt.get_width()/2, 200))
        pygame.display.flip()

    win.blit(splash,(0,0))
    win.blit(splashTxt, (512 - splashTxt.get_width()/2, 200))
    pygame.display.update()
    pygame.time.wait(1500)
    fadeInBlack()
    fadeInText('Credits Music:')
    fadeInText('Overwatch League',300)
    fadeInText('All Stars Theme',400)
    pygame.time.wait(1000)
    fadeInBlack()
    fadeInText('Splash Screen Music:')
    fadeInText('Walking the Wire',300)
    pygame.time.wait(1000)
    fadeInBlack()
    fadeInText('Main Menu Music:')
    fadeInText('SynthWave Part 1',300)
    pygame.time.wait(1000)
    fadeInBlack()
    pygame.mixer.music.fadeout(3000)
    time.sleep(5)
    fadeIn()
    pygame.event.pump()
    fadeToMain()
    pygame.mixer.music.load('menu.mp3')
    

    
    
    
def fadeToHS():
    blankSurf2 = pygame.Surface((1024,768))
    blankSurf2.fill((255,255,255))
    blankSurf2.set_alpha(255)
    topScore = txtFont.render(Top.name + '  -  ' + str(Top.score), True,(0,0,0))
    midScore = txtFont.render(Mid.name + '  -  ' + str(Mid.score), True,(0,0,0))
    lowScore = txtFont.render(Low.name + '  -  ' + str(Low.score), True,(0,0,0))
    backBtn = txtBtn(140,40,75,50,'back','Fox Cavalier.otf')
    hsBG.set_alpha(0)
    win.blit(hsBG,(0,0))
    win.blit(topScore,(175,245))
    win.blit(midScore,(175,425))
    win.blit(lowScore,(175,600))

    backBtn.draw(win)

    for x in range(0,255,10):

        hsBG.set_alpha(x)
        clock.tick(60)
        
        win.blit(hsBG,(0,0))
        win.blit(topScore,(175,245))
        win.blit(midScore,(175,425))
        win.blit(lowScore,(175,600))

        backBtn.draw(win)
        pygame.display.update()

def fadeToHTP():
    
    blankSurf2 = pygame.Surface((1024,768))
    blankSurf2.fill((255,255,255))
    blankSurf2.set_alpha(255)
    backBtn = txtBtn(140,35,75,50,'back','Fox Cavalier.otf')
    nxtBtn = txtBtn(762,655,75,50,'next','Fox Cavalier.otf')  
    htp1.set_alpha(0)
    win.blit(htp1,(0,0))
    backBtn.draw(win)

    for x in range(0,255,10):

        htp1.set_alpha(x)
        clock.tick(60)

        win.blit(htp1,(0,0))
        nxtBtn.draw(win)
        backBtn.draw(win)
        pygame.display.flip()
        
def Update():
    
    win.blit(MENUbg, (0,0))
    drawButtons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
        if high.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            fadeIn()
            fadeToHS()
            hsLOOP()

        if exitButton.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            exitLOOP()
            
        if play.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            mainGame()

        if instruction.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            fadeIn()
            fadeToHTP()
            htpLOOP()
        if info.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:
            #fadeInBlack()
            infoLOOP()
    pygame.display.update()

def mainGame():
    global objects, score, calc_speed, iterator
    calc_speed = 1.6
    iterator = 1
    score = 0
    objects = []
    objects.clear()
 
    WIN_WIDTH = 1024
    WIN_HEIGHT = 768
    bg = pygame.image.load(os.path.join('images', 'road.png')).convert()
    bg2 = pygame.image.load(os.path.join('images', 'road.png')).convert()
    bg = pygame.transform.scale(bg,(1024,768))
    bg2 = pygame.transform.scale(bg2, (1024,768))

    # v experimenting v #

    rect1 = bg.get_rect()
    rect2 = bg2.get_rect()

    bgY = 0
    bgY2 = bg.get_height()

    clock = pygame.time.Clock()
    iterator = 1
    speed = 60

    #-----CLASSES-----#
    import classes
    obstacle = classes.hole
    
    #-----FUNCTIONS-----#

    def resetDodge():
        
        global objects, score, calc_speed, iterator
        calc_speed = 1.6
        iterator = 1
        score = 0
        objects.clear()
        car.boost = False
        car.x = 450

    def newHigh():
        try:
            hsFont = pygame.font.Font('fonts/Fox Cavalier.otf', 45)
            smallFont = pygame.font.Font('fonts/Fox Cavalier.otf', 30)
        except:
            hsFont = pygame.font.SysFont('Arial',45)
            smallFont = pygame.font.SysFont('Arial',30)

        newHighSurface = pygame.Surface((1024,768))
        newHighSurface.fill((255,43,0))
        win.blit(newHighSurface,(0,0))
        try:
            nameInput = pygame_textinput.TextInput('','fonts/Fox Cavalier.otf',80,True,(0,0,0),(20,20,20),300,45)
        except:
            nameInput = pygame_textinput.TextInput('','Arial',80,True,(0,0,0),(20,20,20),300,45)

        hsText1 = "Congrats! Your score of %d" %(score)
        hsText2 = "made it to the leaderboard!"
        enterText = "Please enter your name:"
        maxChar = "(10 characters max)"
        wrongName = "invalid name. Please try again"
        
        invalidNameDisplay = smallFont.render(wrongName, True,(255,255,255))
        
        newHsClock = pygame.time.Clock()
        newHS = True
        while newHS == True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            if nameInput.update(events):
                newHighName = (nameInput.get_text())
                #print(len(newHighName))
                if len(newHighName) < 11:
                    win.blit(newHighSurface,(0,0))
                    hsSaved = txtFont.render("High Score Saved,", True, (255,255,255))
                    blitName = txtFont.render(newHighName + '!',True,(255,255,255))
                    win.blit(blitName,(512 - blitName.get_width()/2,415))
                    win.blit(hsSaved,(512 - hsSaved.get_width()/2, 350))
                    pygame.display.update()
                    time.sleep(3.5)
                    return newHighName
                elif len(newHighName)> 11:
                    win.blit(invalidNameDisplay,(512 - invalidNameDisplay.get_width()/2,450))
                    pygame.display.update()
                    time.sleep(2)

            hsDisplayText1 = hsFont.render(hsText1, True,(255,255,255))
            hsDisplayText2 = hsFont.render(hsText2, True,(255,255,255))
            nameAskDisplay = hsFont.render(enterText, True,(255,255,255))
            maxCharDisplay = smallFont.render(maxChar, True,(255,255,255))
            
            win.blit(newHighSurface,(0,0))
            win.blit(hsDisplayText1, (1024/2 - hsDisplayText1.get_width()/2,50))
            win.blit(hsDisplayText2, (512 - hsDisplayText2.get_width()/2,100))
            win.blit(nameAskDisplay, (512 - nameAskDisplay.get_width()/2,250))
            win.blit(maxCharDisplay, (512 - maxCharDisplay.get_width()/2,300))
            win.blit(nameInput.get_surface(),(512 - nameInput.get_surface().get_width()/2,350))
            
            pygame.display.update()
            newHsClock.tick(15)

    def endScreen():


        messages = ["P'wned", "you ded", "Unlucky...", "Better luck next time", "oof!", "Big bOOm!", "Byron Distracted You", "Nice try", "You Crashed", "Creeper...Aw Man"]
        randomPicker = random.randint(0,len(messages)-1)        
        deathMsg = messages[randomPicker]
        deathMsg = str(deathMsg)
    #    print(deathMsg)

        if score > Low.score:
            
            scores.append(score)
            scores.sort()
            scores.reverse()

            Top.score = scores[0]
            Mid.score = scores[1]
            Low.score = scores[2]
           # print(scores)
           # print(players)
            
            newHighName = str(newHigh())

            if score == Top.score:
                Low.name = Mid.name
                Mid.name = Top.name
                Top.name = newHighName
                Mid.name = Mid.name
                Mid.Score = scores[1]
                Low.name = Low.name
                Low.Score = scores[2]
                
                
            elif score == Mid.score:
                Low.name = Mid.name
                #Mid.name = Top.name
                Mid.name = newHighName
                Top.name = Top.name
                Top.Score = scores[0]
                Low.name = Low.name
                Low.Score = scores[2]
                
            elif score == Low.score:
                            #Low.name = Mid.name
               # Mid.name = Top.name
                Low.name = newHighName
                Top.name = Top.name
                Top.Score = scores[0]
                Mid.name = Mid.name
                Mid.Score = scores[1]
            
            players.sort(key=lambda record: record.score, reverse=True)

            #print(players)
            #print(scores)
            with open('data_01.dat','wb') as sav:
                pickle.dump(players,sav,pickle.HIGHEST_PROTOCOL)
                pickle.dump(scores,sav,pickle.HIGHEST_PROTOCOL)
                pickle.dump(Top,sav,pickle.HIGHEST_PROTOCOL)
                pickle.dump(Mid,sav,pickle.HIGHEST_PROTOCOL)
                pickle.dump(Low,sav,pickle.HIGHEST_PROTOCOL)
                pickle.dump(record,sav,pickle.HIGHEST_PROTOCOL)
    
        run = True
        while run:

            bgEndSurface = pygame.Surface((1024,768))
            bgEndSurface.fill((74,54,250))
            win.blit(bgEndSurface,(0,0))
            try:
                txtFont = pygame.font.Font('fonts/Fox Cavalier.otf', 60)
            except:
                txtFont = pygame.font.SysFont('Arial', 60)

            deadMsg = txtFont.render(str(deathMsg), True,(255,255,255))
            previousScore = txtFont.render('Your Score: ' + str(score), 1, (255,255,255))
            colour = (255,255,255)
            playAgain = classes.txtBtn(300,512,100,50,'play again','Fox Cavalier.otf')
            playAgain.draw(win)
            mainMenu = classes.txtBtn(700,512,100,50,'Main Menu','Fox Cavalier.otf')
            mainMenu.draw(win)
           # win.blit(playAgain, (512/2 - playAgain.get_width()/2, 500))

            win.blit(previousScore, (1024/2 - previousScore.get_width()/2,200))
            win.blit(deadMsg, (1024/2 - deadMsg.get_width()/2, 100))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    
                keys = pygame.key.get_pressed()

                if playAgain.hoverCheck() == True and event.type == MOUSEBUTTONDOWN or keys[K_SPACE]:
                    run = False
                    mainGame()

                if mainMenu.hoverCheck() == True and event.type == pygame.MOUSEBUTTONDOWN:

                    menuLoop()
        resetDodge()
                           
    def redrawWindow():
        win.blit(bg, (0,bgY))
        win.blit(bg2, (0,bgY2))
        for obj in objects:
            obj.draw(win)
        try:
            font = pygame.font.Font('fonts/Fox Cavalier.otf', 30)
        except:
            font = pygame.font.SysFont('Arial', 30)

        text = font.render('Score: ' + str(score), 1,(255,255,255))
        win.blit(text, (512-100,0))
        car.draw(win)
    #    khadda.draw(win) Test the hole (non-moving)
        pygame.display.flip()
        pygame.event.pump()

    calc_speed = 1.6
    # khadda = hole(300,220, 10,10) Test the hole object instance
    start_speed = 1.6
    multiplier = 1500 // start_speed #trying to find a number to to scale distance properly
    multiplier = int(multiplier)
    car = classes.player(450,490,5,5)
    pygame.time.set_timer(USEREVENT, multiplier)
    objects = []
    oneup = 1
    score = 0
    #450 by 590 is the starting pos for car (345,704) and surface (129,264); pygame uses topleft corner of image to blit it. 

    #-----DODGE GAME LOOP-----#
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    #pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

    lane_list = [437, 128, 700]
    maxSpeed = False

    run = True
    while run:

        if car.boost == False:
            score = score + 1

        elif car.boost == True:
            score = score + 0.5*calc_speed

        #print(score)
        score = int(round(score))
     #  3 score = int(score)3
        oneup += 1
        #calc_speed = 1.6
          
        for objj in objects:
            if objj.collide(car.hitbox):
                endScreen()

        #---MAXIMUM SPEED---#
        
        if calc_speed == 20:
            calc_speed = 20
        if calc_speed < 20:
            
            calc_speed =  1.4 + iterator


        #---GENERATES RANDOM BETWEEN m+600 and m+1500
        #   INTEGER CONSTANT FOR HOLE OBJECT SPEED---#
        multiplier = 1500 // calc_speed
        multiplier = int(multiplier)
        
        #pygame.time.set_timer(USEREVENT, multiplier)
        if calc_speed > 13:
            multiplier = random.randint(multiplier+700, multiplier+1500)
        elif calc_speed < 13:
            multiplier = random.randint(multiplier+800, multiplier+1600)
        #---DRAW THE OBSTACLE OBJECTS FROM THE LIST---#
        
        for obj in objects:
            obj.y += calc_speed
            #pygame.time.set_timer(USEREVENT, multiplier-350)
            if obj.y > 780:
                objects.pop(objects.index(obj))

        #---EVER INCREASING (UPTO 20) SPEED FOR BACKGROUND---#
        
        bgY += calc_speed
        bgY2 += calc_speed 
        if bgY > WIN_HEIGHT :
            bgY = bg.get_height()*-1
        if bgY2 > WIN_HEIGHT:
            bgY2 = bg.get_height() *-1
        iterator = iterator + 0.005
        
        #---DEBUGGING PURPOSES; CAN DELETE---#
        #print(calc_speed)
        
                    
        #if calc_speed == 20:
        #    calc_speed = 20            
        #if calc_speed < 20:
        #    calc_speed = 1.4 +iterator
        #else:
         #   calc_speed = calc_speed

        #print(calc_speed)

        #---EXIT CONDITION---#

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                
        #---ADD OBSTACLES TO THE OBJECTS LIST---#

        #---THREE DIFFERENT PATHS RANDOMLY CHOSEN SO THAT PLAYER CANNOT CHEAT AND STAY BETWEEN THE GAPS---#
        
            if event.type == USEREVENT:
                
                lane_picker = random.randint(0,2)
 
                if lane_picker == 0:

                    objectX = random.randrange(60, 750, 285)
                    objectY = random.randrange(150,680,250)
                    objectY = objectY*-1
                 
                    objects.append(obstacle(objectX,objectY,10,10))
                elif lane_picker == 1:

                    objectX = random.randrange(100, 750, 285)
                    objectY = random.randrange(160,680,250)
                    objectY = objectY*-1
              
                    objects.append(obstacle(objectX,objectY,10,10))

                elif lane_picker == 2:

                    objectX = random.randrange(205, 780, 285)
                    objectY = random.randrange(170,680,250)
                    objectY = objectY*-1
                    
                    objects.append(obstacle(objectX,objectY,10,10))

            #for timers in range(oneup):
                pygame.time.set_timer(USEREVENT, multiplier-150)
                    
           # print(objects)
        #---KEY PRESSES AND ACTIONS---#
        def pauseScreen():
            transparentSurface = pygame.Surface((1024,768))
            transparentSurface.set_alpha(128)
            transparentSurface.fill((255,255,255))
            pausedDisplay = txtFont.render("paused", True,(0,0,0))
            goToMenu = txtBtn(650 - pausedDisplay.get_width()/2,600-pausedDisplay.get_height()/2,100,50,'Go to menu','Fox Cavalier.otf')
            win.blit(transparentSurface,(0,0))
            win.blit(pausedDisplay, (512- pausedDisplay.get_width()/2,384-pausedDisplay.get_height()/2))
            while True:
                goToMenu.draw(win)

                clock.tick(60)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    if goToMenu.hoverCheck() == True and event.type == MOUSEBUTTONDOWN or keys[K_SPACE]:
                        run = False
                        menuLoop()
                            
                    if event.type == pygame.KEYDOWN:
                        pausedDisplay.set_alpha(0)
                        pygame.display.update()
                        height = 384-pausedDisplay.get_height()/2
                        for x in range(3,0,-1):
                            pausedDisplay = txtFont.render("%d"%(x), True,(0,0,0))
                            pausedDisplay.set_alpha(255)
                            height += 60
                            win.blit(pausedDisplay, (1024/2 - pausedDisplay.get_width()/2,height))
                            pygame.display.update()
                            time.sleep(1)

                        return
                        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            car.boost = True
            iterator = iterator + 0.05
          
        if keys[pygame.K_LEFT]or keys[pygame.K_a]:
            car.movingL = True


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            car.movingR = True

        if keys[pygame.K_j]:
            car.slow = True
        if keys[pygame.K_ESCAPE]:
            pauseScreen()


        redrawWindow()
        clock.tick(60)

run = True
def menuLoop():
    
    pygame.mixer.music.play()
    fadeIn()
    fadeToMain()
    while True:
        Update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

splashScreen()
#fadeIn()
#pygame.display.update()
#fadeToMain()
#fadeInBlack()
menuLoop()
