import pygame
import datetime

back_color = (250,255,255)
window_size = [830, 780]

screen = pygame.display.set_mode(window_size)
main_clock = pygame.image.load(r"C:\Users\User\Desktop\PP2\lab 7\images\main-clock.png")
left_hand = pygame.image.load(r"C:\Users\User\Desktop\PP2\lab 7\images\left_hand.png")
right_hand = pygame.image.load(r"C:\Users\User\Desktop\PP2\lab 7\images\right_hand.png")
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

def blitRotateCenter(surface, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surface.blit(rotated_image, new_rect)

def seconds_angle(theta):
    result =((second % 60) / 60) * -(360)
    return result

def minute_angle(theta):
    result = ((minute % 60) / 60) * -(360-40)
    return result

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(back_color)
    screen.blit(main_clock, (0,0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second

    blitRotateCenter(screen, left_hand, (180, 320), seconds_angle(second))
    blitRotateCenter(screen, right_hand, (160, 300), minute_angle(minute))

    pygame.display.flip()
    clock.tick(60)
