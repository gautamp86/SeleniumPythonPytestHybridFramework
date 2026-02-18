from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class AddRowPage(BasePage):

    # ⭐ Encapsulated locators (private)
    __lnk_practice = (By.XPATH, "//a[normalize-space()='Practice']")
    __lnk_test_exception = (By.LINK_TEXT, "Test Exceptions")
    __btn_add = (By.ID, "add_btn")
    __msg_confirmation = (By.ID, "confirmation")
    __txt_row_2 = (By.ID, "row2")

    def __init__(self, driver):
        super().__init__(driver)

    # ⭐ Business actions (Abstraction)

    def navigate_to_practice_page(self):
        self.click(self.__lnk_practice)

    def navigate_to_test_exceptions_page(self):
        self.click(self.__lnk_test_exception)

    def click_add_button(self):
        self.click(self.__btn_add)

    def get_confirmation_message(self):
        return self.get_text(self.__msg_confirmation)

    def is_second_row_displayed(self):
        return self.is_displayed(self.__txt_row_2)
