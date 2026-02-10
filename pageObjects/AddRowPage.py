from selenium.webdriver.common.by import By

class AddRowPage:
    lnkPractice_XPATH = "//a[normalize-space()='Practice']"
    lnkTest_exception_link_text = "Test Exceptions"
    btnAdd_id = "add_btn"
    msgConfirmation_id = "confirmation"
    txtRow_2_id = "row2"

    def __init__(self,driver):
        self.driver = driver

    def navigateToPracticePage(self):
        self.driver.find_element(By.XPATH,self.lnkPractice_XPATH).click()

    def navigateToTestExceptionsPage(self):
        self.driver.find_element(By.LINK_TEXT,self.lnkTest_exception_link_text).click()

    def clickAddBtn(self):
        self.driver.find_element(By.ID,self.btnAdd_id).click()

    def displayConfirmationMessage(self):
        return self.driver.find_element(By.ID,self.msgConfirmation_id).text

    def secondRowDisplayed(self):
        return self.driver.find_element(By.ID,self.txtRow_2_id).is_displayed()
