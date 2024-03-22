import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com")

#Input by user
product = input("Give your Input: ")

#search input
driver.find_element(By.CSS_SELECTOR,".Pke_EE").send_keys(product)
time.sleep(5)

print("\nThese are the suggestion we are getting after typing",product,":")
options = driver.find_elements(By.CSS_SELECTOR,"._3D0G9a")

#total suggestions
for option in options:
      print(option.text.capitalize())

if len(options) >= 5:
    fifth_suggestion_text = options[4].text
    print("\nFifth suggestion:", fifth_suggestion_text.capitalize())
else:
    print("\nThere are less than 5 suggestions.")






