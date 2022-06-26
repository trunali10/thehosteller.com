from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
Email = "trunaliwagh64@gmail.com"
Password = "123456"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open  website
driver.get("https://www.thehosteller.com/")
driver.maximize_window()
time.sleep(1)
# find username/email field and send the username itself to the input field
driver.find_element(By.CSS_SELECTOR,'div.flex.items-center > p.text-base').click()

driver.find_element(By.XPATH,"//*[contains(@autocomplete,'kskbck')]").send_keys(Email)
driver.find_element(By.ID, "outlined-adornment-password").send_keys(Password)
time.sleep(3)
# click to login
driver.find_element(By.XPATH, "//span[starts-with(text(),'Continue')]").click()
time.sleep(3)