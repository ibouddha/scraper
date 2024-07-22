from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
import time
import json
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.emploidakar.com/offres-demploi-au-senegal/"

driver.get(url)

# Wait for the search input to be present
wait = WebDriverWait(driver, 10)
search = wait.until(EC.presence_of_element_located((By.ID, 'search_keywords')))

search.clear()
search.send_keys("python")
search.send_keys(Keys.ENTER)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'job_listings')))
time.sleep(3)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Find all paragraphs
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'alert')))

json_offre = []
liste = soup.findAll('li', class_='job_listing')
# Write paragraphs to file
for p in liste:
    title = p.find('h3').get_text()
    lien = p.find('a')['href']
    company = p.find('div',class_='company').get_text().strip()
    lieu = p.find('div',class_='location').get_text().strip()
    date = p.find('li',class_='date').get_text().strip()
    offre = {"title":title,"Company":company,"Lien":lien,"date":date,"Adresse":lieu}
    json_offre.append(offre)
    with open("output.json", "w+") as file:
        json.dump(json_offre,file,ensure_ascii=False,indent=4)