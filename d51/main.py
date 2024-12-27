#twitter and ISP provider
#technically this works but Elon is a jerk that prevents normal bot but allow other bots
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ast
import pandas as pd
from dotenv import load_dotenv
import os

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()

def click_enter(driver):
  ActionChains(driver).send_keys(Keys.ENTER).perform()

def click_tab(driver, number_of_tabs):
  for i in range(0,number_of_tabs):
    ActionChains(driver).send_keys(Keys.TAB).perform()
    
# getting the internet speed
print("Getting the internet speed")
driver.get("https://www.speedtest.net/")
download_speed = ''
upload_speed = ''
click_tab(driver, 2)
click_enter(driver)
while len(upload_speed)==0:
  time.sleep(1)
  download_speed = driver.find_element(By.CLASS_NAME,'result-data-large.number.result-data-value.download-speed').text
  upload_speed = driver.find_element(By.CLASS_NAME,'result-data-large.number.result-data-value.upload-speed').text  

print(f"Getting data complete: download {download_speed}, upload {upload_speed}")

# navigate over to X to complain (i could add some logic of threshold here before complaining but meh)
driver.get('https://x.com/compose/post')


email = os.getenv('X_EMAIL')
pwd = os.getenv('X_PASSWORD')
time.sleep(5)

driver.find_element(By.TAG_NAME,'input').send_keys(email)
click_enter(driver)
driver.find_elements(By.TAG_NAME,'input')[1].send_keys(pwd)
click_enter(driver)
message = f"""Hey ISP, why is my internet speed so slow?? 
  Download speed {download_speed} bpm, upload {upload_speed} bpm
  #complainbotsuccess
"""
driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block.public-DraftStyleDefault-ltr').send_keys(message)
  
driver.find_elements(By.TAG_NAME,'button')[1].click() 
click_tab(driver,7)
click_enter(driver)
driver.get("https://x.com/leya1540282/with_replies") 
driver.quit()