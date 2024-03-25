import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.flipkart.com")
driver.implicitly_wait(7)

#print title of phone
Title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
if driver.title == Title:
    print("You have landed on FlipKart!!")

else:
    print("Need to check site")

#prompt for input
#product = input("Enter your product: ")
product = "Realme 7 pro"

#search input
driver.find_element(By.CSS_SELECTOR,".Pke_EE").send_keys(product)
driver.find_element(By.CSS_SELECTOR,"._2iLD__").click()

#click on first product
driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
print("Clicked on 1st Product!")

#handle multiple windows
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])

#open your product
product = driver.find_element(By.CSS_SELECTOR,".B_NuCI").text
print("Your product is :", product)

#confirmation of product
confirmation = input("Do you really want to go with this item?\n Yes/No: ")
if confirmation.lower() == "yes":
    print("We are proceeding now...")
else:
    print("Choose your product again😥")


#click on buy button
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button").click()

#give you number to login
Phone = input("Give your number to Proceed: ")
driver.find_element(By.XPATH,"//input[@autocomplete='off']").send_keys(Phone)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#enter otp
otp = input("Enter your OTP: ")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@autocomplete='on']")))
driver.find_element(By.XPATH,"//input[@autocomplete='on']").send_keys(otp)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

