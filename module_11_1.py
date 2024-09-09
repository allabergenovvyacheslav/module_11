import requests


# requests - запросить данные с сайта и вывести их в консоль.
query = {'q': 'wood floor'}
# создадим переменную, которая будет содержать необходимые параметры
# (q — передаём ключевые слова для поиска)
res = requests.get('https://ru.pinterest.com/search/pins', params=query)
# метод get, в ответе мы получим ссылку с нужными параметрами запроса
print(res.ok)
print(res.url)



