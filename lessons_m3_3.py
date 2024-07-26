#!/usr/bin/env python
# coding: utf-8

# Задание 1. Сделайте текст «Доброе утро!» желтым цветом на зеленом фоне, чтобы он двигался снизу вверх.

# In[1]:


import pygame as pg
import sys
import time

#Константы:
YELLOW = (255, 255, 0) #желтый   
LIGHT_GREEN = (200, 255, 200) #зеленый 
WIDTH, HEIGHT = 400, 300

def main():
    pg.init()
    
    #Параметры окна на экране:
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    sc.fill(LIGHT_GREEN)
    pg.display.set_caption("Двигающийся текст")
    
    #Параметры отображаемого текста:
    font = pg.font.Font(None, 72)
    text = font.render("Доброе утро!", True, YELLOW)
    
    #Выводим текст:
    place = text.get_rect(center=(200, 300))
    sc.blit(text, place)
    pg.display.update()
    
    #Обновляем экран, наблюдаем двигающийся текст:
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                sys.exit()
        sc.fill(LIGHT_GREEN)
        place.y -= 20
        sc.blit(text, place)
        pg.display.update()
        time.sleep(0.5)
    
if __name__ == "__main__":
    main()


# Задание 2. Измените цвет шрифта по нажатию клавиши

# In[2]:


import pygame as pg
import sys
import time
from random import randint

#Константы:
YELLOW = (255, 255, 0) #желтый   
LIGHT_GREEN = (200, 255, 200) #зеленый 
WIDTH, HEIGHT = 400, 300

#Функция для определения рандомного цвета:
def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def main():
    pg.init()
    
    #Параметры окна на экране:
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    sc.fill(LIGHT_GREEN)
    pg.display.set_caption("Двигающийся текст")
    
    #Параметры отображаемого текста:
    font = pg.font.Font(None, 72)
    text = font.render("Доброе утро!", True, YELLOW)
    
    #Выводим текст:
    place = text.get_rect(center=(200, 300))
    sc.blit(text, place)
    pg.display.update()
    
    #Обновляем экран, наблюдаем двигающийся текст:
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif i.type == pg.KEYDOWN:
                text = font.render("Доброе утро!", True, rand_color()) #меняем цвет текста по нажатию любой клавиши
                
        sc.fill(LIGHT_GREEN)
        place.y -= 20
        sc.blit(text, place)
        pg.display.update()
        time.sleep(1)
    
if __name__ == "__main__":
    main()


# Задание 3. Загрузите картинку и поверните ее на 90 градусов, на 180. Измените фон картинки.

# In[3]:


import pygame as pg
import sys
import time

#Константы:
WIDTH, HEIGHT = 400, 400
LIGHT_GREEN = (200, 255, 200) #зеленый 
WHITE = (255, 255, 255) #белый

def main():
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    sc.fill(LIGHT_GREEN)
    pg.display.set_caption("Смена фона, поворот на 90, 180 градусов")
        
    #загружаем спрайт, с белым "родным" фоном, который будем менять:
    python_surf = pg.image.load('python.png') 
    python_rect = python_surf.get_rect(bottomright=(WIDTH-35, HEIGHT-40))
    sc.blit(python_surf, python_rect)
    pg.display.update()
    time.sleep(2) #смотрим на картинку 2 сек, чтобы убедиться, что фон был белым изначально
    
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                sys.exit()    
                
        sc.fill(LIGHT_GREEN) #залили изначальный спрайт
        pg.display.update()
        
        #загрузили снова спрайт, но поменяли фон на прозрачный:
        python_surf = pg.image.load('python.png') 
        python_surf.set_colorkey(WHITE) #меняем белый фон в картинке python.png на прозрачный с пом.наложения белых пикселей, который заливается фоном окна (LIGHT_GREEN)
        python_rect = python_surf.get_rect(bottomright=(WIDTH-35, HEIGHT-40))
        sc.blit(python_surf, python_rect) #отобразили спрайт 
        pg.display.update()
        time.sleep(2) #смотрим на картинку 2 сек, чтобы убедиться, что фон был поменялся на прозрачный   
        
        sc.fill(LIGHT_GREEN) #залили спрайт с прозрачным фоном
        pg.display.update()
        
        python_surf_rt = pg.transform.rotate(python_surf, 90) #повернули спрайт на 90 градусов
        python_surf_rt.set_colorkey(WHITE) #меняем белый фон в картинке python.png на прозрачный с пом.наложения белых пикселей, который заливается фоном окна (LIGHT_GREEN)
        sc.blit(python_surf_rt, python_rect) #отобразили спрайт  
        pg.display.update()
        time.sleep(2) #смотрим на картинку 2 сек, чтобы убедиться, что спрайт повернулся 
       
        sc.fill(LIGHT_GREEN) #залили спрайт с прозрачным фоном
        pg.display.update()
        
        python_surf_rt_2 = pg.transform.rotate(python_surf_rt, 180) #повернули спрайт на 180 градусов
        python_surf_rt_2.set_colorkey(WHITE) #меняем белый фон в картинке python.png на прозрачный с пом.наложения белых пикселей, который заливается фоном окна (LIGHT_GREEN)
        sc.blit(python_surf_rt_2, python_rect) #отобразили спрайт  
        pg.display.update()
        time.sleep(2) #смотрим на картинку 2 сек, чтобы убедиться, что спрайт повернулся
           
    
if __name__ == "__main__":
    main()


# Задание 4. Творческое задание. Нарисуйте свой рисунок. Добавьте движение и трансформацию

# In[4]:


#здесь загружается последовательно две картинки с бабочками, которые сменяют друг друга через секунду, 
#добавлена возможность перемещения обеих картинок в рамках окна приложения с помощью стрелок клавиатуры ↑, ↓, →, ←.

import pygame as pg
import sys
import time

#Константы:
WIDTH, HEIGHT = 800, 600
LIGHT_BLUE = (135, 206, 250) #бледно-голубой 
WHITE = (255, 255, 255) #белый

def main():
    sc = pg.display.set_mode((WIDTH, HEIGHT))
    sc.fill(LIGHT_BLUE)
    pg.display.set_caption("Бабочки")
    x = 35
    y = 40
    
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    x = x + 60
                elif i.key == pg.K_RIGHT:
                    x = x - 60
                elif i.key == pg.K_UP:
                    y = y + 60
                elif i.key == pg.K_DOWN:
                    y = y - 60
                
        #загружаем спрайт:
        butter_surf = pg.image.load('butter1.jpg') 
        butter_rect = butter_surf.get_rect(bottomright=(WIDTH - x, HEIGHT - y))
        sc.blit(butter_surf, butter_rect)
        pg.display.update()
        time.sleep(1)
    
        sc.fill(LIGHT_BLUE) #залили спрайт фоном
        pg.display.update()
        
        #загрузили снова спрайт:
        butter_surf = pg.image.load('butter2.jpg') 
        butter_rect = butter_surf.get_rect(bottomright=(WIDTH - x, HEIGHT - y))
        sc.blit(butter_surf, butter_rect) #отобразили спрайт 
        pg.display.update()
        time.sleep(1)
        
        sc.fill(LIGHT_BLUE) #залили спрайт фоном
        pg.display.update() 
    
if __name__ == "__main__":
    main()


# In[ ]:




