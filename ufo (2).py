import pygame
from pygame.draw import *

pygame.init()

# Тарелка

WHITE = (255, 255, 255)
GREY = (153, 153, 153)
LIGHT_GREY = (204, 204, 204)
DIRTY_YELLOW = (200, 150, 45)
RED = (150, 10, 10)
BLACK = (0, 0, 0)
GREEN = (20, 150, 20)

def UFO(x, y, width, height):
    polygon = pygame.Surface((800, 800), pygame.SRCALPHA)   
    pygame.draw.polygon(polygon, LIGHT_GREY + (128,), [[x - width * 0.1, y + height * 0.2], 
                                             [x + width * 0.1, y + height * 0.2], 
                                             [x + width * 0.5, y + height * 2.5], 
                                             [x - width * 0.5, y + height * 2.5]])
    screen.blit(polygon, (0, 0))  # Свет
    
    
    pygame.draw.ellipse(screen, GREY, (x - width//2, y - height // 2, width, height))  # Основа
    
    width_top = int(width * 0.7)
    height_top = int(height * 0.7)
    pygame.draw.ellipse(screen, LIGHT_GREY, (x  - width_top // 2, y - height_top // 2 - int(height * 0.25), width_top, height_top))  # Навершие
    
    for xx, yy in [(x - width * 0.45, y - height * 0.1),
                   (x - width * 0.3, y + height * 0.12),
                   (x - width * 0.1, y + height * 0.18),
                   (x + width * 0.1, y + height * 0.14),
                   (x + width * 0.3, y - height * 0.05)]:
        pygame.draw.ellipse(screen, WHITE, (xx, yy, width // 7, height // 4))  # Фары
        
# Фон
        
def background():
    pygame.draw.rect(screen, DIRTY_GREEN, (0, h * 0.4, w, h))
    pygame.draw.rect(screen, DIRTY_BLUE, (0, 0, w, h * 0.4))
    pygame.draw.line(screen, GREY, [0, h * 0.4], [w, h * 0.4], 1)
    
# Существо
    
def man(screen, x, y, size, is_transfomed=False):
    man_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
    
    
    
    for xx, yy, width, height in [(x - size * 0.1, y - size * 0.2, size * 0.2, size * 0.4),  # Туловище
                                 (x - size * 0.11, y + size * 0.1, size * 0.1, size * 0.15), # Левое бедро
                                 (x + size * 0.01, y + size * 0.12, size * 0.1, size * 0.15), # Правое бедро
                                 (x - size * 0.11, y + size * 0.22, size * 0.06, size * 0.15), # Правая ляжка
                                 (x + size * 0.06, y + size * 0.25, size * 0.06, size * 0.15), # Левая ляжка
                                 (x - size * 0.18, y - size * 0.13, size * 0.08, size * 0.05),# Левый локоть
                                 (x + size * 0.13, y - size * 0.11, size * 0.08, size * 0.05), # Правый локоть
                                 (x + size * 0.2, y - size * 0.14, size * 0.08, size * 0.045), # Правая ладонь
                                 (x + size * 0.05, y - size * 0.35, size * 0.03, size * 0.05), # Услики
                                 (x - size * 0.05, y - size * 0.35, size * 0.03, size * 0.05),
                                 (x + size * 0.07, y - size * 0.37, size * 0.05, size * 0.035),
                                 (x - size * 0.06, y - size * 0.4, size * 0.03, size * 0.05),
                                 (x + size * 0.12, y - size * 0.39, size * 0.05, size * 0.035),
                                 (x - size * 0.11, y - size * 0.44, size * 0.05, size * 0.05)]: 
        pygame.draw.ellipse(man_surface, DIRTY_YELLOW, (xx, yy, width, height))

    for xx, yy, r in [(x + size * 0.15, y + size * 0.38, size * 0.04),  # Правая ступня
                     (x - size * 0.14, y + size * 0.34, size * 0.04),   # Левая ступня
                     (x - size * 0.08, y - size * 0.15, size * 0.04),   # Левое плечо
                     (x + size * 0.12, y - size * 0.13, size * 0.04), # Правое плечо
                     (x - size * 0.16, y - size * 0.05, size * 0.03), # Левая ладонь
                     ]: 
        pygame.draw.circle(man_surface, DIRTY_YELLOW, (xx, yy), r)
    pygame.draw.circle(man_surface, RED, (x + size * 0.32, y - size * 0.19), size * 0.07) # Яблоко
    pygame.draw.line(man_surface, BLACK, [x + size * 0.32, y - size * 0.25],  [x + size * 0.35, y - size * 0.3], 1) # Хвостик
    pygame.draw.ellipse(man_surface, GREEN, (x + size * 0.32, y - size * 0.34, size * 0.025, size * 0.07)) # Листок
    
    pygame.draw.circle(man_surface, DIRTY_YELLOW, (x , y - size * 0.21),  size * 0.05)                 # Голова
    pygame.draw.ellipse(man_surface, DIRTY_YELLOW, (x - size * 0.09, y - size * 0.3, size * 0.12, size * 0.09))
    pygame.draw.ellipse(man_surface, DIRTY_YELLOW, (x - size * 0.02, y - size * 0.3, size * 0.12, size * 0.09))
    
    pygame.draw.circle(man_surface, BLACK, (x - size * 0.04, y - size * 0.25), size * 0.03)  # Глаза
    pygame.draw.circle(man_surface, BLACK, (x + size * 0.04, y - size * 0.25), size * 0.025)
    
    pygame.draw.circle(man_surface, WHITE, (x - size * 0.033, y - size * 0.24), size * 0.01)  # Зрачки
    pygame.draw.circle(man_surface, WHITE, (x + size * 0.045, y - size * 0.24), size * 0.009)
    
    man_surface = pygame.transform.flip(man_surface, is_transfomed, False)
    screen.blit(man_surface, (0, 0))

# Облако

def cloud(screen, x, y, width, height, color):
    cloud = pygame.Surface((2000, 2000), pygame.SRCALPHA)   
    pygame.draw.ellipse(cloud, color + (150,), (x, y, width, height))
    cloud = pygame.transform.smoothscale(cloud, (25, 15))
    cloud = pygame.transform.smoothscale(cloud, (width, height))
    screen.blit(cloud, (0, 0))
    
FPS = 30
w = 800
h = 800
screen = pygame.display.set_mode((w, h))

DIRTY_GREEN = (34, 43, 0)
DIRTY_BLUE = (0, 34, 43)
DIRTY_GREY = (123, 123, 123)
BLACK = (50, 50, 50)

background()

pygame.draw.circle(screen, DIRTY_GREY, (550, 120), w // 12)

for x, y, width, height, color in [(600, 300, 1000, 600, LIGHT_GREY),
                                   (400, 200, 800, 600, GREY),
                                  (200, 400, 600, 400, GREY),
                                  (300, 1000, 700, 400, GREY),
                                  (200, 500, 700, 500, BLACK),
                                  (1200, 200, 700, 500, BLACK),
                                  (100, 100, 800, 500, GREY),
                                  (1300, 50, 800, 500, GREY)]:
    cloud(screen, x, y, width, height, color)

for x, y, size, is_transformed in [(580, 450, 150, True),
                                   (700, 420, 120, True),
                                   (100, 580, 160, False),
                                   (300, 630, 100, False),
                                  (600, 550, 300, False)]:
        man(screen, x, y, size, is_transformed)
        
        
UFO(150, 240, 270, 100)
UFO(400, 270, 100, 37)
UFO(700, 240, 150, 56)


pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()