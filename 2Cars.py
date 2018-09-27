import pygame, random, os, time,shelve
from pygame.locals import *
x=100
y=100
os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" %(x,y)


pygame.init()
WHITE = (255, 255, 255)
BLACK= (0,0,0)
blue = (0,0,255)
red = (255,0,0)
display_width=400
display_height=600

objSize=40
screen= pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('2Cars')
clock = pygame.time.Clock()

carImage1= pygame.image.load('twocars.png')
carImage1= pygame.transform.scale(carImage1,(40,70))

carImage2= pygame.image.load('twocars2.png')
carImage2= pygame.transform.scale(carImage2,(40,70))

circleBlue=pygame.image.load('circleBlue.png')
circleBlue= pygame.transform.scale(circleBlue,(objSize,objSize))

circleRed=pygame.image.load('circleRed.png')
circleRed= pygame.transform.scale(circleRed,(objSize,objSize))

squareBlue=pygame.image.load('squareBlue.png')
squareBlue= pygame.transform.scale(squareBlue,(objSize,objSize))

squareRed=pygame.image.load('squareRed.png')
squareRed= pygame.transform.scale(squareRed,(objSize,objSize))
def rand(m):
    if m==0:
        v=random.choice([30,130])
    else:
        v=random.choice([230,330])
    return v
def randShape(n):
    if n==0:
        u=random.choice([circleRed,squareRed])
    else:
        u=random.choice([circleBlue,squareBlue])
    return u
def unpause():
    #countdown()
    global pause
    pause=False
def carscore(count):
    font=pygame.font.SysFont(None,30)
    text=font.render('Score: '+ str(count), True, WHITE)
    screen.blit(text,(0,0))    
def paused():
    while pause:
        message_display('Paused',60,blue,(display_width/2),(display_height/2))
        message_display('press space for continue',60,blue,(display_width/2),(display_height/2+100))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    unpause()
def crashed(score):
    
    message_display('Game Over',60,blue,(display_width/2),(display_height/2))
    time.sleep(2)
    screen.fill(BLACK)
    message_display('Game Over',60,WHITE,(display_width/2),(display_height/2))
    message_display('Click Space for Restart',20,red,(display_width/2),(display_height/2+100))
    message_display('Click Esc for Quit',20,red,(display_width/2),(display_height/2+180))
    shelfFile=shelve.open('2cars')
    highScore=shelfFile['highscore']
    
    if score > highScore:
        shelfFile['highscore']=score
        shelfFile.close
        message_display(('Highscore :'+str(score)),25,WHITE,(display_width/2-100),(display_height/2+270))
        message_display(('Score :'+str(score)),30,WHITE,(display_width/2-100),(display_height/2+230))
    else:
        message_display(('Highscore :'+str(highScore)),25,WHITE,(display_width/2-100),(display_height/2+270))
    message_display(('Score :'+str(score)),30,WHITE,(display_width/2-100),(display_height/2+230))
    
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
                elif event.key ==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
def countdown():
    
    for i in range(3,0,-1):
        screen.fill(BLACK)
        message_display(str(i),60,WHITE,(display_width/2),(display_height/2))
        #screen.blit(wallImg,(0,0))
        #screen.blit(bgrImg,(20,20))
        time.sleep(1)
        pygame.display.update()
        clock.tick(5)
def intro():
    
    #pygame.mixer.music.play()
    intros=False
        
    xi1=100
    xi2=260
    moving=10
    yi1=600
    yi2=600
    curveX=5
    curveY=5
    while True:
        
        
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and intros==True:
                    gameloop()
        screen.fill(blue)
        
        pygame.draw.line(screen, WHITE,(display_width/2,20),
                             (display_width/2,580),3)
        pygame.draw.line(screen, WHITE,(display_width/4,20),
                             (display_width/4,580),1)
        pygame.draw.line(screen, WHITE,(display_width/2+100,20),
                             (display_width/2+100,580),1)
        
        if yi1<300:
            xi1+=curveX
            yi1-=curveY
            xi2-=curveX
            yi2-=curveY
            if yi1<190:
                curveX=0
                curveY=0
                intros=True
        else:
            yi1-= moving
            yi2-=moving
        if intros==True:
            message_display('2Cars',
                    50,red,(display_width/2),(display_height/2-210))
            message_display('Click Space to Begin',
                    30,BLACK,(display_width/2),(display_height/2+210))
        screen.blit(carImage1,(xi1,yi1))
        
        screen.blit(carImage2,(xi2,yi2))
        
             
        pygame.display.update()
        clock.tick(15)

