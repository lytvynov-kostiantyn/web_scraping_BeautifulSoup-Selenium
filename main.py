import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

URL = 'https://eldorado.ua/uk/'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.get(URL)
html = driver.page_source
driver.quit()

print(html)
