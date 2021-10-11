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
        self.x = randint(0, SCREEN_WIDTH - 50)
        self.y = randint(0, SCREEN_HEIGHT - 50)
        self.vx = random()*randint(-5, 5)
        self.vy = randint(-5, 5)*random()
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
pool = []
for i in range(10):
    pool.append(Ball())   
    
def score():
    global scores
    counter = 0
    if tup.x - tup.r <= event.pos[0] <= tup.x + tup.r:
        if tup.y - tup.r <= event.pos[1] <= tup.y + tup.r:
            print('+', 100)
            counter += 1
            pool.remove(tup)
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
def renew(list):
    if len(list) < 10:
        for i in range(10 - len(list)):
            list.append(Ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    Ball.target(tup)
    renew(targets)
    for ball in pool:
        Ball.move(ball)
        pygame.display.update()
        Ball.collision(ball)
        renew(pool)
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
