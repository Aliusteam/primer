from bs4 import BeautifulSoup
import requests
import csv
import os
import time  # для задержки

# URL = 'https://auto.ria.com/newauto/marka-jeep/'
URL = 'https://auto.ria.com/newauto/marka-opel/'
# URL = 'https://auto.ria.com/newauto/marka-kia/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


# Функция для перехода на страничку
def get_html(url, params=None):  # params - для перехода по страницам
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    # получение обьекта, с которым мы работаем
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')  # .find('a')
    if pagination:
        return int(pagination[-1].get_text())  # get_text
    else:
        return 1


# Тут обработка переданной странички html при помощи BeautifulSoup
def get_content(html):
    # тут мы создаем обьекты пайтон
    soup = BeautifulSoup(html, 'html.parser')

    # получаем коллекцию элементов 'div'  # 'a'
    # то есть берем основной класс proposition
    #    items = soup.find_all('a', class_='proposition_link')  # proposition_link
    items = soup.find_all('div', class_='proposition')  # proposition_link
    cars = []

    # теперь берем с основного класса items те элементы,
    # которые нам нужны, через цикл
    # item будее равен soup.find('div', class_='proposition')
    for item in items:
        uah_price = item.find('span', class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цену уточняйте'
        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'usd_price': item.find('span', class_='green').text.strip(),
            'uah_price': uah_price,
            'city': item.find('div', class_='proposition_region').find('strong').text.strip()
        })
        time.sleep(0.2)  # задержка в секундах
    #    print(cars)
    return cars


# csv
def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена в $', 'Цена в UAH', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['uah_price'], item['city']])


# тут получение страницы html
def parse():
    # Это для ручного ввода
    #    URL = input('Введите URL, например: https://auto.ria.com/newauto/marka-opel/?page=1: ')
    #    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        # поиск кол-ва страничек этого авто
        pages_count = get_pages_count(html.text)
        # проходим циклом по страничкам
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            # получаем конткнт каждой стринички, в параметры добавляем page
            # https://auto.ria.com/newauto/marka-opel/?page=1&markaId=56&show_in_search=1
            # https://auto.ria.com/newauto/marka-opel/?page=9&markaId=56&show_in_search=1
            #            html = get_html(URL, params = {'page':page})
            try:
                html = get_html(URL, params={'page': page})
            except:
                print(f'Ошибка на страничке {page}')
                continue
            # тепеь парсим каждую стриничку:
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        print(cars)
        print(f'Получено {len(cars)} автомобилей')
        # Для авто открытия файла
        os.startfile(FILE)

    #        print(pages_count)
    #        cars = get_content(html.text)
    #        print(cars)
    else:
        print('Error')


parse()

# 1. 1ая функция парсинга parse().
# c нее мы перенаправляем в функциию, где мы представляемся сайту:
# 'user-agent', 'accept' и возвращаем html код

# 2. Во 2ой функции get_html, мы проверям html код == 200,
# если ок, передаем его в функцию get_content

# 3. В функции get_content мы делаем из html - конструктор
# с помощью BeautifulSoup
# И собираем все нужные нам данные
