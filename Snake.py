import random
import pygame, sys



# Game Settings
is_running = True
WIDTH = 600   # WIDHT / HEIGHT should be proportional to SIZE
HEIGHT = 600
FPS = 10
SIZE = 30
SPEED = SIZE
reward = 0 # Reward system for KI
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128,128,128)


# Vars
x_pos = 0
y_pos = 0
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
    blockSize = SIZE
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)


def isBorder(x_pos, y_pos):
    if (y_pos >= (HEIGHT)) or (y_pos <= 0 - SIZE):
        return True
    if (x_pos >= (WIDTH)) or (x_pos <= 0 - SIZE):
        return True
    else:
        return False


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

def Place_Food(body):
        fruit_position = [random.randrange(0, (WIDTH - SIZE), SIZE),
                    random.randrange(0, (HEIGHT - SIZE), SIZE)]
        if fruit_position in body:
            Place_Food(body)
        else:
            return fruit_position

def Eat_Food(body, x, y):
    reward = +10
    body.append((x, y)) 
    return Place_Food(body), reward

def QuitGame():
    pygame.quit()
    sys.exit()

def GameOver():
    is_Screen = True
    font = pygame.font.SysFont('arial', 30)
    text = font.render('Game Over', True, BLACK)
    screen.fill(GREY)
    screen.blit(text, [WIDTH / 2 - 80, HEIGHT / 2 - 60])
    text2 = font.render('X for Exit | R for Restart', True, BLACK)
    screen.blit(text2, [WIDTH / 2 - 150, HEIGHT / 2 + 20])
    pygame.display.update()
    while is_Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    is_Screen = False
                    return True
                
                if event.key == pygame.K_x:
                    QuitGame()
                    

body = [[x_pos, y_pos]]
fruit_position = Place_Food(body)
while is_running:
    
    predirection = direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QuitGame()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and predirection != 1:
                direction = 0
            if event.key == pygame.K_s and predirection != 0:
                direction = 1
            if event.key == pygame.K_a and predirection != 3:
                direction = 2
            if event.key == pygame.K_d and predirection != 2:
                direction = 3

    if isBorder(x_pos,y_pos):
        reward =-10
        is_running = False
        body.clear()
        body.append([0, 0])
        x_pos, y_pos = 0, 0
        reward = 0
        direction = 3
        is_running = GameOver()
        

    i = int(len(body)) -1
    while i >= 1:
        body[i] = body[i-1]
        
        i-=1
    body[0] = [x_pos, y_pos]

    f = int(len(body)) -1
    while f >= 0:
        if ((body[0] == body[f]) and (f != 0)):
            reward = -10
            QuitGame()
        f-=1

    x_pos, y_pos = Move(direction, x_pos, y_pos)
    if fruit_position == [x_pos, y_pos]:
        fruit_position, reward = Eat_Food(body,x_pos, y_pos)

    screen.fill((175,215,70))   
    screen.blit(apple,fruit_position)
    drawGrid()
    for pos in body:
        screen.blit(surface,(pos))
    pygame.display.update()
    clock.tick(FPS)
