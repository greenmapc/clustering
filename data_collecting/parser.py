import requests

from csv_generator import write_to_csv

PAGE_SIZE = 99
CATEGORY = "cars"
URL = 'https://auto.ru/-/ajax/desktop/listing/'

# TODO: update headers
HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Length': '137',
    'content-type': 'application/json',
    'Cookie': '_csrf_token=1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24; autoru_sid=a%3Ag5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270%7C1580931467355.604800.8HnYnADZ6dSuzP1gctE0Fw.cd59AHgDSjoJxSYHCHfDUoj-f2orbR5pKj6U0ddu1G4; autoruuid=g5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270; suid=48a075680eac323f3f9ad5304157467a.bc50c5bde34519f174ccdba0bd791787; from_lifetime=1580933172327; from=yandex; X-Vertis-DC=myt; crookie=bp+bI7U7P7sm6q0mpUwAgWZrbzx3jePMKp8OPHqMwu9FdPseXCTs3bUqyAjp1fRRTDJ9Z5RZEdQLKToDLIpc7dWxb90=; cmtchd=MTU4MDkzMTQ3MjU0NQ==; yandexuid=1758388111580931457; bltsr=1; navigation_promo_seen-recalls=true',
    'Host': 'auto.ru',
    'origin': 'https://auto.ru',
    'Referer': 'https://auto.ru/ryazan/cars/mercedes/all/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'x-client-app-version': '202002.03.092255',
    'x-client-date': '1580933207763',
    'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
    'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
    'x-requested-with': 'fetch'
}


def parse():
    result = []
    for page in range(1, PAGE_SIZE + 1):

        PARAMS = {
            # 'catalog_filter' : [{"mark": "MERCEDES"}],
            'section': "all",
            'category': CATEGORY,
            'sort': "fresh_relevance_1-desc",
            'page': page
        }

        response = requests.post(URL, json=PARAMS, headers=HEADERS)
        data = response.json()['offers']

        for i in range(len(data)):
            result.append(mapping_data(data[i]))
        print('Page: ' + str(page))
    write_to_csv(result)
    print('Successfully')


def mapping_data(page_data):
    return {
        'color': get_color(page_data),
        'owners_count': get_owners_count(page_data),
        'year': get_year(page_data),
        'price': get_price(page_data),
        'region': get_region(page_data),
        'mileage': get_mileage(page_data),
        'doors_count': get_doors_count(page_data),
        'class_auto': get_class_auto(page_data),
        'body_type': get_body_type(page_data),
        'brand': get_brand(page_data),
        'model': get_model(page_data),
    }


# Цвет автомобиля (возвращается в формате hex)
def get_color(page_data):
    try:
        return str(page_data[page_data]['color_hex'])
    except:
        return None


# Колличество владельцев автомобиля
def get_owners_count(page_data):
    try:
        return str(page_data['documents']['owners_number'])
    except:
        return None


# Год выпуска автомобиля
def get_year(page_data):
    try:
        return str(page_data['documents']['year'])
    except:
        return None


# Цена в рублях, евро и долларах
def get_price(page_data):
    try:
        return str(page_data['price_info']['RUR'])
    except:
        return None


# Регион, в котором находится автомобиль
def get_region(page_data):
    try:
        return str(page_data['seller']['location']['region_info']['name'])
    except:
        return None


# Пробег автомобиля
def get_mileage(page_data):
    try:
        return str(page_data['state']['mileage'])
    except:
        return None


# Количество дверей у автомобиля
def get_doors_count(page_data):
    try:
        return str(page_data['vehicle_info']['configuration']['doors_count'])
    except:
        return None


# Класс автомобиля
def get_class_auto(page_data):
    try:
        return str(page_data['vehicle_info']['configuration']['auto_class'])
    except:
        return None


# Название автомобиля
def get_body_type(page_data):
    try:
        return str(page_data['vehicle_info']['configuration']['human_name'])
    except:
        return None


# Марка автомобиля
def get_brand(page_data):
    try:
        return str(page_data['vehicle_info']['mark_info']['name'])
    except:
        return None


# Модель автомобиля
def get_model(page_data):
    try:
        return str(page_data['vehicle_info']['model_info']['name'])
    except:
        return None


parse()
