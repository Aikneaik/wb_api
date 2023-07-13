import requests
import json
from datetime import datetime
from apikey import API_TOKEN, BASE_URL


def vivod(n):

    for i in range(n):
        # for j in range():
        print('Номер заказа: ' + data[i].get('gNumber'))
        print('Дата заказа: ' + data[i].get('date')[:10])
        print('Артикул продавца: ' +
              data[i].get('supplierArticle'))
        print('Название склада отгрузки: ' +
              data[i].get('warehouseName'))
        print('Регион: ' +
              data[i].get('regionName'))               # for key, value in data[i].items():
        print('Предмет: ' +
              data[i].get('subject'))
        print('Бренд: ' +
              data[i].get('brand'))
        print('К перечислению продавцу: ',
              data[i].get('forPay'))
        print('____________________________________')


headers = {'Authorization': API_TOKEN,
           'Content-Type': 'application/json; charset=utf-8'}


response = requests.get('https://statistics-api.wildberries.ru/api/v1/supplier/sales', params={
                        'dateFrom': datetime.now().date(), 'flag': '0'}, headers=headers)  # datetime.now().date()

data = response.json()
# data = json.loads(response)

# print(data)
vivod(len(data))
print(len(data))

# print('Номер заказа' + data[n].get('gNumber'))
