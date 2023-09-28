import requests
import map

#получаем токен для активации тестового доступа, как указано в документации
#https://api-docs.cdek.ru/29923918.html
url = requests.post('https://api.edu.cdek.ru/v2/oauth/token?parameters', data={'grant_type':'client_credentials',
                                                                               'client_id':'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
                                                                               'client_secret':'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'})
#достаем токен из словаря data, для дальнейшего подключения к сервисам
data = url.json()
token = data['access_token']

#Авторизация по токену и получаем код города по базе сдека и отправляем данные для карты
name_city = ['Миасс', 'Златоуст', 'Челябинск', 'Москва']
for i in name_city:
    #делаем запрос к списку населенных пунктов,что бы достать код города, как указано в документации
    #https://api-docs.cdek.ru/33829437.html
    get_city = requests.get(f'https://api.edu.cdek.ru/v2/location/cities?city={i}', headers={'Authorization': 'Bearer ' + token}).json()
    #достаем код города
    code = get_city[0]['code']
    #делаем запрос к списку офисов(он же список ПВЗ), как указано в документации
    #https://api-docs.cdek.ru/36982648.html
    get_adres = requests.get(f'https://api.edu.cdek.ru/v2/deliverypoints?city_code={code}', headers={'Authorization': 'Bearer ' + token}).json()
    for i in get_adres:
        s_1 = i['location']['address_full'] #достаем адрес ПВЗ
        long, lat = i['location']['longitude'], i['location']['latitude'] #достаем долготу и ширину, что бы передать на карту
        map.search(lat, long, name_city, s_1) #вызов функции из файла map, которая отправляет данные на карту


#Это можно не читать, моя пометка
#get_adres = requests.get(f'https://api.edu.cdek.ru/v2/deliverypoints?city_code={code}', headers={'Authorization': 'Bearer ' + token}).json()
#long, lat = get_adres[0]['location']['longitude'], get_adres[0]['location']['latitude']
