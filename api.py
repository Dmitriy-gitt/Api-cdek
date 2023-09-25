import requests
import map

#получаем токен
url = requests.post('https://api.edu.cdek.ru/v2/oauth/token?parameters', data={'grant_type':'client_credentials',
                                                                               'client_id':'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
                                                                               'client_secret':'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'})
data = url.json()
token = data['access_token']

#Авторизация по токену и получаем код города по базе сдека и отправляем данные для карты
name_city = ['Миасс', 'Златоуст', 'Челябинск', 'Москва']
for i in name_city:
    get_city = requests.get(f'https://api.edu.cdek.ru/v2/location/cities?city={i}', headers={'Authorization': 'Bearer ' + token}).json()
    code = get_city[0]['code']
    get_adres = requests.get(f'https://api.edu.cdek.ru/v2/deliverypoints?city_code={code}', headers={'Authorization': 'Bearer ' + token}).json()
    for i in get_adres:
        s_1 = i['location']['address_full']
        long, lat = i['location']['longitude'], i['location']['latitude']
        map.search(lat, long, name_city, s_1)


#Получаем список ПВЗ
#get_adres = requests.get(f'https://api.edu.cdek.ru/v2/deliverypoints?city_code={code}', headers={'Authorization': 'Bearer ' + token}).json()
#long, lat = get_adres[0]['location']['longitude'], get_adres[0]['location']['latitude']
