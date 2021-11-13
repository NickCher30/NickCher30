import pygame
from pygame.draw import *
from random import randint
from datetime import datetime
pygame.init()

FPS = 30
width = 1200
height = 800
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

def get_table():
    try:
        with open('results.txt', 'r') as f:
            table = [tuple(line.split()) for line in f]
            table = sorted(table, key=lambda x: int(x[0]))
            for line in table:
                print(' '.join(line))
                
    except FileNotFoundError:
        pass
            
def save_points(cnt):
    with open('results.txt', 'a') as f:
        current_time = datetime.now()
        print(cnt, current_time, file=f)

class Ball:
    def __init__(self):
        self.r = randint(30, 50)
        self.x = randint(self.r + 3, width - self.r - 3)
        self.y = randint(self.r + 3, height - self.r - 3)
        self.vx = randint(-20, 20)
        self.vy = randint(-20, 20)  
        self.color = COLORS[randint(0, 5)]

    def update(self):
        if self.x >= width - self.r or self.x <= self.r:
            self.vx = -self.vx
            self.vy = randint(-20, 20)
        if self.y >= height - self.r or self.y <= self.r:
            self.vy = -self.vy
            self.vx = randint(-20, 20)
        self.x += self.vx
        self.y += self.vy
        circle(screen, self.color, (self.x, self.y), self.r)
    
    def is_near(self, p):
        return (self.x - p[0])**2 + (self.y - p[1])**2 <= self.r*self.r
    
balls = []
for i in range(5):
    balls.append(Ball())    
    
cnt = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_fired = False
            for i in range(len(balls)):
                if balls[i].is_near(event.pos):
                    cnt += 1
                    is_fired = True
                    balls.pop(i)
                    balls.append(Ball())
                    pygame.display.update()
            if not is_fired:
                cnt -= 1

    for ball in balls:
        ball.update()
    pygame.display.update()
    screen.fill(BLACK)
print(cnt)
save_points(cnt)
get_table()
pygame.quit()
