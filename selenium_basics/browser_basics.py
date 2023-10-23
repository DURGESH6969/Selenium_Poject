# selenium 4
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
driver.minimize_window() #minimizing window
driver.maximize_window() #maximizing window
driver.get("https://demoqa.com/element")
driver.back()
time.sleep(5)
driver.forward()
driver.refresh()
print(driver.current_url)
time.sleep(3)

driver.exit()