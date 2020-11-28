import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def get_date(soup, Dates = []):
    dates = soup.find_all('b', {'class':'b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4'})
    date_r = re.compile(r'[=]')
    date_cf = re.compile(r'[0-9]+')
    for date in dates:
        if (re.match(date_r, date.getText()) == None):
            Date = date.getText().strip('=') 
            date2 = date_cf.findall(date.getText())
            date3 = date2[0] + '月' + date2[1] + '號'
            Dates.append(date3)

def get_content(soup, Contents = []):
    contents3 = soup.find_all('div', {'class':'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
    for contents in contents3:
        content = contents.find('div', {'style':'text-align: start;'})
        Contents.append(content.getText())

def start(Email, Password, url):
    options = Options()
    options.add_argument("--disable-notifications")

    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get('https://www.facebook.com/')
    email = chrome.find_element_by_id('email')
    password = chrome.find_element_by_id('pass')

    email.send_keys(Email)
    password.send_keys(Password)
    password.submit()

    time.sleep(3)
    chrome.get(url)

    for x in range(1, 3):
        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    time.sleep(3)
    soup = BeautifulSoup(chrome.page_source, 'html.parser')



    # contents3 = soup.find_all('div', {'class':'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
    # reqs2 = soup.find_all('div',{'class':'ecm0bbzt e5nlhep0 a8c37x1j'})
    Contents = []
    Dates = []
    # Requests = []
    time.sleep(3)

    get_date(soup, Dates)
    time.sleep(3)
    get_content(soup, Contents)

    time.sleep(3)
    for i in range(0, len(Contents)):
        print()
        print('發文時間: ', Dates[i])
        print('內容: ', Contents[i])    
    chrome.quit()