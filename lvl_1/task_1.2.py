# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Моё решение
import random
first = my_favorite_songs[(random.randint(0, 8))][1]
second = my_favorite_songs[(random.randint(0, 8))][1]
last_one = my_favorite_songs[(random.randint(0, 8))][1]
print(f'Три песни звучат {first + second + last_one} минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Моё решение
import datetime
first = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(random.randint(0, 8))]]
second = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(random.randint(0, 8))]]
last_one = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(random.randint(0, 8))]]
sum = first + second + last_one
print(f'Три песни звучат {sum} минут')
answer = sum * 60
# Решение D:
second_answer = str(datetime.timedelta(seconds = answer))
print(f'Три песни звучат {second_answer}')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

