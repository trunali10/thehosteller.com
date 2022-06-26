from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.thehosteller.com/ ")
driver.maximize_window()
time.sleep(2)
# Hotel seclection
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/p').click()
time.sleep(2)
# Select Goa
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/p[3]').click()
time.sleep(3)
#dropdown for traveller
driver.find_element(By.XPATH,"//div[contains(text(),'1')]").click()

time.sleep(2)
driver.find_element(By.XPATH,"//body/div[@id='menu-']/div[3]/ul[1]/li[3]").click()

time.sleep(3)

# Click on booknow
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div[6]/button').click()
time.sleep(7)
# verify the Asserrtion passed to match the text given or not
abc=driver.find_element(By.XPATH,"//h1[contains(text(),'The Hosteller')]").text
print(abc)


