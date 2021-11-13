import math
from random import choice
from random import random
from random import randint
from datetime import datetime

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

COUNT_TARGETS = 2

def get_table():
    try:
        with open('results.txt', 'r') as f:
            table = [tuple(line.split()) for line in f]
            table = sorted(table, key=lambda x: int(x[0]))
            for line in table:
                print(' '.join(line))
                
    except FileNotFoundError:
        pass
            
def save_points(cnt_points):
    with open('results.txt', 'a') as f:
        current_time = datetime.now()
        print(cnt_points, current_time, file=f)
        
class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.free = False

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.free:
            self.live -= 1

        # FIXME
        self.x += self.vx
        self.y -= self.vy
        
        if abs(self.vy) + abs(self.vx) < 20 and self.y >= 590 - self.r:
            self.vx *= 0.9
            self.vy *= 0.9
            if abs(self.vy) + abs(self.vx) < 3:
                self.vx = 0
                self.vy = 0
                self.y = 600 - self.r
                self.color = WHITE
        else:
            self.vy -= 1.5
        
        if self.x >= 800 - self.r:
            self.vx = -self.vx * 0.7
            self.vy *= 0.7
            self.x = 800 - self.r - 1
            
        if self.y >= 600 - self.r:
            self.vy = -self.vy * 0.7
            self.vx *= 0.7
            self.y = 600 - self.r - 1

    def draw(self):
        if self.live > 0:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        
        distance = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5 
    
        return distance <= self.r + obj.r


class Gun:
    def __init__(self, screen):
        self.screen = screen
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
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        
        
        pygame.draw.line(screen, self.color + self.f2_power*3, [40, 450], 
                         [40 + self.f2_power*math.cos(self.an), 450 + self.f2_power*math.sin(self.an)], 10)
        pass

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    # FIXME: don't work!!! How to call this functions when object is created?
    def __init__(self):
        self.new_target()
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(10, 50)
        self.a = random() * math.pi * 2
        self.v = randint(5, 10)
        self.vx = self.v * math.sin(self.a)
        self.vy = self.v * math.cos(self.a)
        self.color = choice(GAME_COLORS)
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        
    def move(self):
    
        self.x += self.vx
        self.y -= self.vy
    
        
        self.v = randint(5, 10)
        self.a += random() / 5 - 0.1
        
        self.vx = self.v * math.sin(self.a)
        self.vy = self.v * math.cos(self.a)

    
        if self.x >= 800 - self.r:
            self.a += math.pi / 2
            self.vx = -self.vx
            self.x = 800 - self.r - 1
            
        if self.x <= 400 + self.r:
            self.a += math.pi / 2
            self.vx = -self.vx
            self.x = 400 + self.r + 1
            
        if self.y >= 600 - self.r:
            self.a += math.pi / 2
            self.vy = -self.vy
            self.y = 600 - self.r - 1
            
        if self.y <= self.r:
            self.a += math.pi / 2
            self.vy = -self.vy
            self.y = self.r + 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

font = pygame.font.Font(pygame.font.get_default_font(), 36)
text_surface = font.render('', True, (0, 0, 0))
cnt_tries = 0
time_label = 0

cnt_points = 0
points_surface = font.render('0', True, (0, 0, 0))

targets = [Target() for i in range(COUNT_TARGETS)]

while not finished:
    screen.fill(WHITE)
    screen.blit(points_surface, dest=(10, 10))
    if time_label > 0:
        screen.blit(text_surface, dest=(100, 100))
        time_label -= 1
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif time_label > 0:
            continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            cnt_tries += 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for target in targets:
        target.move()
            
    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target) and not b.free and time_label == 0:
            
                targets.remove(target)
            
                if not targets:
                    text_surface = font.render('Вы поразили цель за ' + str(cnt_tries) + ' попыт' + \
                                           ('ку' if cnt_tries == 1 else 'ки' if cnt_tries <= 4 else 'ток'), True, (0, 0, 0))
                    cnt_points += 1
                    points_surface = font.render(str(cnt_points), True, (0, 0, 0))
                    time_label = 50
                    cnt_tries = 0
                    targets = [Target() for i in range(COUNT_TARGETS)]
        if b.color == WHITE:
            balls.remove(b)
    gun.power_up()

print(f'Ваше количество очков: {cnt_points}')

save_points(cnt_points)

get_table()
    
pygame.quit()