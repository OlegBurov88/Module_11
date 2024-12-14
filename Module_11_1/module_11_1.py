import requests

response = requests.get('https://mail.ru')
if response.status_code == 200:
    print('Ответ получен успешно.')
    content = response.content  # обеспечивает доступ к чистым байтам
    response.encoding = 'utf-8'
    text = response.text  # декодирование байтов в строку
    headers = response.headers  # возвращает словарь, что позволяет получить доступ к значению заголовка HTTP по ключу
    print(response.headers)
elif response.status_code == 404:
    print('Запрашиваемый ресурс не был найден.')
else:
    print(f"Произошла ошибка при получении данных. Код статуса: {response.status_code}")

import pandas

if __name__ == '__maim__':
    file = pandas.read_csv('for_pandas.csv')
    print(file.index)  # индексы по строкам
    file.index = ['A', 'B', 'C']  # заменяем значения индекса путём записи списка в атрибут
    print(file)
    print(file.columns)  # индексы по столбцам
    print(file.head(2))  # метод для получения первых n строк дата-сета
    print(file.tail(2))  # метод для последних n строк дата-сета

import numpy as np

array = np.random.randint(0, 100, size=20)  # массив случайных чисел
array = array * 2 - 15
print(array)
print(array.sum())  # сумма чисел в массиве
print(array.min())  # min число в массиве
print(array.max())  # max число в массиве
print(array.mean())  # среднее значение чисел в массиве

import matplotlib.pyplot as plt

day = np.arange(1, 31)
site_views = np.random.randint(1, 200, size=len(day))

plt.plot(day, site_views)
plt.title('Количество просмотров сайта по дням')
plt.xlabel('День')
plt.ylabel('Просмотры')
plt.show()

from PIL import Image
from urllib.request import urlopen

url = "https://i.pinimg.com/originals/15/52/84/1552846e62a8500053170cb31a35adaa.jpg"
with Image.open(urlopen(url)) as img:
    img.show()  # открываем изображение
    image = img.resize((800, 600))  # изменяем размер изображения
    image.show()  # открываем изображение
    image = image.convert('L')  # делаем изображение черно-белым
    image.show()  # открываем изображение
    image.save('foto.jpg')
