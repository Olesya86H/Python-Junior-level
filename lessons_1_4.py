#!/usr/bin/env python
# coding: utf-8

# Задание 1. Найти сумму всех элементов списка.

# In[1]:


str = input()


# In[4]:


strarray = []
for a in str:
    strarray += a
intarray = [int(item) for item in strarray] 
i = 0
k = 0
while i <= len(intarray) - 1:
    k += intarray[i]
    i += 1
print('Сумма всех элементов списка: {f}'.format(f = k))


# Задание 2. Найти наибольший и наименьший элементы в списке.

# In[5]:


str = input()


# In[6]:


strarray = []
for a in str:
    strarray += a
intarray = [int(item) for item in strarray] 
min_x = intarray[0]
max_x = intarray[0]
i = 1
while i <= len(intarray) - 1:
    if intarray[i] > max_x:
        max_x = intarray[i]
    if intarray[i] < min_x:
        min_x = intarray[i]
    i += 1
print('Минимальный элемент: ', min_x)
print('Максимальный элемент: ', max_x)


# Задание 3. Посчитать количество определенного элемента в списке.

# In[7]:


#вводим последовательность
str = input()


# In[8]:


#вводим элемент для поиска
item = input()


# In[9]:


i = 0
for t in str:
    if t == item:
        i += 1
print('Кол-во элементов в списке, соответствующих заданному ({f1}), равно: {f2}'.format(f1=item, f2=i))


# Задание 4. Удалить все дубликаты из списка.

# In[10]:


#вводим последовательность
str = input()


# In[11]:


i = 0
item = str[i]
i = 1
str2 = item
while i <= len(str) - 1:
    if str[i] != item:
        str2 =


# In[ ]:




