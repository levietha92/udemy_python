# Selenium Webdriver > BS4 allow us to do things with the website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome() #chromimum-based browsers
driver.get("https://www.python.org/")


time_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")]
event_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR,value=".event-widget ul a")]

events = {}

for n in range(len(time_list)):
  events[n] = {
    "time": time_list[n],
    "name": event_list[n]
  }

print(events)




driver.quit()
