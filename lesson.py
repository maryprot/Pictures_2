from pygame.draw import *
import pygame
import numpy as np
pygame.init()


# Солнце
def sun(surface, coordinates, r):
    '''
    Рисует солнце с центром в точке (coordinates)
    и радиусом r
    '''
    circle(surface, yellow1, (r, r), r)
    screen.blit(surface, coordinates)

    
# Первый полигон(серая часть пустыни)
def desert_grey():
    polygon(screen,
            grey1,
            ((x1_1, y1_1),
             (x2_1, y2_1),
             (x3_1, y3_1),
             (x4_1, y4_1)))

    
# первая часть пустыни сверху(розовая)
def desert_pink():
    rect(screen,
        pink1,
        (left, top1, width1, height1))

    
# вторая часть пустыни сверху(желтая)
def desert_yellow_2():
    rect(screen,
         yellow0,
         (left, top2, width2, height2))

    
# Горы 1(верхние)
def mountain_1(surface, coordinates):
    '''
    Рисует первые горы с координатами центра(coordinates)
    и заданным масштабом
    '''
    polygon(surface,
            orange0,
            ((x1_2, y1_2),
             (x2_2, y2_2),
             (x3_2, y3_2),
             (x4_2, y4_2),
             (x5_2, y5_2),
             (x6_2, y6_2),
             (x7_2, y7_2),
             (x8_2, y8_2),
             (x9_2, y9_2),
             (x10_2, y10_2),
             (x11_2, y11_2),
             (x12_2, y12_2),
             (x13_2, y13_2),
             (x14_2, y14_2)))
    circle(surface, pink1, center_1, radius_1)
    ellipse(surface,
            orange0,
            (left_ellipse1,
             top_ellipse1,
             width_ellipse1,
             height_ellipse1))
    screen.blit(surface, coordinates)


def mountain_2(surface, coordinates):
    '''
    Рисует вторые горы с координатами центра(coordinates)
    и заданным масштабом 
    '''
    polygon(surface,
            red0,
            ((x1_3, y1_3),
             (x2_3, y2_3),
             (x3_3, y3_3),
             (x4_3, y4_3),
             (x5_3, y5_3),
             (x6_3, y6_3),
             (x7_3, y7_3),
             (x8_3, y8_3),
             (x9_3, y9_3),
             (x10_3, y10_3),
             (x10_3, y10_3),
             (x10_3, y10_3),
             (x11_3, y11_3),
             (x12_3, y12_3),
             (x13_3, y13_3),
             (x14_3, y14_3),
             (x15_3, y15_3)))
    ellipse(surface,
            red0,
            (left_ellipse2,
             top_ellipse2,
             width_ellipse2,
             height_ellipse2))
    
    screen.blit(surface, coordinates)


def mountain_3(surface, coordinates):
    '''
    Рисует третие горы с координатами центра(coordinates)
    и заданным масштабом 
    '''
    polygon(surface,
            darkgrey0,
            ((x1_4, y1_4),
             (x2_4, y2_4),
             (x3_4, y3_4),
             (x4_3, y4_4),
             (x5_4, y5_4),
             (x6_4, y6_4),
             (x7_4, y7_4),
             (x8_4, y8_4),
             (x9_4, y9_4),
             (x10_4, y10_4),
             (x11_4, y11_4),
             (x12_4, y12_4)))
    screen.blit(surface, coordinates)

    
