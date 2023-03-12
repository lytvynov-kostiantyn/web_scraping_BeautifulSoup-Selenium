from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Url for scraping
URL = 'https://eldorado.ua/uk/'

driver = webdriver.Chrome()

# Setting max-size of screen to render all buttons
driver.set_window_size(1920,1080)

# Open the page with selenium and click js buttons to get more data
driver.get(URL)

# Getting the target btn and click on it
class_name = 'iTosHu'
target_btn = more_buttons = driver.find_elements(By.CLASS_NAME, class_name)[0]
target_btn.click()
sleep(5)

response = driver.page_source
driver.quit()

# Beautiful Soup for extracting data
soup = BeautifulSoup(response, 'lxml')
data = soup.body
