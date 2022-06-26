from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)

Email_Address= "trunaliwagh64@gmail.com"
Email = "trunaliwagh64@gmail.com"
Password = "123456"
First_Name ="Tanu"
Last_Name = "Patil"
Mobile_Number = "8286366884"
Address = "plot33/D-25 smaijmi"
Country='India'
State='Maharashtra'
City='Mumbai'
PinCode='400013'
CouponCode='TH50'
GroupSize='10'
Code='91'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.thehosteller.com/ ")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/p').click()
time.sleep(2)
# Select Goa
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/p[3]').click()
time.sleep(3)


#dropdown for traveller
driver.find_element(By.XPATH,"//div[contains(text(),'1')]").click()
time.sleep(2)
#select no of people 10+
driver.find_element(By.XPATH,"//body/div[@id='menu-']/div[3]/ul[1]/li[10]").click()
#Name
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Name')]").send_keys(First_Name)
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Email')]").send_keys(Email)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Group')]").send_keys(GroupSize)
driver.find_element(By.XPATH,"//body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//li[contains(text(),'Goa')]").click()


driver.find_element(By.XPATH,'//*[@id="react-select-2-input"]').click()
driver.find_element(By.XPATH,'//*[contains(@class," css-1d8n9bt")]').clixk()
driver.find_element(By.XPATH,"//div[contains(@id,'react-select-3-placeholder')]").send_keys(Code)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Phone')]").send_keys(Mobile_Number)
driver.find_element(By.XPATH,"//span[contains(text(),'Submit Req')]").click()
# Click on booknow
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div[6]/button').click()
time.sleep(3)
