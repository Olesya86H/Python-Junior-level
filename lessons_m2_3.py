#!/usr/bin/env python
# coding: utf-8

# 1.Создайте классы для представления геометрических фигур в плоскости: круга, прямоугольника и треугольника. Каждый класс должен иметь методы для вычисления площади и периметра.

# In[2]:


class Circle:
    def __init__(self, r): #Метод инициализации
        self.r = r   #радиус

    def __square__(self, r):
        s = r*math.pow(math.pi,2)
        return s
    
    def __perimeter__(self):
        l = 2*r*math.pi
        return l
    
class Rectangle:
    def __init__(self, a, b): #Метод инициализации
        self.a = a #длина
        self.b = b #ширина

    def __square__(self, a, b):
        s = 2*(a+b)
        return s
    
    def __perimeter__(self, a, b):
        p = a*b
        return p

class Triangle:
    def __init__(self, a, b, c, h): #Метод инициализации
        self.a = a  #Первая боковая сторона
        self.b = b  #Вторая боковая сторона
        self.c = c  #Основание
        self.h = h  #Высота

    def __square__(self, c, h):
        s = 2*c*h/2
        return s
    
    def __perimeter__(self, a, b, c):
        p = a+b+c
        return p


# 2. Спроектируйте класс User, представляющий учетную запись пользователя. Класс должен содержать основные данные о пользователе (имя, электронная почта, пароль) и методы для изменения пароля и вывода информации о пользователе.

# In[3]:


class User:
    def __init__(self, name, email, pwd): #Метод инициализации
        self.name = name
        self.email = email
        self.pwd = pwd

    def __chg_pwd__(self):
        new_pwd = str(input("Введите новый пароль: "))
        self.pwd = new_pwd
        return self.pwd
    
    def __output_info__(self, name, email, pwd):
        new_pwd = str(input("Введите новый пароль: "))
        self.pwd = new_pwd
        print("Имя пользователя: {f}".format(f = self.name))
        print("Эл.почта пользователя: {f}".format(f = self.email))
        print("Пароль пользователя: {f}".format(f = self.pwd))


# 3. Разработайте классы для представления книг и библиотеки. Класс Book должен содержать информацию о книге (название, автор, год издания), а класс Library должен управлять коллекцией книг, предоставлять методы для добавления, удаления и поиска книг.

# In[5]:


class Book:
    def __init__(self, name, author, year): #Метод инициализации
        self.name = name
        self.author = author
        self.year = year

class Library:
    def __init__(self, a_book_list): #Метод инициализации
        self.name = name
        self.book_list = a_book_list
    def __add_book__(self, a_book_list, a_book): #добавляем книгу
        lst = a_book_list[0:0]
        for i in range(len(lst)):
            if a_book in lst: 
                continue
            lst.append(a_book)
        return(lst)
    def __del_book__(self, a_book_list, a_book): #удаляем книгу
        lst = a_book_list[0:0]
        for i in range(len(lst)):
            if a_book in lst: 
                lst.remove(a_book)
                continue
        return(lst)
    def __find_book__(self, a_book_list, a_book): #поиск книги
        bk = Book()
        lst = a_book_list[0:0]
        for i in range(len(lst)):
            if a_book in lst: 
                bk = a_book
                continue
            else:
                bk = None
        return(bk)


# 4. Создайте базовый класс Animal, представляющий животное в зоопарке. Этот класс должен содержать основные характеристики животного, такие как имя, возраст и вид. Реализуйте методы для получения информации о животном.

# In[7]:


class Animal:
    def __init__(self, name, age): #Метод инициализации
        self.name = name
        self.age = age
    def __get_name__(self): #получаем информацию об имени
        animal_name = self.name
        return(animal_name)
    def __get_age__(self): #получаем информацию о возрасте
        animal_age = self.age
        return(animal_age)
    def get_kind(self): #получаем информацию о виде
        pass


# На основе класса Animal создайте несколько дочерних классов, представляющих различные виды животных. К примеру, можно создать классы Lion, Elephant, Monkey.
# 
# У каждого дочернего класса должны быть дополнительные атрибуты, специфичные для его вида, и методы, характерные для данного вида. Например, метод roar() для льва, метод trumpet() для слона, и т.д.
# 
# Создайте объекты различных видов животных и продемонстрируйте их функциональность, вызывая методы у каждого экземпляра. Покажите, как базовый класс Animal и его дочерние классы используют наследование для представления различных видов животных.

# In[10]:


class Lion(Animal):
    def __init__(self, mane_length): #Метод инициализации, атрибут - длина гривы
        self.mane_length = mane_length
    def get_kind(self):
        return "Lion"
    def roar(self):
        return "RRR!"
class Elephant(Animal):
    def __init__(self, trunk_length): #Метод инициализации, атрибут - длина хобота
        self.trunk_length = trunk_length
    def get_kind(self):
        return "Elephant"
    def trumpet(self):
        return "UUU!"  
class Monkey(Animal):
    def __init__(self, iq_level): #Метод инициализации, атрибут - уровень интеллекта
        self.iq_level = iq_level
    def get_kind(self):
        return "Monkey"
    def monkey_sounds(self):
        return "UGAGA!"
    
def get_animal_kind(animal):
    return animal.get_kind()

lion = Lion('Leva') #объект лев класса Лев
print(lion.roar()) #уникальный метод для дочернего класса
print(get_animal_kind(lion)) #наследование

elephant = Elephant('Slon') #объект слон класса Слон
print(elephant.trumpet()) #уникальный метод для дочернего класса
print(get_animal_kind(elephant)) #наследование

monkey = Monkey('Obezyana') #объект обезьяна класса Обезьяна
print(monkey.monkey_sounds()) #уникальный метод для дочернего класса
print(get_animal_kind(monkey)) #наследование

