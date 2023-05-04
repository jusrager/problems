# Задача 3 (Области) из урока WEB. Введение в API


import requests


req = "https://geocode-maps.yandex.ru/1.x/?apikey=bfcb052f-4727-43ef-82cb-591c8b61ee66&geocode=Барнаул&format=json"
response = requests.get(req)
res = response.json()
print(res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
      ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]['name'])

req = "https://geocode-maps.yandex.ru/1.x/?apikey=bfcb052f-4727-43ef-82cb-591c8b61ee66&geocode=Мелеуз&format=json"
response = requests.get(req)
res = response.json()
print(res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
      ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]['name'])

req = "https://geocode-maps.yandex.ru/1.x/?apikey=bfcb052f-4727-43ef-82cb-591c8b61ee66&geocode=Йошкар-Ола&format=json"
response = requests.get(req)
res = response.json()
print(res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
      ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]['name'])