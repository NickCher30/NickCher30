import pygame
from pygame.draw import*
from math import pi,ceil
from math import sin, cos, floor #floor округление в меньшую сторону
from random import randint
pygame.init()
FPS=100
screen=pygame.display.set_mode((900,900))#размеры экрана
def polar_dekart(r, alpha, rad=False):#для удобства исключили счисление в радианах-создано для пояса астероидов
    if not rad:
        alpha=alpha*2*pi/360
    x=r*cos(alpha)
    y=r*sin(alpha)
    return {"y":y+450, "x":x+450}
pygame.draw.circle(screen, (73,66,61), (450,450), 201, 40)#Пояс астероидов
pygame.draw.circle(screen, (97,66,61), (450,450), 561, 112)#Пояс Койпера
from math import sin, cos, floor
class Planet:#задаем класс планет
    A=0 #при любом значении, однако, не влияет на картину
    color = "white"
    r=0
    v=0
    def __init__(self, A, color, r, v, size, name="unknown", is_Planet=True):#__init __() – это встроенная функция в Python, которая вызывается всякий раз, когда создается объект.
        self.A=A #A is angle, это также и как бы начало наших планет
        self.color=color#цвет
        self.r=r
        self.v=v #v-speed, r-orbit radius
        self.x=0
        self.y=0
        self.old_x=0 #это старые координаты, которые образуются при каждом перемещении планеты, и в них сразу появляется черная тень, закрывающая след планты
        self.old_y=0
        self.size=size #размер планет-их собственный радиус
        self.is_Planet=is_Planet
    def Get_X(self):# Coordinate X
        self.old_x=self.x
        self.x=self.r*cos(self.A)#зависимость собственной координаты х от собственного угла(перемещение в полярной системе координат объекта)
        return self.x
    def Get_OX(self):# Coordinate Old X
        return self.old_x
    def Get_Omega(self):#Angle speed-угловая скорость
        return self.v/self.r
    def Get_A(self, t=1):#Angle-перемещение планеты и ее появление на экране-линейная скорость (v=w*t из физики)
        self.A+=self.Get_Omega()*t
        return self.A
    def Get_Y(self):# Coordinate Y
        self.old_y = self.y
        self.y = self.r*sin(self.A)
        return self.y
    def Get_OY(self):# Coordinate Old Y
        return self.old_y
    def __str__(self): #moving on a circle-движение по круговой орбите-но оно необязательно
        return "X:"+str(self.Get_X())+"Y:"+str(self.Get_Y())
Planets=[]
for i in range(309):#сведения для 309 астероидов
    size=randint(1,6)
    size=size**4/216  #рисуем астероиды в поясе астероидов такие, что маленьких больше, чем больших
    if size<1:
        size=1
    r=randint(160+ceil(size)+1,200-ceil(size)-1)#радиусы астероидов(ceil-округление в большую сторону)
    alpha=randint(0,360)#угол перемещения
    coords=polar_dekart(r,alpha)#ПСО для перемещения
    Planets.append(Planet(alpha*pi/180, (128,128,128), r, 0.18+randint(1,12)/100, size, is_Planet=False))#движение астероидов
