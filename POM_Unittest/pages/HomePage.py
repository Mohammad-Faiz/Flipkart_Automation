from selenium.webdriver.common.by import By


class Homepage():

    def __int__(self, driver):
        self.driver = driver
        self.logout_button_xpath = "//*[@id='loop-container']/div/article/div[2]/div/div/div/a"


    def logout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.logout_button_xpath).click()
