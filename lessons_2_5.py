#!/usr/bin/env python
# coding: utf-8

# Задача 1
# У вас есть два множества, представляющие участников двух разных клубов в школе. Вам нужно определить, кто состоит в обоих клубах, кто состоит только в первом клубе, и кто состоит только во втором клубе.
# club_a = {'Alice', 'Bob', 'Charlie', 'David'} 
# club_b = {'Charlie', 'David', 'Edward', 'Fiona'}
# Требования:
# 1.	Создайте два множества:
# o	club_a: Множество участников первого клуба.
# o	club_b: Множество участников второго клуба.
# 2.	Реализуйте функции для выполнения следующих операций:
# o	get_common_members(club_a, club_b): Вернуть множество участников, которые состоят в обоих клубах.
# o	get_only_club_a_members(club_a, club_b): Вернуть множество участников, которые состоят только в первом клубе.
# 

# In[57]:


#1 - создаем мн-ва:
club_a = {'Alice', 'Bob', 'Charlie', 'David'}
club_b = {'Charlie', 'David', 'Edward', 'Fiona'} 


# In[58]:


#2 - вернуть множество участников, которые состоят в обоих клубах:
def get_common_members(club_a, club_b):
    cmn_mbrs_set = []
    for i in club_a:
        for j in club_b:
            if j == i:
                cmn_mbrs_set.append(i)
                break
    return cmn_mbrs_set


# In[59]:


#2 - вернуть множество участников, которые состоят только в первом клубе:
def get_only_club_a_members(club_a, club_b):
    a_mbrs_set = []
    flag_add = False
    for i in club_a:
        for j in club_b:
            if j != i:
                flag_add = True
            else:
                flag_add = False
                break
        if flag_add == True:
            a_mbrs_set.append(i)
        flag_add = False
    return a_mbrs_set


# In[60]:


print("В обоих клубах состоят: {f}".format(f = get_common_members(club_a, club_b)))
print("Только в первом клубе состоят: {f}".format(f = get_only_club_a_members(club_a, club_b)))

#вычисляем, кто состоит только во втором клубе:
cl_b = []
for i in club_b:
    if i not in club_a:
        cl_b.append(i)
        
print("Только во втором клубе состоят: {f}".format(f = cl_b))


# Задача 2
# Создайте класс HogwartsStudent, который будет использоваться для представления ученика Хогвартса. Класс должен включать следующие атрибуты и методы:
# Атрибуты:
# •	name (строка): имя ученика.
# •	house (строка): факультет ученика.
# •	year (целое число): год обучения ученика.
# Методы:
# •	__init__(self, name, house, year): конструктор, который инициализирует имя, факультет и год обучения ученика.
# •	promote(self): метод для перевода ученика на следующий год обучения.
# •	change_house(self, new_house): метод для перевода ученика на другой факультет.
# •	__str__(self): метод для строкового представления объекта ученика, включающего его имя, факультет, год обучения.
# 

# In[61]:


class HogwartsStudent:
    def __init__(self, name, house, year): #Метод инициализации
        self.name = name
        self.house = house
        self.year = year

    def promote(self): #Метод перевода ученика на след.год
        new_year = self.year + 1
        self.year = new_year
        return self.year
    
    def change_house(self, new_house): #Метод перевода ученика на др.факультет
        self.house = new_house
        return self.house
    
    def str(self): #Метод для строкового представления объекта ученика, включающего его имя, факультет, год обучения
        str_obj = "ФИО: " + self.name + ", Факультет: " + self.house + ", Год обучения: " + str(self.year)
        return str_obj


# In[62]:


student = HogwartsStudent("Aisha", "IT", 1) #объект студент
print("Данные ученицы: ")
print(student.str())
print("Ученица переведена на следующий год обучения: {f}".format(f = student.promote()))
print("Ученица переведена на другой факультет: {f}".format(f = student.change_house("Lingua")))
print("----------------------------")
print("Обновленные данные ученицы: ")
print(student.str())