Mercury=Planet(0, (119,181,161), 50, 0.66, 4.65, "Mercury")#Mercury(в скобках по порядку:угол, цвет, расстояние от солнца, скорость линейная, радиус,сам объект)
Venus=Planet(0, (181,121,0), 74, 0.48, 9.3, "Venus")#Venus
Planets.append(Planet(0, "blue", 100, 0.4, 9.9, "Earth"))#Earth Землю задали по-особенному-она как центр вращеня луны
Earth_index=len(Planets)-1 #задаем землю как особый объект с особым индексом - -1 так как имеет при себе вращающ.Луну
Mars=Planet(0, "red", 143, 0.33, 5.5, "Mars")#Mars
Jupiter=Planet(0, "navajowhite", 225, 0.176, 20.95, "Jupiter")#Jupiter
Saturn=Planet(0, "tan",269, 0.122, 15.999999, "Saturn")#Saturn
Uranus=Planet(0, (108,146,175), 316, 0.108, 10.55, "Uranus")#Uranus
Neptun=Planet(0, "purple", 354, 0.08, 10.05, "Neptun")#Neptun
Plython=Planet(0, "gray", 425, 0.039, 3.75, "Plython")#Plython
Moon=Planet(0, (255,255,255), 12, 1, 2, "Moon", is_Planet=False)
Earth=Planets[Earth_index]#необходимо для того, чтобы задать землю как центр вращения луны!!!!!
clock=pygame.time.Clock()
finished=False
while not finished:
    clock.tick(FPS)
    pygame.draw.circle(screen,(0,0,0), (Moon.Get_OX()+450+Earth.Get_OX(), Moon.Get_OY()+450+Earth.Get_OY()), Moon.size+2)#планеты себя не отрисовывают
    for p in Planets:#можно задать для всех планет, но задали именно для земли(вокруг него вращается Луна)
        if p.is_Planet:
            bg_color=(0,0,0)# черный задний фон-земля не оставляет свой след
        else:
            bg_color=(73,66,61)#цвет астероидов-они как бы не планеты, для них-отдельно
        pygame.draw.circle(screen,bg_color, (p.Get_OX()+450, p.Get_OY()+450), p.size+1)#создать темный фон от движения луны
        p.Get_A()
        x=floor(p.Get_X()) #округление
        y=floor(p.Get_Y())
        if p.is_Planet:
            pygame.draw.circle(screen, "white", (450,450), p.r, width=1)# Earth's orbit
        pygame.draw.circle(screen, p.color, (x+450,y+450), p.size)#Earth Planet - draw
        pygame.draw.circle(screen, p.color, (x+450,y+450), p.size)#Earth Planet - draw
    pygame.draw.circle(screen,(0,0,0), (Earth.Get_OX()+450, Earth.Get_OY()+450), 8)#Это помогает не оставлять планете след после себя, последнее число-радиус образ.черного шара, блокирующего образование следа
    pygame.draw.circle(screen,(0,0,0), (Mercury.Get_OX()+450, Mercury.Get_OY()+450), 10)
    pygame.draw.circle(screen,(0,0,0), (Venus.Get_OX()+450, Venus.Get_OY()+450), 10)
    pygame.draw.circle(screen,(0,0,0), (Mars.Get_OX()+450, Mars.Get_OY()+450), 10)
    pygame.draw.circle(screen,(0,0,0), (Jupiter.Get_OX()+450, Jupiter.Get_OY()+450), 20)
    pygame.draw.circle(screen,(0,0,0), (Saturn.Get_OX()+450, Saturn.Get_OY()+450), 17)
    pygame.draw.circle(screen,(0,0,0), (Uranus.Get_OX()+450, Uranus.Get_OY()+450), 15)
    pygame.draw.circle(screen,(0,0,0), (Neptun.Get_OX()+450, Neptun.Get_OY()+450), 14)
    pygame.draw.circle(screen,(0,0,0), (Plython.Get_OX()+450, Plython.Get_OY()+450), 4)#если удалить эту строку-планета оставляет за собой колею
    
    
    Moon.Get_A()#за счет get_a планета перемещается по своей орбите впринципе!!!!
    x=floor(Moon.Get_X()) #округление
    y=floor(Moon.Get_Y())
    pygame.draw.circle(screen, Moon.color, (x+450+Earth.Get_X(),y+450+Earth.Get_Y()), Moon.size)#Луна

    x=floor(Mercury.Get_X())#за счет этого планета получает свою первую координату-прорисовывается и начинает свое движение-округление
    y=floor(Mercury.Get_Y())
    Mercury.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Mercury.r, width=1)# Mercury's orbit Меркурий
    pygame.draw.circle(screen, Mercury.color, (x+450,y+450), 4.65)#Mercury Planet - draw
    
    
    x=floor(Venus.Get_X())
    y=floor(Venus.Get_Y())
    Venus.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Venus.r, width=1)# Venus's orbit
    pygame.draw.circle(screen, Venus.color, (x+450,y+450), 9.3)#Venus Planet - draw Венера
    
    x=floor(Earth.Get_X()) #округление
    y=floor(Earth.Get_Y())
    Earth.Get_A()
    pygame.draw.circle(screen, "white", (450,450), Earth.r, width=1)# Earth's orbit
    pygame.draw.circle(screen, Earth.color, (x+450,y+450), 9.9)#Earth Planet - draw Земля

    x=floor(Mars.Get_X())
    y=floor(Mars.Get_Y())
    Mars.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Mars.r, width=1)# Mars's orbit
    pygame.draw.circle(screen, Mars.color, (x+450,y+450), 5.5)#Mars Planet - draw Марс 
    
    x=floor(Jupiter.Get_X())
    y=floor(Jupiter.Get_Y())
    Jupiter.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Jupiter.r, width=1)# Jupiter's orbit Юпитер
    pygame.draw.circle(screen, Jupiter.color, (x+450,y+450), 20.95)#Jupiter Planet - draw
    
    x=floor(Saturn.Get_X())
    y=floor(Saturn.Get_Y())
    Saturn.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Saturn.r, width=1)# Saturn's orbit
    pygame.draw.circle(screen, Saturn.color, (x+450,y+450), 17)#Saturn Planet - draw Сатурн
    
    x=floor(Uranus.Get_X())
    y=floor(Uranus.Get_Y())
    Uranus.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Uranus.r, width=1)# Uranus's orbit
    pygame.draw.circle(screen, Uranus.color, (x+450,y+450), 10.55)#Uranus Planet - draw

    x=floor(Neptun.Get_X())
    y=floor(Neptun.Get_Y())
    Neptun.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Neptun.r, width=1)# Neptun's orbit
    pygame.draw.circle(screen, Neptun.color, (x+450,y+450), 10.05)#Neptun's Planet - draw Нептун

    x=floor(Plython.Get_X())
    y=floor(Plython.Get_Y())
    Plython.Get_A()
    pygame.draw.circle(screen, (255,255,255), (450,450), Plython.r, width=1)# Plython's orbit Плутон
    pygame.draw.circle(screen, Plython.color, (x+450,y+450), 3.75)#Plython's Planet - draw

    pygame.draw.circle(screen, "yellow", (450,450), 34.5)#солнце в центре
    
    for event in pygame.event.get():#выход из программы
        if event.type==pygame.QUIT:
            finished=True
    pygame.display.update() 
pygame.quit()