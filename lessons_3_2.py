#!/usr/bin/env python
# coding: utf-8

# Задание 1. Рисование линий мышью
# 
# Создайте программу, которая позволяет пользователю рисовать линии на экране с помощью мыши. При движении мыши должны появляться линии, которые сохраняются на экране.

# In[24]:


import pygame
import sys
from random import randint

#Функция для определения рандомного цвета:
def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def main():
    pygame.init()
    
    #Определение констант:
    WIDTH, HEIGHT = 800, 600 #размеры окна приложения
    WHITE = (255, 255, 255) #цвет фона окна приложения
    LINE_WIDTH = 5 #ширина рисуемых линий, в пикселях
    
    
    #Создание окна:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    screen.fill(WHITE)
    pygame.display.set_caption("Рисуем линии")

    #Переменные:
    mouse_position = (0, 0) #x, y координаты для рисования, к которым ведём мышь    
    last_pos = None #конечные координаты для рисования, которые становятся стартовыми в след.итерации цикла
    draw_go = False #флаг, определяющий, рисуем ли в текущий момент

    #Основной игровой цикл:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #выход из приложения
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION: #двигаем мышку с зажатой ЛКМ
                if draw_go == True:
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos != None:
                        pygame.draw.line(screen, rand_color(), last_pos, mouse_position, LINE_WIDTH)
                    last_pos = mouse_position
            elif event.type == MOUSEBUTTONUP: #отпустили ЛКМ - обнулили все координаты, чтобы рисовать новые линии, сохраняя старые
                mouse_position = (0, 0)
                last_pos = None
                draw_go = False                
            elif event.type == MOUSEBUTTONDOWN: #зажали ЛКМ
                draw_go = True

        pygame.display.update() #обновили экран

if __name__ == "__main__":
    main()


# Задание _2 . Круги
# 
# Пусть в центре экрана нарисован круг. При нажатии левой клавиши мыши , радиус круга увеличивается на 20%, при нажатии клавиши пробел уменьшается на 20%.

# In[27]:


import pygame
import sys

pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
AQUA = (0, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Круг меняет радиус")

# Начальные координаты и радиус круга
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 50
circle_color = AQUA

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #Левая кнопка мыши (ЛКМ)
            #При нажатии ЛКМ радиус круга увеличивается на 20%
            circle_radius = circle_radius + circle_radius * 0.2
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #Нажата клавиша "Пробел"
            #При нажатии пробела радиус круга уменьшается на 20%
            circle_radius = circle_radius - circle_radius * 0.2

    # Обновление игры
    # Отрисовка фона
    screen.fill(WHITE)

    # Рисование круга
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    # Задаем частоту кадров
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit() 


# In[ ]:




