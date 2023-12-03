import threading

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
from bs4 import BeautifulSoup
import os
import re
from time import sleep
import sys
def data_dividing(a, m):
    data = []
    temp = []
    try:
        n = len(a) // m
        for i in range(m):
            data.append([])
        for i in range(m):
            data[i] = a[:n+1]
            del a[:n+1]
    except:
        temp = a
    if a != []:
        temp = a
    return data, temp
def crawl_shop_list(shop_list):
    global user_rating
    driver = webdriver.Chrome(options=chrome_options)
    for i in shop_list:
        driver.get(gian_hang_url.format(i))
        e = driver.find_elements(By.CLASS_NAME, 'review__author')
        for i in e:
            a_tag = i.find_element(By.TAG_NAME, 'a')
            href = a_tag.get_attribute('href')
            href = href.replace('https://taphoammo.net/thong-tin/', '')
            user_rating += href
            print(href)
f = open('userlist.txt', 'w')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-default-apps')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
search_url = 'https://taphoammo.net/danh-muc/none?q=&t=&keywork=&page={}'
gian_hang_url = 'https://taphoammo.net/gian-hang/{}'
user_link = 'https://taphoammo.net/thong-tin/{}'
ten_nguoi_ban = []
user_rating = []
link_shop = []
user_link_list = []
temp = []
i = 1
while True:
    driver.get(search_url.format(i))
    print(search_url.format(i))
    i += 1
    WebDriverWait(driver, timeout=0.1)
    html = driver.page_source
    hrefs = re.findall(r'href="/thong-tin/([^"]+)"', html)
    hrefs2 = re.findall(r'href="/gian-hang/([^"]+)"', html)
    if hrefs == []:
        break
    ten_nguoi_ban.extend(hrefs)
    for j in hrefs:
        print(j)
    link_shop.extend(hrefs2)
driver.quit()
f.writelines(list((i+'\n') for i in list(set(ten_nguoi_ban))))
f.close()
threads_num = int(input('Threads : '))
data, temp = data_dividing(link_shop, threads_num)
threads = []
for i in range(threads_num):
    threads.append(threading.Thread(target=crawl_shop_list, args=(data[i],)))
for i in threads:
    i.start()
for i in threads:
    i.join()
a = open('userlist.txt', 'a')
a.writelines(list((i+'\n') for i in list(set(user_rating))))
a.close()