import pygame, sys
from pygame.locals import *

pygame.init()

W, H = 1200, 700

fps = 60
clock = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STARTCOLOR = (200, 200, 255)
YELLOW = (255, 255, 0)
SKY = (0, 255, 255)
PURPLE = (255, 0, 255)
hsl = (170, 255, 255)
color = BLACK
colorname = 'Black'

screen = pygame.display.set_mode((W, H))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

forbutton = pygame.Surface((300, 70))

startPos = (0, 0)
welcomeFont = pygame.font.SysFont('Begetter Regular', 50)
welcomeFont2 = pygame.font.SysFont('ChunkFive', 42)
surffont = pygame.font.SysFont('arial', 15)
surffont2 = pygame.font.SysFont('Verdana', 23)

living = True
welcomepage = True
commands = {
    'rect' : [3, 23, 38, 38],
    'circle' : [60, 23, 38, 38], 
    'line' : [120, 23, 38, 38],
    'eraser' : [180, 23, 38, 38]
}

def setsurf():
    forbutton.fill(hsl)
    pygame.draw.rect(forbutton, BLACK, [0, 0, 299, 69], 1)
    forbutton.blit(surffont.render('equipments:', True, (0, 0, 0)), (5, 3))
    for i in commands:
        pygame.draw.rect(forbutton, BLACK, commands[i], 1)
    pygame.draw.rect(forbutton, RED, (7, 27.5, 30, 30), 1)
    pygame.draw.circle(forbutton, RED, (79, 42), 15, 1)
    pygame.draw.aaline(forbutton, RED, (120 ,25.5), (155, 60), 1)
    pygame.draw.rect(forbutton, WHITE, (184.8, 27.5, 30, 30))
    screen.blit(background, (0, 0))
    screen.blit(forbutton, (1, 1))

def rectangle(screen, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x1, y1, width, height), size)
        else:
            pygame.draw.rect(screen, color, (x1, y2, width, height), size)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, width, height), size) 
        else:
            pygame.draw.rect(screen, color, (x2, y2, width, height), size) 

def circle(screen, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x1, y1, width, height), size)
        else:
            pygame.draw.ellipse(screen, color, (x1, y2, width, height), size)
    else:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x2, y1, width, height), size) 
        else:
            pygame.draw.ellipse(screen, color, (x2, y2, width, height), size)
    
def line(screen, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), size)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), size)
    
last_pos = (0, 0)
w = 3
draw_line = False
erase = False
ed = 50
d = {
    'line' : True,
    'rect': False,
    'circle': False,
    'eraser': False
}

while living:
    while welcomepage:
        screen.fill(STARTCOLOR)
        for event in pygame.event.get():
            pressedkey = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(welcomeFont.render("Welcome", True, BLACK), (290, 10))
            screen.blit(welcomeFont2.render("Painting options:", True, RED), (10, 50))
            screen.blit(welcomeFont2.render("D: Black(Default color)", True, BLACK), (10, 100))
            screen.blit(welcomeFont2.render("R: Red", True, BLACK), (10, 150))
            screen.blit(welcomeFont2.render("B: Blue", True, BLACK), (10, 200))
            screen.blit(welcomeFont2.render("Y: Yellow", True, BLACK), (10, 250))
            screen.blit(welcomeFont2.render("G: Green", True, BLACK), (10, 300))
            screen.blit(welcomeFont2.render("S: Sky", True, BLACK), (10, 350))
            screen.blit(welcomeFont2.render("P: Purple", True, BLACK), (10, 400))
            screen.blit(welcomeFont2.render("Equipments", True, RED), (10, 450))
            screen.blit(welcomeFont2.render("E: Eraser", True, BLACK), (10, 500))
            screen.blit(welcomeFont2.render("L: Save image", True, BLACK), (10, 550))
            screen.blit(welcomeFont2.render("Press W to stpeart", True, BLUE), (240, 600))
            pygame.display.flip()
            if pressedkey[K_w]:
                welcomepage = False
    pressedkey = pygame.key.get_pressed()
    setsurf()

    if pressedkey[K_d]:
        color = BLACK
        colorname = 'Black'
    elif pressedkey[K_r]:
        color = RED
        colorname = 'Red'
    elif pressedkey[K_b]:
        color = BLUE
        colorname = 'Blue'
    elif pressedkey[K_y]:
        color = YELLOW
        colorname = 'Yellow'
    elif pressedkey[K_g]:
        color = GREEN
        colorname = 'Green'
    elif pressedkey[K_s]:
        color = SKY
        colorname = 'Sky'
    elif pressedkey[K_p]:
        color = PURPLE
        colorname = 'Purple'
    elif pressedkey[K_e]:
        color = WHITE
        colorname = 'Eraser'
    elif pressedkey[K_t]:
        welcomepage = True
    elif pressedkey[K_l]:
        pygame.image.save(background, 'image.png')

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            living = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0] - 10 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break
        if d['line'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
                pygame.draw.circle(background, color, pos, w)
                draw_line = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_line = False
            if event.type == pygame.MOUSEMOTION:
                if draw_line:
                    line(background, last_pos, pos, w, color)
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                rectangle(background, last_pos, pos, w, color)
        elif d['circle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                circle(background, last_pos, pos, w, color)
        elif d['eraser'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x ,y) = pos
                pygame.draw.rect(background, WHITE, (x, y ,ed, ed))
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(background, WHITE, (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False
    for k, v in d.items():
        if v == True:
            pygame.draw.rect(forbutton, RED, commands[k], 1)
        else:
            pygame.draw.rect(forbutton, BLACK, commands[k], 1)

    background.blit(surffont2.render("Press 'T' to show painting options!",True,(0,0,0)),(30, 550))
    screen.blit(forbutton, (1, 1))
    background.blit(forbutton, (1, 1))
    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(fps)
    pygame.display.flip()