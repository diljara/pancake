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
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    def __init__(self, x=40, y=450, r=10, vx=0, vy=0, color=choice(GAME_COLORS)):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = color
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
        if abs(self.x - 400 - self.r) >= 370:
            self.vx *= -1
            self.live -= 1
        if abs(self.y - 300 - self.r) >= 270:
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
            obj: Объект, с которым проверяется столкновение.
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
        new_ball.vx = self.f2_power * math.cos(self.an) * 0.8
        new_ball.vy = - self.f2_power * math.sin(self.an) * 0.8
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
                      r=randint(10,25), vx=randint(0, 10), vy=randint(0, 10), color=RED):
        """ Инициализация цели
        Args:
        x - начальное положение target'а по горизонтали
        y - начальное положение target'а по вертикали
        """
        super().__init__(x, y, r, vx, vy, color)
        
    def move(self):
        """Переместить target по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx 
        self.y -= self.vy
        if abs(self.x - 400 - self.r) >= 370:
            self.vx *= -1
        if abs(self.y - 300 - self.r) >= 270:
            self.vy *= -1

def draw(sth:str, x=50, y=50):
    '''
    the function draws sth
    x, y define the position of text in the screen
    default x, y = 50, 50
    '''
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(str(sth), 1, BLACK)
    screen.blit(text1, (x, y))
    pygame.display.update() 

pygame.init()

clock = pygame.time.Clock()
gun = Gun()
balls = []
for i in range(2):
    balls.append(Target())
points = 0
bulletcounter = 0
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
            for j, target in enumerate(balls[:2]):
                if b.hittest(target):
                    points += 1
                    bulletcounter = 0
                    del balls[2:]
                    balls[j] = Target()
        if b.live == 0:
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
        elif pygame.key.get_pressed()[pygame.K_RETURN] :
            screen.fill(WHITE)
            
    gun.power_up()
pygame.quit()


