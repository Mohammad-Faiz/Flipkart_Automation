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
driver.implicitly_wait(5)

# print title of phone
Title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
if driver.title == Title:
    print("You have landed on FlipKart!!")
else:
    print("Need to check site")
    # driver.close()

#handle windows
#windows_opened = driver.window_handles 

def selection():
    global confirmation
    global selected_product
    # prompt for input
    product = input("Enter your product: ")
    #product = "Realme 7 pro"

    # search input
    driver.find_element(By.CSS_SELECTOR, ".Pke_EE").send_keys(product)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # open your product
    # product = driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").text
    # print("Your product is :", product)

    #list of products
    products = driver.find_elements(By.CSS_SELECTOR,"._4rR01T")
    print("List of available products: 🤩")
    # for product in products[:5]:
    #     print(product.text)

    # Enumerate through the first five products
    for index, product in enumerate(products[:5], start=1):
        print(f"{index}. {product.text}")

    # Prompt user for input to select a product
    selected_product_index = int(input("Choose the desired option...😋: "))

    # Adjust index to match list indexing
    selected_product = products[selected_product_index - 1]

    #confirmation of final product
    print("Selected Product:", selected_product.text)
    confirmation = input("Do you really want to go with this item?\n Yes/No: ")

selection()

# confirmation of product
if confirmation.lower() == "yes":
    print("We are proceeding now...")

    #click on product
    # driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
    time.sleep(5)

    selected_product.click()
    print("Clicking on final Product😍")

    # handle multiple windows
    # handle windows
    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])


    # click on buy button
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button").click()


    # give you number to login
    Phone = input("Give your number to Proceed: ")
    driver.find_element(By.XPATH, "//input[@autocomplete='off']").send_keys(Phone)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # enter otp
    otp = input("Enter your OTP: ")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@autocomplete='on']")))
    driver.find_element(By.XPATH, "//input[@autocomplete='on']").send_keys(otp)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


elif confirmation.lower() == "no":
    print("Choose your product again😥") 

    driver.get("https://www.flipkart.com")
    time.sleep(3)

    #click on popup bar
    popup = driver.find_element(By.XPATH, "/html/body/div[3]/div/span")
    if popup.is_displayed():
        popup.click()
    selection()

