import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re


options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")
email = chrome.find_element_by_id('email')
password = chrome.find_element_by_id('pass')

email.send_keys('maybuby0721@yahoo.com.tw')
password.send_keys('bubymay0721')
password.submit()

time.sleep(3)
chrome.get("https://www.facebook.com/profile.php?id=100003087240828")

for x in range(1, 3):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

time.sleep(5)
soup = BeautifulSoup(chrome.page_source, 'html.parser')

# chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]').click()
# chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[2]/span[2]/span').click()

def get_date(soup, Dates = []):
    dates = soup.find_all('b', {'class':'b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4'})
    for date in dates:
        if (re.match(date_r, date.getText()) == None):
            Date = date.getText().strip('=') 
            Dates.append(date.getText())
    return Dates

def get_content(soup, Contents = []):
    contents3 = soup.find_all('div', {'class':'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
    for contents in contents3:
        content = contents.find('div', {'style':'text-align: start;'})
        Contents.append(content.getText())


contents3 = soup.find_all('div', {'class':'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
# dates = soup.find_all('b', {'class':'b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4'})

reqs2 = soup.find_all('div',{'class':'ecm0bbzt e5nlhep0 a8c37x1j'})
date_r = re.compile(r'[=]')
Contents = []
Dates = []
Requests = []
time.sleep(5)


# for contents in contents3:
#     content = contents.find('div', {'style':'text-align: start;'})
#     Contents.append(content.getText())
get_date(soup, Dates)

time.sleep(5)

get_content(soup, Contents)
# print(get_content(soup, Contents))
# req = reqs2.find('div',{'dir':'auto'})
# for R in reqs2:
#     rs = R.find('div', {'style':'text-align: start;'})
#     print(rs.getText())
time.sleep(5)
for i in range(0, len(Contents)):
    print()
    print('發文時間: ', Dates[i])
    print('內容: ', Contents[i])    
chrome.quit()