def bird(x, y, s):
    '''
    x, y: задает крайнюю левую верхнюю точку птицы
    s: размер птицы
    '''
    x1, y1 = x + size[0] * s // 160 - s // 2, y
    # Правое крыло
    arc(screen,
        black,
        (x1, y1, size[0] * s // 160, size[1] * s // 120),
        np.pi / 2,
        np.pi,
        1 * s // 2)
    # Левое крыло
    arc(screen,
        black,
        (x, y, size[0] * s // 160, size[1] * s // 120),
        0,
        np.pi / 2,
        1 * s // 2)

# ввод данных
# Общие настройки
size = (800, 600) # Размер экрана
left = 0
FPS = 30
# первая часть пустыни сверху(розовая)
height1 = size[1] * 4 // 5
width1 = size[0]
top1 = size[1] * 1 // 5
# вторая часть пустыни сверху(желтая)
height2 = size[1] * 11 // 20
width2 = size[0]
top2 = size[1] * 9 // 20

# Параметры солнца
sun_coordinates = (400, 100) # Координаты центра 
radius_sun = 50 # Радиус
# Параметры  гор
mountain_1_scale = 1 # Масштаб первых гор
mountain_1_coordinates = (400, 300) # Координаты центра первых гор
mountain_2_scale = 1 # Масштаб вторых гор
mountain_2_coordinates = (400, 400) # Координаты центра вторых гор
mountain_3_scale = 1 # Масштаб третьих гор
mountain_3_coordinates = (400, 600) # Координаты центра третьих гор
# Цвета
black = (0, 0, 0)
darkgrey0 = (47, 79, 79)
pink1 = (250, 128, 114)
yellow0 = (244, 164, 96)
yellow1 = (230, 230, 0)
grey1 = (188, 143, 143)
orange0 = (255, 140, 0)
red0 = (178, 34, 34)

# Горы 1(верхние)
mountain_1_size = (int(size[0] * mountain_1_scale), # Задаются размеры экрана, на
                   int(size[1] * mountain_1_scale)) # котором изображаются первые горы. 
center_1 = (mountain_1_size[0] // 50, mountain_1_size[1]*2 // 5)
radius_1 = mountain_1_size[0] // 30
x1_2, y1_2 = 0, mountain_1_size[1] // 2
x2_2, y2_2 = mountain_1_size[0] // 40, mountain_1_size[1] * 17//40
x3_2, y3_2 = mountain_1_size[0] // 5, mountain_1_size[1] * 3//10
x4_2, y4_2 = mountain_1_size[0] // 4, mountain_1_size[1] * 19//60
x5_2, y5_2 = mountain_1_size[0] * 11//40, mountain_1_size[1] * 7//20
x6_2, y6_2 = mountain_1_size[0] * 9//20, mountain_1_size[1] * 11//25
x7_2, y7_2 = mountain_1_size[0] // 2, mountain_1_size[1] * 67//160
x8_2, y8_2 = mountain_1_size[0] * 11//20, mountain_1_size[1] * 367//800
x9_2, y9_2 = mountain_1_size[0] * 7//10, mountain_1_size[1] * 11//40
x10_2, y10_2 = mountain_1_size[0] * 4//5, mountain_1_size[1] * 14//40
x11_2, y11_2 = mountain_1_size[0] * 17//20, mountain_1_size[1] * 13//40
x12_2, y12_2 = mountain_1_size[0] * 18//20, mountain_1_size[1] * 15//40
x13_2, y13_2 = mountain_1_size[0] * 37//40, mountain_1_size[1] * 14//40
x14_2, y14_2 = mountain_1_size[0], mountain_1_size[1] * 18//40
height_ellipse1 = mountain_1_size[1] // 10
width_ellipse1 = mountain_1_size[0] // 20
left_ellipse1 = mountain_1_size[0] * 27//40
top_ellipse1 = mountain_1_size[1] * 11//40

# Горы 2(средние)
mountain_2_size = (int(size[0] * mountain_2_scale), # Задаются размеры экрана, на
                   int(size[1] * mountain_2_scale)) # котором изображаются вторые горы.
height_ellipse2 = mountain_2_size[1] // 2
width_ellipse2 = mountain_2_size[0] // 6
left_ellipse2 = mountain_2_size[1] // 50
top_ellipse2 = mountain_2_size[1] * 9//20
x1_3, y1_3 = mountain_2_size[0] * 4//25, mountain_2_size[1] * 50//75
x2_3, y2_3 = mountain_2_size[0] // 5, mountain_2_size[1] * 11//20
x3_3, y3_3 = mountain_2_size[0] * 7//25, mountain_2_size[1] * 207//340
x4_3, y4_3 = mountain_2_size[0] * 8//25, mountain_2_size[1] * 167//340
x5_3, y5_3 = mountain_2_size[0] * 11//25, mountain_2_size[1] * 177//340
x6_3, y6_3 = mountain_2_size[0] * 13//25, mountain_2_size[1] * 197//340
x7_3, y7_3 = mountain_2_size[0] * 15//25, mountain_2_size[1] * 187//340
x8_3, y8_3 = mountain_2_size[0] * 16//25, mountain_2_size[1] * 157//340
x9_3, y9_3 = mountain_2_size[0] * 20//25, mountain_2_size[1] * 187 // 340
x10_3, y10_3 = mountain_2_size[0] * 21//25, mountain_2_size[1] * 167//340
x11_3, y11_3 = mountain_2_size[0] * 22//25, mountain_2_size[1] * 177//340
x12_3, y12_3 = mountain_2_size[0] * 45//50, mountain_2_size[1] * 167//340
x13_3, y13_3 = mountain_2_size[0] * 24//25, mountain_2_size[1] * 162//340
x14_3, y14_3 = mountain_2_size[0] * 25//25, mountain_2_size[1] * 9//20
x15_3, y15_3 = mountain_2_size[0], mountain_2_size[1] * 3//5
# Первый полигон(серая часть пустыни)
x1_1, y1_1 = 0, size[1] * 36//48
x2_1, y2_1 = size[0], size[1] * 35//48 
x3_1, y3_1 = size[0], size[1] 
x4_1, y4_1 = 0, size[1]
# Горы 3(нижние)
mountain_3_size = (int(size[0] * mountain_3_scale), # Задаются размеры экрана, на
                   int(size[1] * mountain_3_scale)) # котором изображаются первые горы. 
x1_4, y1_4 = 0, mountain_3_size[1] // 2
x2_4, y2_4 = mountain_3_size[0] * 3//25, mountain_3_size[1] * 180//340
x3_4, y3_4 = mountain_3_size[0] * 5//25, mountain_3_size[1] * 250//340
x4_4, y4_4 = mountain_3_size[0] * 8//25, mountain_3_size[1] * 300//340
x5_4, y5_4 = mountain_3_size[0] * 11//25, mountain_3_size[1] * 310//340
x6_4, y6_4 = mountain_3_size[0] * 15//25, mountain_3_size[1] * 260//340
x7_4, y7_4 = mountain_3_size[0] * 18//25, mountain_3_size[1] * 290//340
x8_4, y8_4 = mountain_3_size[0] * 22//25, mountain_3_size[1] * 230//340
x9_4, y9_4 = mountain_3_size[0] * 23//25, mountain_3_size[1] * 220// 340
x10_4, y10_4 = mountain_3_size[0] * 25//25, mountain_3_size[1] * 210//340
x11_4, y11_4 = mountain_3_size[0], mountain_3_size[1]
x12_4, y12_4 = mountain_3_size[0] * 0, mountain_3_size[1]
# Птицы(координаты и размеры)
xb_1, yb_1, sizeb_1 = size[0] // 3, size[1] // 3, 10
xb_2, yb_2, sizeb_2 = size[0] // 4, size[1] // 4, 8
xb_3, yb_3, sizeb_3 = size[0] // 3, size[1] // 4, 9
xb_4, yb_4, sizeb_4 = size[0] // 2, size[1] // 3, 12
xb_5, yb_5, sizeb_5 = size[0] // 2, size[1] // 2, 13

# Основная программа
screen = pygame.display.set_mode(size) # Создаем основной экран с размерами size.
screen.fill(yellow0) # Рисуется небо.
desert_pink() # Рисуется розовая пустыня.
desert_yellow_2() # Рисуется желтая пустыня.

# Рисуем солнце.
sun_surface = pygame.Surface((radius_sun * 2, radius_sun * 2), pygame.SRCALPHA, 32) # Создаем доп.экран для солнышка.
sun_surface = sun_surface.convert_alpha()
sun_surface.set_alpha(0)
sun(sun_surface, sun_coordinates, radius_sun)

# Рисуем первые горы.
mountain_1_surface = pygame.Surface(mountain_1_size, pygame.SRCALPHA, 32) # Создаем доп.экран размера mountain_1_size для первых гор.
mountain_1_surface = mountain_1_surface.convert_alpha()
mountain_1_surface.set_alpha(0)
mountain_1(mountain_1_surface, (int(mountain_1_coordinates[0] - (mountain_1_size[0])/2), # Рисуем первые горы c координатами
                                int(mountain_1_coordinates[1] - (mountain_1_size[1])/2))) #  центра гор mountain_1_coordinates.

# Рисуем вторые горы.
mountain_2_surface = pygame.Surface(mountain_2_size, pygame.SRCALPHA, 32) # Создаем доп.экран размера mountain_2_size для вторых гор.
mountain_2_surface = mountain_2_surface.convert_alpha()
mountain_2_surface.set_alpha(0)
mountain_2(mountain_2_surface, (int(mountain_2_coordinates[0] - (mountain_2_size[0])/2), # Рисуем вторые горы c координатами
                                int(mountain_2_coordinates[1]  - 50 - (mountain_2_size[1])/2))) #  центра гор mountain_2_coordinates.
desert_grey()# Рисуется серая пустыня.
# Рисуем третьи горы.
mountain_3_surface = pygame.Surface(mountain_3_size, pygame.SRCALPHA, 32) # Создаем доп.экран размера mountain_3_size для третьих гор.
mountain_3_surface = mountain_3_surface.convert_alpha()
mountain_3_surface.set_alpha(0)
mountain_3(mountain_3_surface, (int(mountain_3_coordinates[0] - (mountain_3_size[0])/2), # Рисуем третие горы c координатами
                                int(mountain_3_coordinates[1]  - mountain_3_size[1]))) #  центра гор mountain_3_coordinates.
bird(xb_1, yb_1, sizeb_1)
bird(xb_2, yb_2, sizeb_2)
bird(xb_3, yb_3, sizeb_3)
bird(xb_4, yb_4, sizeb_4)
bird(xb_5, yb_5, sizeb_5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
