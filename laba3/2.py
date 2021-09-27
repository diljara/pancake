import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 450))
line(screen, (254, 213, 148), (0, 50), (800, 50), 100)
line(screen, (254, 213, 196), (0, 150), (800, 150), 100)
line(screen, (254, 213, 148), (0, 250), (800, 250), 100)


dx = [50, 25, 40, 45, 33, 49, 56]
dy = [12, -25, 17, -20, 10, -16, 8]
x = [(0, 250)]
i = 0
while x[i][0] <= 740:
    x.append((x[i][0] + dx[i%7], x[i][1] + dy[i%7]))
    i += 1
x.append((800, 200))
x.append((800, 450))
x.append((0, 450))
da = [30, 80, 100, 65]
a = [(0, 180)]
i = 0
while a[i][0] <= 700:
    a.append((a[i][0] + da[i%4], a[i][1] + dy[i%7]))
    i += 1
a.append((800, 150))
a.append((0, 180))
#sky (254, 213, 162)
#sandd(254, 213, 148)


polygon(screen, (255, 178, 66), a)
polygon(screen, (172, 67, 52), x)
polygon(screen, (179, 134, 148), [(0, 300), (800, 250), (800, 450), (0, 450)])
circle(screen, (252, 238, 33), (400, 100), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
