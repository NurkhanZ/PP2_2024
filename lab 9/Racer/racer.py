import pygame, sys, random, time
from pygame.locals import *

pygame.init()

W, H = 400, 600

fps = 60
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_speed = 5
speed = 7
score = 0
coins = 0
bonus = False
speeding = False

font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, WHITE)
game_over_rect = game_over.get_rect()
game_over_rect.center = (W // 2, H // 2)

speeding_text = font_small.render('+10 km/h', True, RED)
speeding_text_rect = speeding_text.get_rect()
speeding_text_rect.center = (W // 2, H // 2)

bonus_text = font_small.render('Better steering!', True, BLACK)
bonus_text_rect = bonus_text.get_rect()
bonus_text_rect.center = (W // 2, H // 2)

background = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\road.png')
bonus_image = pygame.image.load(r"C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Coin\maintenance.png")
vehicle_image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\vehicle.png')
bonus_image_rect = bonus_image.get_rect()
bonus_image_rect.center = (W // 2 - 100, H // 2)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Racer')
pygame.display.set_icon(vehicle_image)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rand = random.randint(1, 6)
        self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Enemy' + f'/{self.rand}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        self.rand = random.randint(1, 6)
        if self.rect.top > H:
            score += 1
            self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Enemy' + f'/{self.rand}.png')
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 5:
            self.rect.move_ip(-player_speed, 0)
        elif pressed_keys[K_RIGHT] and self.rect.right < W - 5:
            self.rect.move_ip(player_speed, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Coin\1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, W - 10), 30)
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class CoinBig(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Coin\2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, W - 25), 15)
        self.spawn = 0
    def move(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
            self.spawn = 0

class CoinBonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\Coin\maintenance.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(5, W - 5), 35)
        self.spawn = 0
    def move(self):
        self.rect.move_ip(0, 6)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
            self.spawn = 0

P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = CoinBig()
C3 = CoinBonus()

enemies = pygame.sprite.Group()
enemies.add(E1)

players = pygame.sprite.Group()
players.add(P1)

big_coins = pygame.sprite.Group()
big_coins.add(C2)

bonus_coins = pygame.sprite.Group()
bonus_coins.add(C3)

active_sprites = pygame.sprite.Group()
active_sprites.add(P1)
active_sprites.add(E1)
active_sprites.add(C1)

coin_sprites = pygame.sprite.Group()
coin_sprites.add(C1)
coin_sprites.add(C2)
coin_sprites.add(C3)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

crash_sound = pygame.mixer.Sound(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\crash.mp3')
cash_sound = pygame.mixer.Sound(r'C:\Users\User\Desktop\PP2\lab 9\Racer\assets\coin.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            speed += 0.055
    
    game_score = font_small.render(f'Close calls: {score}', True, BLACK)
    game_score_rect = game_score.get_rect()
    game_score_rect.center = (75, 20)

    coin_score = font_small.render(f'{coins}$', True, BLUE)
    coin_score_rect = coin_score.get_rect()
    coin_score_rect.center = (380, 20)

    screen.blit(background, (0, 0))
    screen.blit(game_score, game_score_rect)
    screen.blit(coin_score, coin_score_rect)


    for entity in active_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if C2.spawn >= 10:
        speed += 0.01
        speeding = True
        speeding_timer = pygame.time.get_ticks()
        for entity in big_coins:
            screen.blit(entity.image, entity.rect)
            entity.move()

    if speeding:
        screen.blit(speeding_text, speeding_text_rect)
        if pygame.time.get_ticks() - speeding_timer >= 1000:
            speeding = False
            
        
    if C3.spawn >= 15:
        for entity in bonus_coins:
            screen.blit(entity.image, entity.rect)
            entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        screen.fill(BLACK)
        screen.blit(game_over, game_over_rect)
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(C1, players):
        cash_sound.play()
        coins += 1
        C2.spawn += 1
        C3.spawn += 1
        C1.rect.center = (random.randint(40, W - 40), 0)

    if pygame.sprite.spritecollideany(C2, players):
        cash_sound.play()
        coins += 3
        C2.spawn = 0
        C3.spawn += 1
        C2.rect.center = (random.randint(40, W - 40), 0)

    if pygame.sprite.spritecollideany(C3, players):
        cash_sound.play()
        coins += 2
        C3.spawn = 0
        C2.spawn += 1
        C3.rect.center = (random.randint(40, W - 40), 0)
        bonus_timer = pygame.time.get_ticks()
        bonus = True
    if bonus:
        player_speed = 8
        screen.blit(bonus_text, bonus_text_rect)
        screen.blit(bonus_image, bonus_image_rect)
        if pygame.time.get_ticks() - bonus_timer >= 5000:
            bonus = False
            player_speed = 5

    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)
