import pygame, sys, time
from pygame.locals import *
from math import cos, sin, pi 

pygame.init()

W, H = 800, 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# screen settings
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint")
buttons = pygame.Surface((100, 350))

# default settings
color = BLACK
tool = 'line'

font = pygame.font.SysFont('Verdana', 19)

# new dictionary
commands = {
    'right_triangle': [4, 4, 44, 44],
    'square': [52, 4, 44, 44],
    'equilateral_triangle': [4, 50, 44, 44],
    'rhombus': [52, 50, 44, 44],
    'rectangle': [4, 96, 44, 44],
    'circle': [52, 96, 44, 44],
    'line': [4, 142, 44, 44],
    'eraser' : [52, 142, 44, 44]
}


# function to draw interactive buttons
def draw_button():
    screen.fill(WHITE)
    buttons.fill(BLACK)
    pygame.draw.rect(buttons, BLACK, (2, 2, 96, 236), 1)

    for i in commands:
        pygame.draw.rect(buttons, WHITE, commands[i], 1)
    pygame.draw.polygon(buttons, WHITE, [(10, 40), (41, 40), (10, 10)], 2)
    pygame.draw.polygon(buttons, WHITE, [(25, 55), (42, 85), (10, 85)], 2)
    pygame.draw.rect(buttons, WHITE, (58, 10, 32, 32), 2)
    pygame.draw.polygon(buttons, WHITE, [(80, 60), (55, 60), (65, 85), (90, 85)], 2)
    pygame.draw.rect(buttons, WHITE, (7.5, 103, 38, 30), 2)
    pygame.draw.circle(buttons, WHITE, (74, 119), 17, 2)
    pygame.draw.line(buttons, WHITE, (9 ,180), (43, 147), 4)
    pygame.draw.rect(buttons, WHITE, (58, 148, 32, 32))
    
# function to calculate distance between 2 points   
def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

# function to draw a right triangle with account to mouse positions
def right_triangle(screen, current, end, width, color):
    x1, y1, x2, y2 = current[0], current[1], end[0], end[1]

    dy = abs(y1 - y2)
    if x1 <= x2:
        if y1 < y2:
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dy), (x2, y2)], width)
        else:
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dy), (x2, y2)], width)
    else:
        if y1 < y2:
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dy), (x2, y2)], width)
        else:
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dy), (x2, y2)], width)

# function to draw an equilateral triangle with account to mouse positions
def equilateral_triangle(screen, current, end, width, color):
    dis = distance(end, current)
    pygame.draw.polygon(screen, color, [end, current,((current[0] - end[0])*cos(pi/3) - (current[1] - end[1])*sin(pi/3) + end[0], (current[0] - end[0])*sin(pi/3) + (current[1] - end[1])*cos(pi/3) + end[1])], width)

# function to draw a square with account to mouse positions
def square(screen, current, end, width, color):
    x1, y1, x2, y2 = current[0], current[1], end[0], end[1]
    dx = abs(x1 - x2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x1, y1, dx, dx), width)
        else:
            pygame.draw.rect(screen, color, (x1, y2, dx, dx), width)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, dx, dx), width)
        else:
            pygame.draw.rect(screen, color, (x2, y2, dx, dx), width)

# function to draw a rhombus with account to mouse positions
def rhombus(screen, current, end, width, color):
    dis = distance(end, current)
    pygame.draw.polygon(screen, color, [end, (end[0] + dis, end[1]), (current[0] + dis, current[1]), current], width)

# function to draw a rectangle with account to mouse positions
def rectangle(screen, current, end, width, color):
    x1, y1, x2, y2 = current[0], current[1], end[0], end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x1, y1, dx, dy), width)
        else:
            pygame.draw.rect(screen, color, (x1, y2, dx, dy), width)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, dx, dy), width) 
        else:
            pygame.draw.rect(screen, color, (x2, y2, dx, dy), width)

# function to draw a circle with account to mouse positions
def circle(screen, current, end, width, color):
    x1, y1, x2, y2 = current[0], current[1], end[0], end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x1, y1, dx, dy), width)
        else:
            pygame.draw.ellipse(screen, color, (x1, y2, dx, dy), width)
    else:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x2, y1, dx, dy), width)

# function to draw a line
def line(screen, current, end, width, color):
    x1, y1, x2, y2 = current[0], current[1], end[0], end[1]

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
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

end_pos = (0, 0)
width = 2
drawing = False
erasing = False
erase_size = 50

tools = {
    'right_triangle' : False,
    'equilateral_triangle' : False,
    'square' : False,
    'rhombus' : False,
    'rectangle' : False,
    'circle' : False,
    'line' : True,
    'eraser' : False
}

# drawing our buttons
draw_button()

# main game loop
while True:
    current_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = 'red'
            if event.key == pygame.K_2:
                color = 'green'
            if event.key == pygame.K_3:
                color = 'blue'
            if event.key == pygame.K_4:
                color = 'black'
            if event.key == pygame.K_5:
                tools['eraser'] = True
                for k, v in tools.items():
                    if k!= 'eraser':
                        tools[k] = False

        # checks if mouse clicks within the hitbox of buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= current_pos[0] - 700 <= v[0] + v[2] and v[1] <= current_pos[1] <= v[1] + v[3]:
                    tools[k] = True
                    for i, j in tools.items():
                        if i != k:
                            tools[i] = False
                    break
        
        # implementation of drawing tools
        if tools['right_triangle'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                right_triangle(screen, end_pos, current_pos, width, color)
        elif tools['equilateral_triangle'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                equilateral_triangle(screen, end_pos, current_pos, width, color)
        elif tools['square'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                square(screen, end_pos, current_pos, width, color)
        elif tools['rhombus'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                rhombus(screen, end_pos, current_pos, width, color)
        elif tools['rectangle'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                rectangle(screen, end_pos, current_pos, width, color)
        elif tools['circle'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
            if event.type == pygame.MOUSEBUTTONUP:
                circle(screen, end_pos, current_pos, width, color)
        elif tools['line'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_pos = current_pos
                pygame.draw.circle(screen, color, current_pos, width)
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    line(screen, end_pos, current_pos, width, color)
                end_pos = current_pos
        elif tools['eraser'] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = current_pos
                pygame.draw.rect(screen, 'white', (x, y, erase_size, erase_size))
                erasing = True
            if event.type == pygame.MOUSEMOTION:
                if erasing:
                    pygame.draw.rect(screen, 'white', (current_pos[0], current_pos[1], erase_size, erase_size))
            if event.type == pygame.MOUSEBUTTONUP:
                erasing = False

    # outlines button red if selected
    for k, v in tools.items():
        if v == True:
            pygame.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pygame.draw.rect(buttons, 'white', commands[k], 1)

    
    screen.blit(buttons, (700, 0))
    screen.blit(screen, (0, 0))
    txt1 = font.render('Press:', 1, 'white')
    txt2 = font.render('1:Red', 0, 'white')
    txt3 = font.render('2:Green', 0, 'white')
    txt4 = font.render('3:Blue', 0, 'white')
    txt5 = font.render('4:Black', 0, 'white')
    txt6 = font.render('5:Eraser', 0, 'white')
    buttons.blit(txt1, (5, 200))
    buttons.blit(txt2, (5, 220))
    buttons.blit(txt3, (5, 240))
    buttons.blit(txt4, (5, 260))
    buttons.blit(txt5, (5, 280))
    buttons.blit(txt6, (5, 300))

    pygame.display.update()
    pygame.display.flip()
