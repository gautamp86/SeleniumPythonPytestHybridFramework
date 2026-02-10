from selenium.webdriver.common.by import By

class LanguageTablePage:
    lnkTestTable_XPATH = "//a[normalize-space()='Test Table']"
    rdBtnPython_xpath = "//input[@value='Python']"
    rows_xpath = "//table[@id='courses_table']/tbody/tr"
    languages_xpath = "./td[3]"

    def __init__(self,driver):
        self.driver = driver

    def navigateToTestTable(self):
        self.driver.find_element(By.XPATH,self.lnkTestTable_XPATH).click()

    def clickPythonRadioButton(self):
        self.driver.find_element(By.XPATH,self.rdBtnPython_xpath).click()

    def get_visible_languages(self):
        rows = self.driver.find_elements(By.XPATH, self.rows_xpath)
        languages = []
        for row in rows:
            if row.is_displayed():
                language = row.find_element(By.XPATH, self.languages_xpath).text
                languages.append(language)
        return languages



