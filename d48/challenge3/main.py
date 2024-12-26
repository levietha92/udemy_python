# Selenium Webdriver > BS4 allow us to do things with the website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome() #chromimum-based browsers
driver.get("http://secure-retreat-92358.herokuapp.com/")

# driver.find_element(By.LINK_TEXT)
driver.find_element(By.NAME,"fName").send_keys("hihi")
driver.find_element(By.NAME,"lName").send_keys("bb")
driver.find_element(By.NAME,"email").send_keys("hihi_bb@gmail.com")

driver.find_element(By.TAG_NAME,"button").click()