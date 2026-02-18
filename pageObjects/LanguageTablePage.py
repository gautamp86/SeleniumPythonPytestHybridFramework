from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class LanguageTablePage(BasePage):

    # ⭐ Encapsulated locators
    __lnk_test_table = (By.XPATH, "//a[normalize-space()='Test Table']")
    __rd_btn_python = (By.XPATH, "//input[@value='Python']")
    __rows = (By.XPATH, "//table[@id='courses_table']/tbody/tr")
    __language_column = "./td[3]"

    def __init__(self, driver):
        super().__init__(driver)

    # ⭐ Business Actions (Abstraction)

    def navigate_to_test_table(self):
        self.click(self.__lnk_test_table)

    def click_python_radio_button(self):
        self.click(self.__rd_btn_python)

    def get_visible_languages(self):

        rows = self.driver.find_elements(*self.__rows)
        languages = []

        for row in rows:
            if row.is_displayed():
                language = row.find_element(
                    By.XPATH,
                    self.__language_column
                ).text
                languages.append(language)

        return languages
