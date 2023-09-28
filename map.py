import folium
from folium.plugins import Geocoder

#Создаем карту
map = folium.Map(location=['55.047874', '60.112206'], zoom_start=8)


#Добавляем маркеры с ПВЗ на карту
def search(lat, long, name_city, s_1):
    #Передается долгота, ширина, город, адрес
    folium.Marker([lat, long], popup=f'{name_city}', tooltip=s_1).add_to(map)
    map.save('mapcdek.html')

Geocoder().add_to(map)
map.save('mapcdek.html')

