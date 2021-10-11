import pygame
from pygame.draw import *
from random import randint
from random import random
pygame.init()

FPS = 15
t = 1
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
scores = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    def __init__(self):
        self.x = randint(50, SCREEN_WIDTH - 50)
        self.y = randint(50, SCREEN_HEIGHT - 50)
        self.vx = random()*randint(-15, 15)
        self.vy = randint(-15, 15)*random()
        self.r = randint(10, 50)
        self.color = COLORS[randint(0, 5)]
        
    def move(self, surface=screen):
        circle(surface, self.color, (self.x, self.y), self.r)
        self.x += self.vx * t
        self.y += self.vy * t
    
    def target(self, surface = screen):
        circle(surface, RED, (self.x, self.y), self.r, self.r//2)
        circle(surface, WHITE, (self.x, self.y), self.r - self.r//2)
        self.x += self.vx * t
        self.y += self.vy * t
            
    def collision(self):
        if self.x < self.r or self.x + self.r > SCREEN_WIDTH:
            self.vx = -self.vx
        if self.y < self.r or self.y + self.r > SCREEN_HEIGHT:
            self.vy = -self.vy
                

tup = Ball()
targets = [tup]
targets.append(Ball())
pool = []
for i in range(10):
    pool.append(Ball())   
def hit(ball1, ball2):
    if pow((ball1.x - ball2.x), 2) + pow((ball1.y - ball2.y), 2) < ball1.r * ball1.r + ball2.r * ball2.r:
        ball1.vx *= -1
        ball1.vy *= -1
        ball2.vx *= -1
        ball2.vy *= -1
def score():
    global scores
    counter = 0
    for tup in targets:
        if tup.x - tup.r <= event.pos[0] <= tup.x + tup.r:
            if tup.y - tup.r <= event.pos[1] <= tup.y + tup.r:
                print('+', 100)
                counter += 1
                scores += 100
                targets.remove(tup)
    for ball in pool:
        if ball.x - ball.r <= event.pos[0] <= ball.x + ball.r:
            if ball.y - ball.r <= event.pos[1] <= ball.y + ball.r:            
                scores += 50 - ball.r
                print('+', 50 - ball.r)
                counter += 1
                pool.remove(ball)
    if counter == 0:
        print('Click!')
            
def draw_scores():
    pass
def renew(list, number):
    if len(list) < number:
        for i in range(number - len(list)):
            list.append(Ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for ball in targets:
        Ball.target(ball)
        pygame.display.update()
        Ball.collision(ball)
        renew(targets, 2)
        hit(targets[0], targets[1])
    for ball in pool:
        Ball.move(ball)
        pygame.display.update()
        Ball.collision(ball)
        renew(pool, 10)
    for i in range (len(pool)):
        for j in range (i, len(pool)):
            hit(pool[i], pool[j])
            hit(pool[i], targets[0])
            hit(pool[i], targets[1])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score()

    pygame.display.update()
    screen.fill(BLACK)
draw_scores()
pygame.quit()
print(scores)
