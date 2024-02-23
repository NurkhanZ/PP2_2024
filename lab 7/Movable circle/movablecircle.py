import pygame

pygame.init()


SIZE = WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
RADIUS = 25
speed = 5
x = WIDTH / 2
y = HEIGHT / 2

clock = pygame.time.Clock()
pygame.display.set_caption("Circle")
screen = pygame.display.set_mode(SIZE)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - RADIUS - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + RADIUS + speed <= WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - RADIUS - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + RADIUS + speed <= HEIGHT:
        y += speed

    screen.fill(WHITE)
    circle = pygame.draw.circle(screen, RED, (x,y), RADIUS)
    
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()
    

