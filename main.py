import requests
import os

def getprovider(number):
    l = number.replace('+', '')
    if str(l)[0] == '8':
        l = l.replace(str(l)[0], '7')
    data = requests.post('https://www.kody.su/check-tel', data={'number': l}).text.splitlines()
    target = data[80]
    
    try:
      region = target.split('Страна')[1].split('<strong>')[1].split('</strong>')[0]
      operator = target.split('<br><strong>')[1].split('</strong>')[0]
      operator = operator.replace(',', '')    
      op = operator.split('[')[0].replace(' ', '')
      city = operator.split('[')[1].split(']')[0]
      l = [region, op, city]
    except:
      l = ['Не найдено', 'Не найдено', 'Не найдено']

    return l

number = input('Введите номер телефона -> ')
provider_info = getprovider(number)

region = provider_info[0]
operator = provider_info[1]
city = provider_info[2]

print(f'Найденная информация о номере {number}: \n Страна: {region}, \n Оператор: {operator}, \n Город: {city}')
os.system('pause')