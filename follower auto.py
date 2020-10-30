from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
file = open('users.txt','r',encoding='utf-8')#WRITE YOUR FILE PATH HERE
names = []
counter = 0
for i in file:
    names.append(i)
for i in range(201):#TODO bad in ke az barname omadi biroon age rafti too edame kar ro anjam bede
    print(counter)
    driver.get('https://www.aparat.com/signin')
    time.sleep(3)
    username = driver.find_element_by_id('username')
    string = names[i]
    username.send_keys(string)
    time.sleep(1)
    username.send_keys(Keys.ENTER)
    time.sleep(3)
    password = driver.find_element_by_xpath('/html/body/div/main/div/section/div/div[1]/form/div/label/input')
    password.send_keys('1520642814Ghh')
    time.sleep(2)
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get('https://www.aparat.com/v/IbcVT')
    time.sleep(3)
    followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
    counter +=1
    if followvalid.text =='دنبال کردن':
        driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
        driver.delete_all_cookies()
    else:
        driver.delete_all_cookies()
