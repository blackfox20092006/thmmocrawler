from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
from time import sleep


proxy_address = '103.82.36.127:10671'

options = webdriver.ChromeOptions()

options.add_argument('--proxy-server=http://' + proxy_address)

driver = webdriver.Chrome(options=options)

driver.get("https://www.whatismyip.com")

sleep(1000000000000000000000)

driver.quit()