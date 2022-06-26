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
#driver.find_element(By.ID,'id="demo-simple-select-outlined"').click()
time.sleep(2)
driver.find_element(By.XPATH,"//body/div[@id='menu-']/div[3]/ul[1]/li[3]").click()

time.sleep(3)

# Click on booknow
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div[6]/button').click()
time.sleep(5)

# Click Add 1st bed
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[4]/div[4]/div[1]/div[4]/div/div/table/tr[4]/td[2]/div/button").click()
#driver.find_element(By.XPATH,"//span[contains(@class,'MuiButton-label jss3628')]").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Add 1st Bed')]").click()

time.sleep(4)
# set implicit wait time
driver.implicitly_wait(5)
# wait for review Booking
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="review_cart_row0"]/div[2]/button')))
time.sleep(2)
price_1=driver.find_element(By.XPATH,'//*[@id="room"]/div/div/table/tr[2]/td[2]/div/div/p/span[2]').text
print("Price 1 :"+price_1)

price_2=driver.find_element(By.XPATH,'//*[@id="review_cart_row0"]/div[1]/div[2]/h6').text
print("Price 2 :"+price_2)

# clickreview booking
driver.find_element(By.XPATH,'//*[@id="review_cart_row0"]/div[2]/button').click()
time.sleep(3)

# wait for login to continue and retrive price
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div/button/span[1]')))
time.sleep(3)
total_price=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div[3]/h6').text
print("Total price :"+total_price)

driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div/button/span[1]').click()
driver.find_element(By.XPATH,"//*[contains(@autocomplete,'kskbck')]").send_keys(Email)
driver.find_element(By.ID, "outlined-adornment-password").send_keys(Password)
time.sleep(3)

driver.find_element(By.XPATH, "//span[starts-with(text(),'Continue')]").click()
time.sleep(3)

#GUUEST DETail
#driver.find_element(By.XPATH,"//div[contains(@xpath,'1')]").click()
driver.find_element(By.XPATH,"//div[@id='demo-simple-select-outlined']").click()
driver.find_element(By.XPATH,"//body/div[@id='menu-']/div[3]/ul[1]/li[2]").click()
#Guest first name & last name deatils
driver.find_element(By.XPATH,"//*[contains(@placeholder,'First Name')]").send_keys(First_Name)
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Last Name')]").send_keys(Last_Name)
driver.find_element(By.XPATH,"//*[contains(@placeholder , 'Mobile Number')]").send_keys(Mobile_Number)
driver.find_element(By.XPATH,"//*[contains(@placeholder , 'Email Address')]").send_keys(Email_Address)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input').send_keys(Address)
driver.find_element(By.XPATH,'//*[@id="react-select-2-input"]').click()
driver.find_element(By.XPATH,"//div[@id='react-select-2-option-14']").click()
driver.find_element(By.XPATH,'//*[@id="react-select-3-input"]').click()
driver.find_element(By.XPATH,"//div[@id='react-select-3-option-1']").click()
driver.find_element(By.XPATH,'//*[@id="react-select-4-input"]').click()
driver.find_element(By.XPATH,"//div[@id='react-select-4-option-1']").click()
driver.find_element(By.XPATH,"//*[contains(@placeholder,'PinCode')]").send_keys(PinCode)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]').click()

#driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(CouponCode)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/input').send_keys(CouponCode)

driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/div[4]/button').click()
print("Completed..")
time.sleep(1234)