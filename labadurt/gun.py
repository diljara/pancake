import math
from random import choice, randint

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
BLACK = 0x000000
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 10

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx 
        self.y -= self.vy
        self.vy -= 1.0
        if abs(self.x - 400 - self.r) >= 400:
            self.vx *= -1
            self.live -= 1
        if abs(self.y - 300 - self.r) >= 300:
            self.vy *= -0.75
            self.live -= 1

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный объект с целью(объект obj).

        Args:
            obj: Объ ект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        distsq = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2
        if distsq <= self.r ** 2 + obj.r ** 2 + 2:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return(new_ball)

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0]-20) == 0:
                self.an = 1.57
            else:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        deltax, deltay = self.f2_power * (x - 20) // 150, self.f2_power * (y - 450) // 150    
        pygame.draw.line(screen, self.color, (20, 450), (20 + deltax, 450 + deltay), width=10)
         

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.draw()
                
            self.color = RED
        else:
            self.color = GREY


class Target(Ball):
    def __init__(self, x=randint(600, 780), y=randint(300, 550), 
                      r=randint(10,25), vx=randint(10,25), vy=randint(10,25)):
        """ Инициализация цели
        Args:
        x - начальное положение target'а по горизонтали
        y - начальное положение target'а по вертикали
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = RED
        
    def move(self):
        """Переместить target по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx 
        self.y -= self.vy
        if abs(self.x - 400 - self.r) >= 400:
            self.vx *= -1
        if abs(self.y - 300 - self.r) >= 300:
            self.vy *= -1

def draw(sth, x=50, y=50):
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(str(sth), 1, BLACK)
    screen.blit(text1, (x, y))
    pygame.display.update() 

pygame.init()

clock = pygame.time.Clock()
gun = Gun()
target1 = Target()
target2 = Target()
points = 0
bulletcounter = 0
balls = [target1, target2]
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in balls[0:2]:
        target.draw()
    draw('points : ' + str(points))
    draw('shots : ' + str(bulletcounter), 50, 100)
    draw('emo kid is watching you: ///_^', 200, 100)
    for i, b in enumerate(balls):
        b.draw()
        b.move()
        if i > 1:
            for target in balls[0:2]:
                if b.hittest(target):
                    points += 1
                    bulletcounter = 0
                    del balls[2:]
                    target = Target(randint(600, 780), randint(300, 550), randint(10,25), randint(10,25), randint(10,25))
            if b.live == 0:
                bulletcounter += 1
                balls.remove(b)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            bullet = gun.fire2_end(event)
            balls.append(bullet)
            bulletcounter += 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    gun.power_up()

pygame.quit()
