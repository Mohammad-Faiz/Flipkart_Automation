from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com")
driver.implicitly_wait(5)

#Click on mobiles
driver.find_element(By.XPATH, "//span[text()='Mobiles']").click()
print(driver.title)

#search input
driver.find_element(By.XPATH,"//input[@class='_3704LK']").send_keys("Realme 7 pro")
driver.find_element(By.CSS_SELECTOR,".L0Z3Pu").click()

features = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[3]/div[1]/div[1]").text
print(features)

assert "(Mirror Blue, 128 GB)  (8 GB RAM)" in features

