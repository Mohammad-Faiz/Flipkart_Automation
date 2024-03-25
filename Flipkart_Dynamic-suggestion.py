import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create a ChromeOptions object
chrome_options = Options()

# Enable headless mode
chrome_options.add_argument("--headless") #disable as per your need

# Initialize the Chrome webdriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Implicitly wait for elements to be found
driver.implicitly_wait(5)

# Open Flipkart website
driver.get("https://www.flipkart.com")

# Input by user
product = input("Give your Input: ")

# Search input
driver.find_element(By.CSS_SELECTOR, ".Pke_EE").send_keys(product)
time.sleep(6)

# Fetch suggestions
options = driver.find_elements(By.CSS_SELECTOR, "._3D0G9a")

if len(options) >= 5:
    fifth_suggestion_text = options[4].text
    print("\nFifth Suggestion:", fifth_suggestion_text.capitalize())
else:
    print("\nThere are less than 5 Suggestions.")

# Close the browser
driver.quit()
