import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
print(driver.current_url)

#ID_name, class_name, link_text, xpath, css_selector, tag_name

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = driver.find_element(By.NAME,"password")
password.send_keys("secret_sauce")

login_btn = driver.find_element(By.XPATH,"//input[@id='login-button']")
login_btn.click()
cart = driver.find_element(By.CLASS_NAME,"product_label")

if cart.is_displayed:
  print("user logged in")
else:
  print("something went wrong")


product_backpack = driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
product_backpack.click()

if product_backpack.is_displayed:
  print("bagpack added to cart")
else:
  print("something went wrong")

cart_link = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']")
cart_link.click()

checkout_btn = driver.find_element(By.LINK_TEXT,"CHECKOUT")
checkout_btn.click()

form_f_name = driver.find_element(By.CSS_SELECTOR,"#first-name")
form_f_name.send_keys("Durgesh")

form_l_name = driver.find_element(By.CSS_SELECTOR,"#last-name")
form_l_name.send_keys("Gupta")

form_zip_code = driver.find_element(By.XPATH,"//input[@id='postal-code']")
form_zip_code.send_keys("221007")

continue_btn = driver.find_element(By.XPATH,"//input[@value='CONTINUE']")
continue_btn.click()

finish_btn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[8]/a[2]")
finish_btn.click()

end_msg = driver.find_element(By.XPATH,"(//h2[normalize-space()='THANK YOU FOR YOUR ORDER'])[1]")

if end_msg.is_displayed:
  print("buying workflow automation complete")
else:
  print("something went wrong")


time.sleep(10)





