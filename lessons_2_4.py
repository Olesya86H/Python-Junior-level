#!/usr/bin/env python
# coding: utf-8

# Задание 1. Программа задумывает город. И выводит буквы в случайном порядке. Нужно угадать город.

# In[5]:


import random

def city_guess():
    cities = ["н ь ю - й о р к", "т о к и о", "м о с к в а"]
    computer_city = random.choice(cities) #пограмма выбрала город
    
    list_city_symbols = list(computer_city.split(" ")) #сделали список букв из выбранного программой города
    
    computer_city = computer_city.replace(' ','') #удалили пробелы из выбранного города - чтобы потом сравнить с городом игрока
    
    print("Давайте сыграем в города!")
    print("Я буду выводить буквы загаданного города, пока Вы не угадаете, либо не сдадитесь!")
    
    k = 0 #счетчик
    
    list_city_symbols_rmv = list_city_symbols #список, из которого будем удалять буквы во избежании повторов их вывода на экран
    
    for i in range(len(list_city_symbols)):
        a = random.choice(list_city_symbols_rmv)
        list_city_symbols_rmv.remove(a)
        print(a)
        player_city = input("Какой, Вы думаете, это город?: ").strip().lower()
        if player_city == computer_city:
            print("Правильно!")
            print("Вы выиграли! Игра завершена.")
            break
        else:
            print("Неправильно.")
            k += 1
        if k == len(list_city_symbols):
            print("Вы проиграли. Игра завершена.")
            print(f"Программа выбрала: {computer_city}")
            break

city_guess()


# Задание 2. Программа на поле размещает 5 двухместных кораблей. Нужно найти координаты этих кораблей.

# In[65]:


from random import randint
        
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 45)

def get_ships():
    comp_x_y = [] 
    n = 10
    for i in range(5): 
        x = randint(0, 9)
        y1 = randint(0, 9)
        y2 = y1 + 1 #все корабли разместим по горизонтали
        
        #первая пара координат двухпалубника:
        s = str(x) + ' ' + str(y1)
        row = s.split() 
        for i in range(len(row)): 
            row[i] = int(row[i]) 
        comp_x_y.append(row) #Каждая строка является массивом из 2x элементов (x,y)
        
        #вторая пара координат двухпалубника:
        s = str(x) + ' ' + str(y2)
        row = s.split() 
        for i in range(len(row)): 
            row[i] = int(row[i]) 
        comp_x_y.append(row) #Каждая строка является массивом из 2x элементов (x,y)

    return comp_x_y

def main():
    board = [[' ' for _ in range(11)] for _ in range(11)] #нарисовали доску
    comp_x_y = get_ships()#нарисовали корабли
    cnt = 0 #счетчик верных ударов, значение в клетке = Х
    print(comp_x_y)
    while True:
        print_board(board)
        print("Ваш ход!")

        try:
            row = int(input("Введите номер строки (0 - 9): "))
            col = int(input("Введите номер столбца (0 - 9): "))
            
            s = "."
            for i in range(10):
                if (comp_x_y[i][0] == row) and (comp_x_y[i][1] == col):
                    s = "X"
                    cnt += 1
                    break
            
            board[row][col] = s #поставили отметку на поле боя
            
            if (cnt == 10):
                print('Все корабли найдены! Игра окончена.')
                break
            
        except (ValueError, IndexError):
            print("Некорректный ввод! Пожалуйста, введите числа от 0 до 9.")


if __name__ == "__main__":
    main()

