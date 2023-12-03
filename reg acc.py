from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
from time import sleep
import threading
import string
signup = 'https://taphoammo.net/login.html'
generate_random_string = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(15, 25)))
def register():
    global success_count
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
    proxy = f'103.82.36.127:{random.randint(10001, 12000)}'
    chrome_options.add_argument('--proxy-server=http://' + proxy)
    try:
        driver = webdriver.Chrome(options=chrome_options)
        email = generate_random_string() + '@gmail.com'
        username = generate_random_string()
        password = generate_random_string()
        driver.get(signup)
        WebDriverWait(driver, timeout=0.5)
        e = driver.find_element(By.ID, 'user.username')
        e.send_keys(username)
        e = driver.find_element(By.ID, 'signup_email')
        e.send_keys(email)
        e = driver.find_element(By.ID, 'user.password')
        e.send_keys(password)
        e = driver.find_element(By.ID, 'confirmPassword')
        e.send_keys(password)
        e = driver.find_element(By.XPATH, '//*[@id="formSignup"]/button')
        e.click()
        sleep(2)
        driver.get(signup)
        e = driver.find_element(By.XPATH, '//*[@id="login_email"]')
        e.send_keys(email)
        e = driver.find_element(By.XPATH, '//*[@id="login_password"]')
        e.send_keys(password)
        e = driver.find_element(By.XPATH, '//*[@id="loginButton"]')
        e.click()
        WebDriverWait(driver, timeout=0.5)
        driver.get('https://taphoammo.net/profile.html')
        sleep(3)
        try:
            e = driver.find_element(By.XPATH, '//*[@id="loginButton"]')
            print(f'\033[31mFAIL => {email}|{password}\033[0m')
        except:
            print(f'\033[32mSUCCESS => {email}|{password}\033[0m')
            f.write(f'{email}|{password}\n')
            success_count += 1
    except:
        print(f'\033[31mFAIL => {email}|{password}\033[0m')
threads_num = int(input('Threads : '))
nums = int(input('Number of account : '))
success_count = 0
while success_count <= nums:
    f = open('acc_reg.txt', 'a')
    threads = []
    for i in range(threads_num):
        threads.append(threading.Thread(target=register))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    f.close()
print('\035[32mFinished!!!!!\033[0m')