#!/usr/bin/env python
# coding: utf-8

# 1 задание

# In[1]:


phrase_1 = input("Введите фразу 1: ")
phrase_2 = input("Введите фразу 2: ")
if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_1) < len(phrase_2):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы одной длины")


# 2 задание

# In[2]:


year = int(input("Введите год: "))
if len(str(year)) != 4:
    print("Неверный формат")
elif year % 4 == 0:
    print("Високосный год")
else:
    print("Обычный год")


# 3 задание

# In[19]:


day_of_birth = int(input("Введите день: "))
month_of_birth = input("Введите месяц в именительном падеже: ")
if (month_of_birth == 'Март' and 21 <= day_of_birth <= 31) or (month_of_birth == 'Апрель' and 1 <= day_of_birth <= 20):
    print("Ваш знак зодиака: Овен")
elif (month_of_birth == 'Апрель' and 21 <= day_of_birth <= 30) or (month_of_birth == 'Май' and 1 <= day_of_birth <= 21):
    print("Ваш знак зодиака: Телец")
elif (month_of_birth == 'Май' and 22 <= day_of_birth <= 31) or (month_of_birth == 'Июнь' and 1 <= day_of_birth <= 21):
    print("Ваш знак зодиака: Близнецы")
elif (month_of_birth == 'Июнь' and 22 <= day_of_birth <= 30) or (month_of_birth == 'Июль' and 1 <= day_of_birth <= 22):
    print("Ваш знак зодиака: Рак")
elif (month_of_birth == 'Июль' and 23 <= day_of_birth <= 31) or (month_of_birth == 'Август' and 1 <= day_of_birth <= 21):
    print("Ваш знак зодиака: Лев")
elif (month_of_birth == 'Август' and 22 <= day_of_birth <= 31) or (month_of_birth == 'Сентябрь' and 1 <= day_of_birth <= 23):
    print("Ваш знак зодиака: Дева")
elif (month_of_birth == 'Сентябрь' and 24 <= day_of_birth <= 30) or (month_of_birth == 'Октябрь' and 1 <= day_of_birth <= 23):
    print("Ваш знак зодиака: Весы")
elif (month_of_birth == 'Октябрь' and 24 <= day_of_birth <= 31) or (month_of_birth == 'Ноябрь' and 1 <= day_of_birth <= 22):
    print("Ваш знак зодиака: Скорпион")
elif (month_of_birth == 'Ноябрь' and 23 <= day_of_birth <= 30) or (month_of_birth == 'Декабрь' and 1 <= day_of_birth <= 22):
    print("Ваш знак зодиака: Стрелец")
elif (month_of_birth == 'Декабрь' and 23 <= day_of_birth <= 31) or (month_of_birth == 'Январь' and 1 <= day_of_birth <= 20):
    print("Ваш знак зодиака: Козерог")
elif (month_of_birth == 'Январь' and 21 <= day_of_birth <= 31) or (month_of_birth == 'Февраль' and 1 <= day_of_birth <= 19):
    print("Ваш знак зодиака: Водолей")
elif (month_of_birth == 'Февраль' and 20 <= day_of_birth <= 29) or (month_of_birth == 'Март' and 1 <= day_of_birth <= 20):
    print("Ваш знак зодиака: Рыбы")
else:
    print("Кажется, вы родились без знака зодиака. Не переживайте, с кем не бывает!")


# 4 задание

# In[6]:


width = int(input("Введите ширину в см: "))
length = int(input("Введите длину в см: "))
height = int(input("Введите высоту в см: "))
if width < 15 and length < 15 and height < 15:
    print("Коробка №1")
elif length > 200:
    print("Упаковка для лыж")
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print("Коробка №2")
else:
    print("Стандартная коробка №3")


# 5 задание

# In[7]:


number = str(input("Введите номер билета: "))
sum1 = int(number[0]) + int(number[1]) + int(number[2])
sum2 = int(number[3]) + int(number[4]) + int(number[5])
if sum1 == sum2:
    print('Счастливый билет')
else:
    print('Несчастливый билет')


# 6 задание

# In[18]:


type = input("Ведите тип фигуры: ")
if type == 'Круг':
    radius = int(input("Ведите радиус круга: "))
    square_circle = 3.14 * (radius ** 2)
    print('Площадь круга: ', square_circle)
elif type == 'Треугольник':
    side_A = int(input("Ведите длину стороны A: "))
    side_B = int(input("Ведите длину стороны B: "))
    side_C = int(input("Ведите длину стороны C: "))
    p = (side_A + side_B + side_C) / 2
    square_triangle = (p * (p - side_A) * (p - side_B) * (p - side_C)) ** 0.5
    print('Площадь треугольника: ', square_triangle)
elif type == 'Прямоугольник':
    side_A = int(input("Ведите длину стороны A: "))
    side_B = int(input("Ведите длину стороны B: "))
    square_rectangle = side_A * side_B
    print('Площадь прямоугольника: ', square_rectangle)
else:
    print("Упс! Я не знаю такие фигуры.")

