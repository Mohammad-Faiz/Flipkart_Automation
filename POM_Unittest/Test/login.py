import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from POM_Unittest.pages.LoginPage import LoginPage
from POM_Unittest.pages.HomePage import Homepage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        cls.driver = webdriver.Chrome(chrome_options)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")

        login = LoginPage(driver)
        login.enter_username("student")
        login.enter_password("Password123")
        login.click_login()

        homepage = Homepage(driver)
        homepage.logout()
        time.sleep()

    @classmethod
    def tearDownClass(cls):
        # time.sleep(5)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
