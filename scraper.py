from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# import By
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.google.com"

driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
# print(driver.title)
print(soup.prettify())