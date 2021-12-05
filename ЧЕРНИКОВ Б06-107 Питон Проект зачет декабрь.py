##Черников Николай Б06-107


#Тема-игра в стиле космического шутера-"Space Battle"(космич.корабль против пришельцев)




#В модуле pygame




#План: 
#1 сделать пушку-космич.корабль 
#2 перемещать ее по горизонтали 
#3 задать пули и сделать их вылетающими из пушки
#4 сделать сначала 1, затем армию пришельцев
#5 движение пришельцев на пушку
#6 уничтожение пришельцев
#7 очки за пришельца-вывести на экран статистику, счет
#8 вывести рекорд и документ, в котором он будет содержаться
#9 вывести обновление армии пришельцев, если все пришельцы убиты и проверить и сделать обновление пушки, пуль, экрана
#10 вывести количество жизней и если они кончатся-игра закрывается
#11 Готово! Осталось проверить, что нигде нет ошибок и можно играть






#Полный код:





import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
import time
import pygame.font#шрифт


class Ino(pygame.sprite.Sprite):#класс 1 пришельца

    def __init__(self, screen):#инициалищируем и создаем начальную позицию пришельца
        super(Ino, self).__init__()#Функция super() в Python позволяет нам явно ссылаться на родительский класс
        self.screen = screen
        self.image = pygame.image.load('Downloads/ino.png')#пришелец-картинка
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width#координаты пришельца-прямоугольная область 
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):#вывод пришельца на экран(рисуем с помощью blit)
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.25#перемещение пришельца
        self.rect.y = self.y


def create_army(screen, inos): #армия пришельцев
    ino = Ino(screen)
    ino_height = ino.rect.height
    ino_width = ino.rect.width
    number_ino_x = int((600 - 2 * ino_width) / ino_width)
    number_ino_y = int((700 - 100 - 2 * ino_height) / ino_height)#параметры правильного отступа и размещения пришельцев

    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number#заселяем поле пришельцами
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height * 2 + ino.rect.height * row_number
            inos.add(ino)#добавляет на экран пришельцев


def check_high_score(stats, sc):#документ, который хранит сведения о максимальном количестве набранных очков-проверка рекорда
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:#документ, где хранится рекорд игры(txt)
            f.write(str(stats.high_score))


def gun_kill(stats, screen, sc, gun, inos,  bullets):#столкновение пушки и пришельцев
    global F
    if stats.guns_left > 0:
        stats.guns_left -= 1#снижение уровня жизни
        sc.image_guns()
        inos.empty()#удаление пришельцев
        bullets.empty()
        create_army(screen, inos)
        time.sleep(1)#время обновления армии и просто игры после столкновения
    else:
        stats.run_game = False
        F = False


def update_inos(stats, screen, sc, gun, inos, bullets):#обновление позиции пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):#проверяет, столyкнулся ли конкретный спрайт с любым из спрайтов из группы. Функция принимает первым аргументом спрайт, чья коллизия проверяется, вторым – группу.
        gun_kill(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):#проверка, добралась ли армия пришельцев до края экрана
    #screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:#если ниж.часть пришельца там где вверх пушки- на оси Оу, то удаление 1 жизни
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


class Gun(Sprite):#инициализация пушки

    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Downloads/gun.png')#изображение пушки
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx#перемещение произвдится по координате центра пушки
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):#отображение пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):#перемещение на 3 вправо и 3 влево пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 3
        if self.mleft and self.rect.left > 0:
            self.center -= 3
        self.rect.centerx = self.center

    def create_gun(self):#размещает пушку по центру внизу
        self.center = self.screen_rect.centerx


class Bullet(pygame.sprite.Sprite):#инициализируем пули пушки

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)#размер пуль
        self.color = (139, 195, 74)
        self.speed = 3#скорость пули
        self.rect.centerx = gun.rect.centerx#центр пули-там, где центр пушки-исходная позиция
        self.rect.top = gun.rect.top#верхняя координата пуль там, где верх пушки
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed#скорость перемещения пуль-они движутся, разумеется, вертикально
        self.rect.y = self.y

    def draw_bullet(self):#отображаем пулю
        pygame.draw.rect(self.screen, self.color, self.rect)


def events(screen, gun, bullets):
    global F
    for event in pygame.event.get():#в каком случае игра продолжается
        if event.type == pygame.QUIT:
            F = False
        elif event.type == pygame.KEYDOWN:#команды для перемещения пушки от нажатия кнопок клавиатуры
            if event.key == pygame.K_d:#клавиша d перемещает вправо, клавиша a влево
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):#обновление экрана
    screen.fill(bg_color)
    sc.show_score()#мы видим за счет этого статистику на экране игры
    for bullet in bullets.sprites():#отрисовка пуль именно по draw
        bullet.draw_bullet()
    gun.output()#мы видим пушку на экране игры
    inos.draw(screen)
    pygame.display.flip()# обновляет содержимое основного окна игры


def update_bullets(screen, stats, sc, inos, bullets):#обновление позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)#удаление и пушки, и пришельцев
    if collisions:#если происходит столкновение
        for inos in collisions.values():
            stats.score += 10 * len(inos)#добавляется 10 очков за пришельца, в которого попала пуля-уничтожение его
        stats.score += 10
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:#если кончились(уничтожены) пришельцы, тогда что мы делаем
        bullets.empty()
        create_army(screen, inos)


class Scores:#вывод игровой информации 

    def __init__(self, screen, stats):#инициализируем подсчет очков
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 32)#параметры шрифта, на котором пишем очки
        self.image_score()
        self.image_high_score()
        self.image_guns()#
        
    def image_score(self):#преобразует текст счета в графическое изображение
        self.score_img = self.font.render(str(self.stats.score), True,
                self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()#место, где располагается надпись-количество очков на данный момент
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_guns(self):#поле для вырисовки количества жизней наверху-число пушек
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def image_high_score(self):#преобразует текст наибольшего счета(рекорда) в графическое изображение
        self.high_score_image = \
            self.font.render(str(self.stats.high_score), True,
                             self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()#координаты расположения надписи-рекорд(max балл)
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):#вывод счета на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)

class Stats:#отслеживание статистики

    def __init__(self):#инициализир.статистику
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())
        
    def reset_stats(self):#статистика, которая меняется во время игры
        self.guns_left = 2
        self.score = 0

pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Star Battle')
bg_color = (0, 0, 0)#фон
gun = Gun(screen)
bullets = Group()
inos = Group()
create_army(screen, inos)
stats = Stats()
sc = Scores(screen, stats)

F = True
while F:
    events(screen, gun, bullets)
    if stats.run_game:#во время игры 
        gun.update_gun()
        update(bg_color, screen, stats, sc, gun, inos, bullets)#то, что мы обновляем
        update_bullets(screen, stats, sc, inos, bullets)
        update_inos(stats, screen, sc, gun, inos, bullets)

pygame.quit()