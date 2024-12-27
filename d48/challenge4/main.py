#cookieclicker game (kinda work but got network blocked?)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ast
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


game_on = True
cookies_stat = 0
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()
time.sleep(1)

while game_on:
  start_time = time.time()
  product_list = []
  driver.find_element(By.ID,'bigCookie').click()
  
  #every 5 seconds checking to buy products
  for i in range(0,5):
    time.sleep(1)
  
  for product in driver.find_elements(By.CLASS_NAME,"product.unlocked.enabled"): #class name with space resolved by dot
    text = product.get_attribute("id")
    price = float(driver.find_element(By.ID, text).text.split('\n')[1].replace(',',''))
    product_list.append({'name':text, 'price':price})
    
  cookies_stat = int(driver.find_element(By.ID,'cookies').text.split(" ")[0].replace(',',''))
  try:
    chosen_product = product_list[-1]['name']
    highest_price = product_list[-1]['price']
    # buy the most expensive stuff
    if cookies_stat > highest_price:
      driver.find_element(By.ID, chosen_product).click()
  except:
    driver.find_element(By.ID,'bigCookie').click()

  if time.time() - start_time ==300:
    game_on = False

  driver.quit()

