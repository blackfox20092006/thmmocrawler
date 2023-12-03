import requests
import random
import threading
tokens = []
api = 'https://taphoammo.net/api/buyProducts?kioskToken=BWKVGGQETFJ4GWIIGOQ3&userToken={}&quantity={}&promotion={}'
def buy(token, amount, promotion):
    global count
    api_ = api.format(token, amount, promotion)
    proxy = {
        'http': f'http://103.82.36.127:{random.randint(10001, 12000)}'
    }
    a = requests.get(api_, proxies=proxy)
    if (a.json())['success'] == 'true':
        count += 1
        print(f'\x1b[32m[{count}] {a.text}')
    else:
        print(f'\x1b[31m {a.text()}')
with open('list_token.txt', 'r') as f:
    tokens = [i.replace('\n', '') for i in f.readlines()]
threads_num = len(tokens)
count = 0
_time_ = int(input('Số lần chạy : '))
while count <= _time_:
    for i in tokens:
        threads = []
        threads.append(threading.Thread(target=buy, args=(i.split('|')[0], i.split('|')[1], i.split('|')[2],)))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
