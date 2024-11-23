# Selenium Webdriver > BS4 allow us to do things with the website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome() #chromimum-based browsers
driver.get("https://selenium-python.readthedocs.io/navigating.html")

# print(driver.find_element(By.CLASS_NAME,value="Poll_question__Q1AjI").text)
# print(driver.find_element(By.CLASS_NAME,value="Poll_options__yMEpp").text)
# can use By.CSS_SELECTOR or if doesn't work --> XPATH

print(driver.find_element(By.XPATH,value='//*[@id="interacting-with-the-page"]/p[3]/cite').text)
# driver.close()
driver.quit()
