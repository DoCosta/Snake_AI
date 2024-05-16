import random
import pygame, sys



# Game Settings
WIDTH = 1000
HEIGHT = 1000
FPS = 10
SPEED = 50
SIZE = 50
reward = 0 # Reward system for KI
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128,128,128)


# Vars
x_pos = 200
y_pos = 250
score = 0
isApple = False
direction = 3

# PyGame Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
surface = pygame.Surface((SIZE, SIZE))
surface.fill(color=GREY)
apple = pygame.Surface((SIZE, SIZE))
apple.fill(color=RED)

def drawGrid():
    blockSize = 50
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)


def isBorder():
    if (y_pos == (WIDTH)) or (y_pos == 0- 50):
        return True
    if (x_pos == (HEIGHT)) or (x_pos == 0-50):
        return True
    else:
        False


def Move(direction, x_pos, y_pos):

    if direction == 0:
        y_pos -= SPEED
    if direction == 1:
        y_pos += SPEED
    if direction == 2:
        x_pos -= SPEED
    if direction == 3:
        x_pos += SPEED

    return x_pos, y_pos

def Place_Food():
    fruit_position = [random.randrange(0, (HEIGHT - 50), 50),
                  random.randrange(0, (WIDTH - 50), 50)]
    return fruit_position

def Eat_Food(score, x, y):
    reward = +10
    body.append((x, y)) 
    return Place_Food(), reward


fruit_position = Place_Food()
        

body = [[x_pos, y_pos]]
while True:
    
    predirection = direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and predirection != 1:
                direction = 0
            if event.key == pygame.K_s and predirection != 0:
                direction = 1
            if event.key == pygame.K_a and predirection != 3:
                direction = 2
            if event.key == pygame.K_d and predirection != 2:
                direction = 3
    if isBorder():
        reward =-10
        pygame.quit()
        sys.exit()

    i = int(len(body)) -1
    while i >= 1:
        body[i] = body[i-1]
        
        i-=1
    body[0] = [x_pos, y_pos]

    f = int(len(body)) -1
    while f >= 0:
        if ((body[0] == body[f]) and (f != 0)):
            reward = -10
            pygame.quit()
            sys.exit()
        f-=1

    x_pos, y_pos = Move(direction, x_pos, y_pos)
    if fruit_position == [x_pos, y_pos]:
        fruit_position, reward = Eat_Food(score,x_pos, y_pos)

    screen.fill((175,215,70))   
    screen.blit(apple,fruit_position)
    drawGrid()
    for pos in body:
        screen.blit(surface,(pos))
    pygame.display.update()
    print(reward)
    clock.tick(FPS)
