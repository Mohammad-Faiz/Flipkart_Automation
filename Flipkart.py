from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com")
driver.implicitly_wait(7)

#Click on mobiles
driver.find_element(By.XPATH, "//span[text()='Mobiles']").click()
print(driver.title)

#prompt for input and  search
product = "realme 7 Pro"

#search input
driver.find_element(By.XPATH,"//input[@class='_3704LK']").send_keys(product)
driver.find_element(By.CSS_SELECTOR,".L0Z3Pu").click()

#extract deatils of product and store in variable
#features = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[3]/div[1]/div[1]").text
features = driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]").text

#print(features)

#compare details of product
assert product in features

#add to cart
driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
#place order
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div[1]/div/div[3]/div/form/button").click()
