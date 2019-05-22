from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import json
from pyvirtualdisplay import Display

#-*- coding:utf-8 -*-

#normal way
#login
def twitch_way (driver):
    driver.get('https://twip.kr')

    driver.find_element_by_xpath('//*[@id="streamer-login-area"]/a').click()
    driver.implicitly_wait(delay)

    driver.find_element_by_name('username').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button/span').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > div.row.border-bottom > nav > ul > li:nth-child(3) > a"))
    )

    return driver

#facebook way
#first facebook login
def facebook_way (driver):
    driver.get('https://www.facebook.com/login')
    driver.find_element_by_name('email').send_keys(user_id)
    driver.find_element_by_name('pass').send_keys(user_password)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    driver.implicitly_wait(delay)
    print('login - 1')
    #second twitch login
    driver.get('https://www.twitch.tv/login')
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div[2]/button').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div > div > nav > div > div > div > a:nth-child(3)"))
    )
    print('login - 2')
    #login to twip
    driver.get('https://twip.kr/')
    driver.find_element_by_xpath('//*[@id="streamer-login-area"]/a').click()
    driver.implicitly_wait(delay)
    print('login finished')

    return driver


delay = 1
#1 : twitch login , #2 : facebook login can get parameter
login_way = 2

display = Display(visible=0, size=(800, 800))  
display.start()

user_id = 'id'
user_password = 'password'

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

if login_way ==1:
    driver = twitch_way(driver)
elif login_way == 2:
    driver = facebook_way(driver)

result = []
updated = []
set_result = []

driver.get('https://twip.kr/dashboard/donate')
driver.implicitly_wait(delay)
streamerID = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[1]/p/a').text
streamerID = streamerID[15:]

#thead = driver.find_elements_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div/div/div[2]/div[2]/table/thead/tr')
#for tr in thead:
#    print(tr.text)

while True:
    #login to twip
    driver.get('https://twip.kr/dashboard/donate')
    driver.implicitly_wait(delay)

    result = []

    tbody = driver.find_elements_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr')
    for tr in tbody:
        temp = tr.text.split(' ')
        dict1 = {"donatorID": temp[2], "streamerID": streamerID, "content": " ".join(temp[4:]), "date": " ".join(temp[0:2])}
        result.append(dict1)
        #print(tr.text)

    if len(result) >0:
        if len(set_result) > 0:
            updated = result[0:(result.index(set_result[0]))]
        else :
            updated = result
        if len(updated) >0 :  
            print(updated)
            resultJson = json.dumps(updated, ensure_ascii=False)
            print(resultJson)

            set_result = result
        else: resultJson = json.dumps(updated, ensure_ascii=False)
        f = open('missionResult.json', 'w+t', encoding = 'utf-8')
        f.write(resultJson)
        f.close()
    sleep(5)
    #print("tiktok")