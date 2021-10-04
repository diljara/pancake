import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 450))
#colordefinition
birds = (66, 33, 11)
sky = (254, 213, 162)
sand = (254, 213, 148)
front = (48, 16, 38)
midhills = (172, 67, 52)
backhills = (252, 152, 49)
sun = (252, 238, 33)
line3 = (254, 213, 196)
purple = (179, 134, 148)
#skylines
line(screen, sky, (0, 50), (800, 50), 100)
line(screen, line3, (0, 150), (800, 150), 100)
line(screen, sand, (0, 250), (800, 250), 100)
#listsformountains
dx = [50, 25, 40, 45, 33, 49, 56]
dy = [28, -45, 27, -40, 30, -42, 10]
x = [(0, 250)]
i = 0
while x[i][0] <= 740:
    x.append((x[i][0] + dx[i % 7], x[i][1] + dy[i % 7]))
    i += 1
x.append((800, 200))
x.append((800, 450))
x.append((0, 450))
da = [30, 80, 100, 65]
a = [(0, 180)]
i = 0
while a[i][0] <= 700:
    a.append((a[i][0] + da[i % 4], a[i][1] + dy[i % 7]))
    i += 1
a.append((800, 160))
a.append((0, 220))
a.append(a[0])
#птыц

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def draw_arc_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.arc(shape_surf, color, (0, 0, *target_rect.size), 0, 3.14, width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def BIRDS(x, y, alpha=1): #alpha defines the size of the bird
    draw_ellipse_angle(screen, birds, [x - 12.5*alpha, y, 40*alpha, 10*alpha], -45)
    draw_ellipse_angle(screen, birds, [x + 12.5*alpha, y - 2*alpha, 43*alpha, 10*alpha], 50)

listforfronthills=[(0, 200), (100, 230), (250, 370), (300, 420), (500, 440), (550, 380), (600, 400), (650, 300), (800, 248),  (800, 450), (0, 450), (0, 200)]

polygon(screen, backhills, a)
polygon(screen, midhills, x)
polygon(screen, purple, [(0, 300), (800, 250), (800, 450), (0, 450)])
circle(screen, sun, (400, 100), 40)
polygon(screen, front, listforfronthills)

BIRDS(100, 100)
BIRDS(400, 300)
BIRDS(150, 150)
BIRDS(600, 200)
BIRDS(650, 230)
BIRDS(500, 260, 0.75)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
