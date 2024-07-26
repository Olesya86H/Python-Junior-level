#!/usr/bin/env python
# coding: utf-8

# 1. Создать окно. Изменить цвета фона каждую секунду.

# In[4]:


import pygame
import time
from random import randint

#функция для определения рандомного цвета
def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

# Инициализация Pygame
pygame.init()

# Установка размеров окна
window_width = 800
window_height = 600

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(rand_color())

    # Получаем текущее время
    #current_time = time.strftime("%H:%M:%S")

    # Устанавливаем новый заголовок окна
    pygame.display.set_caption("RGB_code: " + str(rand_color()))

    # Обновляем экран
    pygame.display.flip()

    # Ждем 1 секунду
    time.sleep(1)

# Выход из программы
pygame.quit()


# 2. Нарисовать светофор. Сделать, так чтобы сначала загорался красный, потом желтый, потом зеленый.

# In[2]:


import pygame
import time

pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255) #белый    
GREY = (128, 128, 128) #серый 
RED = (255, 0, 0) #красный
YELLOW = (255, 255, 0) #желтый   
GREEN = (0, 128, 0) #зеленый 
BLACK = (0, 0, 0) #черный  

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Светофор")

#Начальная отрисовка:
screen.fill(WHITE)
pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))
pygame.draw.ellipse(screen, GREY, (325, 100, 100, 100))
pygame.draw.ellipse(screen, GREY, (325, 250, 100, 100))
pygame.draw.ellipse(screen, GREY, (325, 400, 100, 100))
pygame.display.flip()
time.sleep(1) #задержка
    
# Основной игровой цикл
running = True
while running:
# Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Обновление игры    
    screen.fill(WHITE)
        
    #поехали переключать цвета:
    #Красный:
    pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))
    pygame.draw.ellipse(screen, RED, (325, 100, 100, 100))
    pygame.draw.ellipse(screen, GREY, (325, 250, 100, 100))
    pygame.draw.ellipse(screen, GREY, (325, 400, 100, 100))
    pygame.display.flip()
    time.sleep(1) #задержка
    
    #Желтый:
    pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))
    pygame.draw.ellipse(screen, GREY, (325, 100, 100, 100))
    pygame.draw.ellipse(screen, YELLOW, (325, 250, 100, 100))
    pygame.draw.ellipse(screen, GREY, (325, 400, 100, 100))
    pygame.display.flip()
    time.sleep(1) #задержка
    
    #Зеленый:
    pygame.draw.rect(screen, BLACK, (250, 50, 250, 500))
    pygame.draw.ellipse(screen, GREY, (325, 100, 100, 100))
    pygame.draw.ellipse(screen, GREY, (325, 250, 100, 100))
    pygame.draw.ellipse(screen, GREEN, (325, 400, 100, 100))
    pygame.display.flip()
    time.sleep(1) #задержка


# Завершение программы
pygame.quit()

