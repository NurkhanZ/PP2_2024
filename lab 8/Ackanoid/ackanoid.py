import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fps = 60
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BACKGROUND = (0, 0, 0)

W = 1200
H = 750
game_score = 0

font = pygame.font.SysFont('comicsansms', 40)

# game over text
game_over = font.render('Game Over', True, WHITE)
game_overRect = game_over.get_rect()
game_overRect.center = (W // 2, H // 2)

# win text
win_text = font.render('You win', True, BLACK)
win_textRect = win_text.get_rect()
win_textRect.center = (W // 2, H // 2)

# game score text
game_score_text = font.render(f'Your game score is: {game_score}', True, WHITE)
game_scoreRect = game_score_text.get_rect()
game_overRect.center = (210, 20)

collision_sound = pygame.mixer.Sound(r'lab 8/Ackanoid/assets/catch.mp3')

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def exit_game():
    global done
    pygame.display.update()
    time.sleep(1.5)
    done = True

class Block:
    def __init__(self, block_rect, color_list, unbreakable = False, bonus = False):
        self.rect = block_rect
        self.color = color_list
        self.unbreakable = unbreakable
        self.bonus = bonus
        self.num_hits = 3 if bonus else 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color[0], self.rect)
    
    def hit(self):
        if not self.unbreakable:
            self.num_hits -=1
            if self.num_hits == 0:
                if self.bonus:
                    return self.handle_bonus()
                else:
                    return True
        return False

    def handle_bonus(self):
        global ball_radius
        ball_radius += 5
        return True

# blocks
block_list = []

for i in range(10):
    for j in range(4):
        block_rect = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        unbreakable = (i % 3 == 0)
        bonus = (i % 6 == 0 and j % 2 == 0)
        if unbreakable:
            color_list = (230, 230, 250)
        elif bonus:
            color_list = (220, 20, 60)
        else:
            color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))]
        block_list.append(Block(block_rect, color_list, unbreakable, bonus))


# paddle
paddle_width = 150
paddle_height = 25
paddle_speed = 20
paddle = pygame.Rect(W // 2 - paddle_width, H - paddle_height - 30, paddle_width, paddle_height)

# ball
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

done = False

INC_SPEED = pygame.USEREVENT + 1
DEC_PADDLE = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 2000)
pygame.time.set_timer(DEC_PADDLE, 2000)

while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ball_speed += 0.1
        if event.type == DEC_PADDLE:
            paddle_width -= 2.5
            paddle.width = paddle_width
        if event.type == pygame.QUIT:
            exit_game()

    screen.fill(BACKGROUND)
    
    W = pygame.display.get_window_size()[0]
    H = pygame.display.get_window_size()[1]

    for block in block_list:
        block.draw(screen)

    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, RED, ball.center, ball_radius)

    # paddle control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddle_speed

    # ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # collision left
    if ball.centerx < ball_radius or ball.centerx > W - ball_radius:
        dx = -dx
    
    # collision right
    if ball.centery < ball_radius + 50:
        dy = -dy
    
    # collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    
    # collision blocks
    hit_index = ball.collidelist([block.rect for block in block_list])

    if hit_index != -1:
        block = block_list[hit_index]
        if block.unbreakable:
            dx, dy = detect_collision(dx, dy, ball, block.rect)
        else:
            dx, dy = detect_collision(dx, dy, ball, block_rect)
            if block.hit():
                block_list.pop(hit_index)
                game_score += 1
                collision_sound.play()
    
    game_score_text = font.render(f'Your game score is: {game_score}', True, WHITE)
    screen.blit(game_score_text, game_scoreRect)

    # win/lose conditions
    if ball.bottom > H:
        screen.fill(BLACK)
        screen.blit(game_over, win_textRect)
        exit_game()
    elif len(block_list) == 16:
        screen.fill(WHITE)
        screen.blit(win_text, win_textRect)
        exit_game()
    
    pygame.display.update()
    clock.tick(fps)
    pygame.display.flip()