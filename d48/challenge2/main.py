# Selenium Webdriver > BS4 allow us to do things with the website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome() #chromimum-based browsers
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# print(driver.find_element(By.ID,value="articlecount").text)
print(driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]').text)
print(driver.find_element(By.CSS_SELECTOR,value="#articlecount a").text)
print(driver.find_elements(By.CSS_SELECTOR,value="#articlecount a")[0].text)

driver.quit()
