from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_id = "submit"

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()