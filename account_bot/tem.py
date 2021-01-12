import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def get_tem(area):
    options = Options()
    options.add_argument("--disable-notifications")

    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://www.cwb.gov.tw/V8/C/W/OBS_Map.html")
    soup = BeautifulSoup(chrome.page_source, 'html.parser')

    date = soup.find('span', {'id':'preestimate'})
    citys = soup.find_all('span', {'class':'city'})
    tems = soup.find_all('span', {'class':'tem-C is-active'})
    weathers = soup.find_all('img', {'class':'img-responsive'})
    CT = date.text+'\n'
    if(area == '北部'):
        for i in range(0, 5):
            CT += ("{:^4}: {:>5}˙C {:>5} \n".format(citys[i].text, tems[i].text, weathers[i+1]['alt']))

    if(area == '中部'):
        for i in range(5, 8):
            CT += ("{:^4}: {:>5}˙C {:>5} \n".format(citys[i].text, tems[i].text, weathers[i+1]['alt']))

    if(area == '南部'):
        for i in range(8, 11):
            CT += ("{:^4}: {:>5}˙C {:>5} \n".format(citys[i].text, tems[i].text, weathers[i+1]['alt']))

    if(area == '東部'):
        for i in range(11, 14):
            CT += ("{:^4}: {:>5}˙C {:>5} \n".format(citys[i].text, tems[i].text, weathers[i+1]['alt']))   

    if(area == '離島'):
        for i in range(14, 20):
            CT += ("{:^4}: {:>5}˙C {:>5} \n".format(citys[i].text, tems[i].text, weathers[i+1]['alt']))

    chrome.quit()
    return CT

# print(get_tem('北部'))