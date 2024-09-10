import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---------------------------------requests---------------------------------------------')
# requests - запросить данные с сайта и вывести их в консоль.
query = {'q': 'wood floor'}
# создадим переменную, которая будет содержать необходимые параметры
# (q — передаём ключевые слова для поиска)
res = requests.get('https://ru.pinterest.com/search/pins', params=query)
# метод get, в ответе мы получим ссылку с нужными параметрами запроса
print(res.ok)
print(res.url)

print('-----------------------------------pandas-------------------------------------------')

# Series
my_series = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])

print(my_series)

my_series[['a', 'c']] = 999

print(my_series)
print('------------------------------------------------------------------------------')

# DataFrame
my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(my_dict)
print(df)

f_row = df.iloc[0]  # индексация строки
print(f_row)

print('------------------------------------------------------------------------------')

# Чтение данных из Excel файла
xlsx = pd.ExcelFile('Календарь учебного года1.xlsx')
data = pd.read_excel(xlsx, 'Календарь')
print(data)

print('-------------------------------numpy-----------------------------------------------')

# Создание массивов numpy
data = np.array([1, 2, 3, 4])
vector = np.ones(4)
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
print(vector)
print(matrix)

# операции с массивами, такие как сложение, среднее арифметическое,
# умножение, транспонирование матрицы:

res1 = vector + data
res2 = data.sum()
res3 = data.mean()
res4 = matrix.prod()
res5 = matrix.T

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)

print('-------------------------------matplotlib----------------------------------------')

# Линейный график
plt.axis([0, 10, 0, 40])
plt.title('My plot')
plt.xlabel('Подсчет')
plt.ylabel('Квадрат')
plt.text(1, 30, r'$y = x^2$', fontsize=15, bbox={'facecolor': 'yellow', 'alpha': 0.3})
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1, 4.5, 'First', color='green')
plt.text(3.5, 12.75, 'Second', color='green')
plt.text(5, 25.5, 'Third', color='green')
plt.text(6, 36.5, 'Fourth', color='green')
plt.grid(True)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot([1, 3.5, 5, 6], [4, 12.25, 25, 36], 'g^')
plt.legend(['First series', 'Second series'], loc=2)
plt.savefig('my_plot.png')
plt.show()

# Столбчатый график
plt.bar(['A', 'B', 'C', 'D'], [1, 2, 3, 4])
# plt.show()

# Круговая диаграмма
plt.pie([1, 2, 3, 4], labels=['A', 'B', 'C', 'D'])
# plt.show() 
