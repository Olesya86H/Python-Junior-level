#!/usr/bin/env python
# coding: utf-8

# Задание 1. Пользователь вводит название месяца. Напишите программу, которая определяет, к какому сезону года относится этот месяц (весна, лето, осень, зима) и выводит соответствующее сообщение

# In[4]:


ls_month_inp = input()


# In[7]:


if ls_month_inp in ('Декабрь','Январь','Февраль'):
    print('Зима')
elif ls_month_inp in ('Март','Апрель','Май'):
    print('Весна')
elif ls_month_inp in ('Июнь','Июль','Август'):
    print('Лето')
elif ls_month_inp in ('Сентябрь','Октябрь','Ноябрь'):
    print('Осень')
else:
    print('Введён не месяц года!')


# Задание 2. Напишите программу, которая рассчитывает сумму скидки. Если сумма покупки больше 1000 руб, предоставляется скидка 10%, если сумма больше 20000 руб, предоставляется скидка 15%. Выведите итоговую сумму покупки и сумму скидки.

# In[8]:


#вводим цену товара:
lf_price = float(input()) #ожидаем ввод с клавиатуры строки и преобразуем её в вещественное число (пользователь вводит десятичное число)


# In[13]:


# определяем размер скидки, в процентах, в зависимости от введённой на предыдущем шаге цены товара:
if lf_price > 1000 and lf_price <= 20000: #если изначальная цена больше 1000 р, но меньше, либо равна 20000 р, то скидка = 10%
    discount = 10 #процент скидки = 10%
elif lf_price > 20000: #если изначальная цена больше 20000 р, то скидка = 15%
    discount = 15 #процент скидки = 15%
else:
    discount = 0 #если изначальная цена меньше, либо равна 1000 р, то скидки нет совсем, т.е. она = 0%
lf_end_price = lf_price - lf_price*discount/100 #делим на 100, чтобы перевести из процентов в рубли
print('Сумма покупки: ', str(lf_end_price))
print('Сумма скидки:  ', str(lf_price*discount/100))


# Задание 3. Даны три стороны треугольника. Определить каким он является: равносторонним, равнобедренным, разносторонним.

# In[14]:


#вводим с клавиатуры длины всех сторон, преобразуем в десятичный формат:
lf_a = float(input())
lf_b = float(input())
lf_c = float(input())


# In[16]:


if lf_a == lf_b and lf_b == lf_c:
    print('Треугольник равносторонний')
elif (lf_a == lf_b and lf_a != lf_c) or (lf_b == lf_c and lf_b != lf_a) or (lf_a == lf_c and lf_a != lf_b):
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')


# Задание 4.
# 
# Дано натуральное число n (n <=100), определяющее в годах возраст человека. Составить программу, по которой на экран монитора выводится это число с наименованием «год», «года» или «лет».

# In[20]:


li_age = input()


# In[21]:


strarray = [] #объявляем массив, он будет содержать строковые значения


# In[23]:


for a in li_age: #для каждого символа в веденной строке формируем элемент массива
    strarray += a


# In[24]:


intarray = [int(item) for item in strarray] #преобразуем строковый массив strarray в целочисленный массив intarray


# In[25]:


print(intarray) #проверка - вывод на экран содержимого массива с целыми числами


# In[26]:


li_last_digit = intarray[len(intarray) - 1]#берм последнюю цифру - от неё зависит, как будем называть возраст человека: он будет заканчиваться на "год", "лет" или "года"


# In[28]:


if li_last_digit == 1:
    print(str(li_age), 'год')
elif li_last_digit in (2,3,4):
    print(str(li_age), 'года')
elif li_last_digit in (5,6,7,8,9,0):
    print(str(li_age), 'лет')
else:
    print('что-то Вы не то ввели, проверьте себя, пожалуйста')


# In[ ]:



