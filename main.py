from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import re

# Url for scraping
URL = 'https://eldorado.ua/uk/'

CONTACT_INF = {}

driver = webdriver.Chrome()

# Setting max-size of screen to render all buttons
driver.set_window_size(1920,1080)

# Open the page with selenium and click js buttons to get more data
driver.get(URL)
class_name = 'iTosHu'
target_btn = driver.find_elements(By.CLASS_NAME, class_name)[0]
target_btn.click()
# sleep(5)

response = driver.page_source
driver.quit()

# Beautiful Soup for extracting data
soup = BeautifulSoup(response, 'lxml')
data = str(soup.body)

# Getting all phone numbers
num_format_1 = re.findall(r'[\d]{3}\s[\d]{3}\s[\d]{2}\s[\d]{2}', data) # 044 299 46 38
num_format_2 = re.findall(r'[\d]{1}\s[\d]{3}\s[\d]{3}\s[\d]{3}', data) # 0 442 994 638
CONTACT_INF['phone_numbers'] = list(set(num_format_1 + num_format_2))

# Getting all emails
CONTACT_INF['emails'] = re.findall(r'\w+@\w+.\w+', data)

# Getting telegram
CONTACT_INF['telegram'] = re.findall(r'http[s]?://t\.me/\S[^\"]*', data)

# Getting viber
CONTACT_INF['viber'] = re.findall(r'viber://\S[^\"]*', data)

# Getting facebook
CONTACT_INF['facebook'] = re.findall(r'http[s]?://www\.facebook\.com/\S[^\"]*', data)

# Getting youtube
CONTACT_INF['youtube'] = re.findall(r'http[s]?://www\.youtube\.com/\S[^\"]*', data)

# Getting instagram
CONTACT_INF['instagram'] = re.findall(r'http[s]?://www\.instagram\.com/\S[^\"]*', data)

# Getting tiktok
CONTACT_INF['tiktok'] = re.findall(r'http[s]?://www\.tiktok\.com/\S[^\"]*', data)

