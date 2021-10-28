import pygame
from pygame.draw import *
from random import randint
from random import random
import json
pygame.init()

#set parametres
FPS = 20
t = 1
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
scores = 0
delta = '0'

#color definition
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#defining class ball
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
def draw(sth, x, y):
    global WHITE
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(str(sth), 1, WHITE)
    surf.blit(text1, (x, y))
    pygame.display.update()  
def hit(ball1, ball2):
    distsq = (ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2
    if distsq < ball1.r ** 2+ ball2.r ** 2:
        ball1.vx *= -1
        ball1.vy *= -1
        ball2.vx *= -1
        ball2.vy *= -1
def score():
    global scores
    counter = 0
    for tup in targets:
        if tup.x - tup.r <= event.pos[0]:
            if tup.x + tup.r >= event.pos[0]:
                if tup.y - tup.r <= event.pos[1]:
                    if tup.y + tup.r >= event.pos[1]:
                        counter += 1
                        scores += 100
                        targets.remove(tup)
                        return '100'
    for ball in pool:
        if ball.x - ball.r <= event.pos[0]:
            if ball.x + ball.r >= event.pos[0]:
                if ball.y - ball.r <= event.pos[1]:
                    if ball.y + ball.r >= event.pos[1]:
                        scores += 50 - ball.r
                        counter += 1
                        pool.remove(ball)
                        return str(50 - ball.r)
    #if counter == 0:
        #print('Click!')
            


def renew(list, number):
    if len(list) < number:
        for i in range(number - len(list)):
            list.append(Ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False
font = pygame.font.SysFont(None, 100)
text = ""
input_active = True

while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
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
    draw(scores, 100, 50)
    if delta is not None:
        draw('+' + delta, 100, 100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or\
               event.type == pygame.KEYDOWN:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            delta = score()
            

pygame.display.update()
screen.fill(BLACK)
draw(scores, 100, 50)

with open("records.json", 'r') as f:
    loaded = json.load(f) 
loaded['results'] = sorted(loaded['results'], 
                            key=lambda x: x['points'], reverse=True)

x = 150
y = 150
screen.fill(BLACK)
for i, el in enumerate(loaded['results']):
    if i > 9:
        break
    y += 50
    draw(el['name']+'    '  +str(el['points']), x, y)
draw('put your nickname', 150, 100)
if event.type == pygame.MOUSEBUTTONDOWN:
    input_active = True
    text = ""
elif event.type == pygame.KEYDOWN and input_active:
    if event.key == pygame.K_RETURN:
        input_active = False
elif event.key == pygame.K_BACKSPACE:
    text =  text[:-1]
else:
    text += event.unicode
screen.fill(0)
text_surf = font.render(text, True, (255, 0, 0))
screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
pygame.display.flip()
    
with open("records.json", 'w') as f:
    json.dump(loaded, f)
x = 150
y = 150
screen.fill(BLACK)
for i, el in enumerate(loaded['results']):
    if i > 9:
        break
    y += 50
    draw(el['name'] + '    '  +str(el['points']), x, y)
nickname = text
loaded['results'].append({'name': nickname, 'points': scores})
screen.fill(BLACK)
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
