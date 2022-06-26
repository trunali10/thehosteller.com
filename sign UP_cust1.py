from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

Full_Name = "Papu"
Email_Address = "hicama5044@runqx.com"
Verification_Code = "32165"
Mobile_Number = "8286366884"
Password = "123456"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.thehosteller.com/")
driver.maximize_window()
time.sleep(1)
# sign up just inputting a details
driver.find_element(By.CSS_SELECTOR,'div.flex.items-center > p.text-base').click()

driver.find_element(By.CSS_SELECTOR,"p.text-grey.text-center > span.text-soil.font-semibold.cursor-pointer").click()
# details of customer dummy
driver.find_element(By.XPATH,"//*[contains(@autocomplete,'kskbck')]").send_keys(Full_Name)
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Ema')]").send_keys(Email_Address)
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Veri')]").send_keys(Verification_Code)
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Mobi')]").send_keys(Mobile_Number)
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Pass')]").send_keys(Password)
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(),'Sign Up')]").click()