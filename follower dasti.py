from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
def loop(start1,end1,password,user):
    for i in range(start1,end1):
        driver.get('https://www.aparat.com/signin')
        time.sleep(3)
        username = driver.find_element_by_id('username')
        username.send_keys(user+str(i))
        time.sleep(1)
        username.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_id('password').send_keys(password+Keys.ENTER)
        time.sleep(5)
        driver.get('https://www.aparat.com/v/0UELA')
        time.sleep(3)
        followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
        if followvalid.text =='دنبال کردن':
            # time.sleep(5)
            # driver.get('https://www.aparat.com/v/IbcVT')
            driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
            driver.delete_all_cookies()
        else:
            driver.delete_all_cookies()
loop(0,120,'WRITE YOUR PASSWORD HERE',"WRITE YOUR USERNAME HERE")
# for i in range(120,144):
#     driver.get('https://www.aparat.com/signin')
#     time.sleep(3)
#     username = driver.find_element_by_id('username')
#     username.send_keys('ghaemnayeb'+str(i))
#     time.sleep(1)
#     username.send_keys(Keys.ENTER)
#     time.sleep(7)
#     driver.find_element_by_id('password').send_keys('1520642814ghh'+Keys.ENTER)
#     time.sleep(5)
#     driver.get('https://www.aparat.com/v/0UELA')
#     time.sleep(3)
#     followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
#     if followvalid.text =='دنبال کردن':
#         # time.sleep(5)
#         # driver.get('https://www.aparat.com/v/IbcVT')
#         driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
#         driver.delete_all_cookies()
#     else:
#         driver.delete_all_cookies()
# for i in range(250,261):
#     driver.get('https://www.aparat.com/signin')
#     time.sleep(3)
#     username = driver.find_element_by_id('username')
#     username.send_keys('ghaemnayeb'+str(i))
#     time.sleep(1)
#     username.send_keys(Keys.ENTER)
#     time.sleep(5)
#     driver.find_element_by_id('password').send_keys('1520642814Ghh'+Keys.ENTER)
#     time.sleep(5)
#     driver.get('https://www.aparat.com/v/0UELA')
#     time.sleep(3)
#     followvalid = driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a')
#     print(followvalid.text)
#     if followvalid.text =='دنبال کردن':
#         # time.sleep(5)
#         # driver.get('https://www.aparat.com/v/IbcVT')
#         driver.find_element_by_xpath('//*[@id="details"]/div/div[2]/div[2]/a').click()
#         driver.delete_all_cookies()
#     else:
        # driver.delete_all_cookies()

