import requests
import json
from datetime import datetime
from apikey import API_TOKEN, BASE_URL


def vivod(n):

    for i in range(n):
        # for j in range():
        print('Номер заказа ' + data[i].get('gNumber'))
        print('Дата заказа ' + data[i].get('date')[:10])
        print('Артикул продавца ' +
              data[i].get('supplierArticle'))
        print('Тип поступившего заказа ' +
              data[i].get('orderType'))
        print('Номер заказа ' + data[i].get('gNumber'))
        print('Цена до согласованной итоговой скидки/промо/спп. ' +
              str(data[i].get('totalPrice')))               # for key, value in data[i].items():
        total = int(data[i].get('totalPrice'))
        disc = int(data[i].get('discountPercent'))
        priceWithDiscount = total * (1 - disc/100)  # print(key, value)
        print('Цена со скидкой ' +
              str(round(priceWithDiscount, 2)))
        print()


headers = {'Authorization': API_TOKEN,
           'Content-Type': 'application/json; charset=utf-8'}


response = requests.get(BASE_URL, params={
                        'dateFrom': datetime.now().date(), 'flag': '0'}, headers=headers)

data = response.json()
# data = json.loads(response)

# print(data)
vivod(len(data))
print(len(data))

# print('Номер заказа' + data[n].get('gNumber'))
