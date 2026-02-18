from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class LoginPage(BasePage):
    __username = (By.ID, "username")
    __password = (By.ID, "password")
    __login_btn = (By.XPATH, "//button[@id='submit']")
    __logout = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.type(self.__username, username)
        self.type(self.__password, password)
        self.click(self.__login_btn)

    def logout(self):
        self.click(self.__logout)