def message_display(text,size,color,x,y):
    largeText=pygame.font.SysFont('comicsansms',size)
    textSurf=largeText.render(text,True,color)
    TextRect= textSurf.get_rect()
    TextRect.center= (x,y)
    screen.blit(textSurf,TextRect)
    pygame.display.update()

    
def gameloop():
    moveY=5
    x1=rand(0)
    x2=rand(1)
    ox0=rand(0)
    ox1=rand(1)
    ox2=rand(0)
    ox3=rand(1)
    a0=randShape(0)
    a1=randShape(0)
    b0=randShape(1)
    b1=randShape(1)
    diff=random.randrange(0,100,20)
    add=5
    y1=0
    y11=y1+diff
    y2=300
    y22=y2+diff
    b=randShape(1)
    countdown()
    score=0
    global pause
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if x1==30:
                        x1=130
                    else:
                        x1=30
                if event.key==pygame.K_RIGHT:
                    if x2==230:
                        x2=330
                    else:
                        x2=230
                if event.key==pygame.K_ESCAPE:
                    pause=True
                    paused()
        bottomDiff=random.randrange(500,700)
        
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE,(display_width/2,20),
                         (display_width/2,580),3)
        pygame.draw.line(screen, WHITE,(display_width/4,20),
                         (display_width/4,580),1)
        pygame.draw.line(screen, WHITE,(display_width/2+100,20),
                         (display_width/2+100,580),1)
        
        screen.blit(carImage1,(x1,530))
        
        screen.blit(carImage2,(x2,530))
        screen.blit(a0,(ox0,y1))
        screen.blit(a1,(ox2,y2))
        screen.blit(b0,(ox1,y11))
        screen.blit(b1,(ox3,y22))
        y1+=moveY
        y2+=moveY
        y11+=moveY
        y22+=moveY
        if 540<y11+objSize<590 and ox1==x2:
            
            if b0==circleBlue:
                score+=1
                
                y11=-100
                b0=randShape(1)
                ox1=rand(1)
                if score% add==0:
                    moveY+=1
            elif b0==squareBlue:
                crashed(score)
        elif 540<y22+objSize<590 and ox3==x2:
            
            if b1==circleBlue:
                score+=1
                
                y22=-100
                b1=randShape(1)
                ox3=rand(1)
                if score% add==0:
                    moveY+=1
            elif b1==squareBlue:
                crashed(score)
        elif 540<y1+objSize<590 and ox0==x1:
            
            if a0==circleRed:
                score+=1
                #print(score)
                y1=-100
                a0=randShape(0)
                ox0=rand(0)
                if score% add==0:
                    moveY+=1
            elif a0==squareRed:
                crashed(score)
        
        
        
        elif 540<y2+objSize<590 and ox2==x1:
            
            if a1==circleRed:
                score+=1
                
                y2=-100
                a1=randShape(0)
                ox2=rand(0)
                if score% add==0:
                    moveY+=1
            elif a1==squareRed:
                crashed(score)
    
        
        elif y1>display_height:
            if a0==circleRed:
                crashed(score)
            else:
                y1=0
                a0=randShape(0)
                ox0=rand(0)
        elif y2>display_height:
            if a1==circleRed:
                crashed(score)
            else:
                y2=0
                a1=randShape(0)
                ox2=rand(0)
        elif y11>display_height:
            if b0==circleBlue:
                crashed(score)
            else:
                
                y11=0
                b0=randShape(1)
                ox1=rand(1)
        elif y22>display_height:
            if b1==circleBlue:
                crashed(score)
            else:
                y22=0
                b1=randShape(1)
                ox3=rand(1)
                
        carscore(score)
        pygame.display.update()
        clock.tick(30)
#gameloop()
intro()
pygame.quit()
quit()
