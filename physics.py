import pygame as pg
import math

run = True
newgame = True
pg.init()
pygame.display.set_caption('physics-toy')
programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

pg.font.init()
font = pg.font.SysFont('Calibri', 16)
info = font.render('Use "x" to launch the cube along the x axis', False, "white")
info2 = font.render('and "y" along the y axis.', False, "white")
screen = pg.display.set_mode((300, 300))

clock = pg.time.Clock()

bounces = 0.3
friction = 0.9
ballx = 130
bally = 0
xspeed = 20
yspeed = 1
gravity = 0.5
xdown = False
ydown = False

pathlines = []

while run:
    ball = pg.Rect(ballx, bally, 20, 20)
    bally += yspeed
    ballx += xspeed
    friction = xspeed * 1.4
        
    if bally >= 280:
       xspeed -= (friction/100)
    else:
       xspeed -= (friction/100)
        
    clock.tick(60)
    screen.fill("black")
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                if xspeed > 0:
                   xspeed += 20
                if xspeed < 0:
                   xspeed -= 20
            if event.key == pg.K_y and bally >= 275:
                yspeed -= 20
            
    if bally < 280:
       yspeed += gravity
    else:
        if yspeed > bounces:
            yspeed = yspeed * -1 * 0.5
        else:
            if abs(yspeed) <= bounces:
                yspeed = 0
    if bally < 0:
        yspeed *= -1

    if ballx < 0 or ballx > 280:
           xspeed *= -1
           
    if ballx < -1:
        ballx = 0
    if ballx > 281:
        ballx = 280

    if len(pathlines) > 20:
        pathlines.pop(0)
           
    pg.draw.rect(screen, "white", ball)
    for pathline in pathlines:
            pg.draw.rect(screen, "white", pathline)

    pathx = ballx 
    pathy = bally + 10
    ballpath = pg.Rect(pathx, pathy, 5, 5)
    pathlines.append(ballpath)
    screen.blit(info, (0, 0))
    screen.blit(info2, (0, 15))
    xspeedtext = font.render('Horizontal speed: ' + str(round(xspeed, 1)), False, "white")
    yspeedtext = font.render('Vertical speed: ' + str(round(yspeed, 1)), False, "white")
    screen.blit(xspeedtext, (0, 270))
    screen.blit(yspeedtext, (0, 285))
    pg.display.flip()
    
pg.quit()
