from email import header
from bs4 import BeautifulSoup
import requests
import re
import time
import os
from fake_useragent import UserAgent
import datetime

randomAgent = UserAgent() 
btcPriceLink = 'https://crypto.com/price/ru/bitcoin' # Ссылка на сайт с биткоин прайсом

def parse():
    while True:

        nowtime = datetime.datetime.now() # подключение текущего системного времени
        nowtime_str = nowtime.strftime("%H:%M:%S") # установка формата для времени часы:минуты:секунды
        os.system('cls') # очистка консоли

        headers = { # подключение юзерагента
            'User-Agent': randomAgent.random
        }

        try:
            responceBtcPrice = requests.get(btcPriceLink, headers = headers).text # получение запроса от сайта с ценой btc с использованием фейкового юзеаргента
            soupForBtcPriceLink = BeautifulSoup(responceBtcPrice, 'lxml') # подключение бс4 для парса цены битка
            btcblock = soupForBtcPriceLink.find('div', class_='chakra-stack coin-chart css-5we3l5') # поиск блока с ценой битка
            btcprice = btcblock.find('h2', class_='chakra-heading css-64zram').text # Текущая цена биткоина по сайту
            btcpricetext = re.findall('\d+',btcprice)
            btcpricetext = f'$'+btcpricetext[0]+btcpricetext[1]
        except:
            btcpricetext = 'Не удалось получить цену биткоина...'

        print(f'Текущее время: {nowtime_str}\nТекущая цена биткоина: {btcpricetext}')
        time.sleep(5)

if __name__ == '__main__':
    parse()