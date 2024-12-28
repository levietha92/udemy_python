#property rent price

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup


class ExtractZillowData():
  def __init__(self):
    response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
    self.soup = BeautifulSoup(response.text, "html.parser")
    self.property_list = []
    self.address = []
    self.link = []
    self.price = []

  def extract_data(self):
    for tile in self.soup.find_all(name='a',class_='StyledPropertyCardDataArea-anchor'):
      self.address.append(tile.text.replace('\n                                  ',''))
      self.link.append(tile.get('href'))

    for tile in self.soup.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine'):
      self.price.append(tile.getText())
      
    for i in range(0, len(self.address)):
      self.property_list.append({
        'address':self.address[i],
        'link':self.link[i],
        'price':self.price[i]
      })
    print(f'Extracting data is complete, there are {len(self.property_list)} items')
    return self.property_list

class DataEntry():
  def __init__(self,url):
    self.driver = webdriver.Chrome()
    self.url = url
    self.driver.get(self.url)

  def _click_tab(self, number_of_tabs):
    for i in range(0,number_of_tabs):
      ActionChains(self.driver).send_keys(Keys.TAB).perform()

  def _click_enter(self):
    ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        
  def enter_data(self, data_input:dict):
    for i in range(0,len(data_input)):
      self.driver.find_elements(By.TAG_NAME,'input')[3].send_keys(data_input[i]['address'])
      self.driver.find_elements(By.TAG_NAME,'input')[4].send_keys(data_input[i]['link'])
      self.driver.find_elements(By.TAG_NAME,'input')[5].send_keys(data_input[i]['price'])
      print(f'Complete data entry for item {i}')
      self._click_tab(1)
      self._click_enter()
      self._click_tab(1)
      self._click_enter()
      time.sleep(2)
      
  # def check_result(self):
  #   self.driver.get("https://docs.google.com/spreadsheets/d/1stBYWSUGBwmXExzEJZpHVygg95yM4pIQhCzEBEZelNs/edit?resourcekey=&gid=1045418401#gid=1045418401")
  
  def close(self):
    self.driver.quit()


# Getting info from Property Page
data_input = ExtractZillowData().extract_data()
# Passing info into the google form
entry = DataEntry(url="https://forms.gle/Tww4TwrzKkpd8B4a6")
entry.enter_data(data_input)
# entry.check_result()
entry.close()
print("complete all entries")