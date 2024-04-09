"""
locator.py

File contains the Locator details
"""

from selenium.webdriver.common.by import By

class WebLocators:
    """
    The class contains the locator details for the testing process
    """

    def __init__(self) -> object:
        self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.loginBtnLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.errorMsgLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
        self.pimLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
        self.addEmployeeLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
        self.firstNameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        self.middleNameLocatorPIM1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
        # self.middleNameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input'
        # self.middleNameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
        self.middleNameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input'
        self.lastNameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        self.employeeIDLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
        self.saveBtnLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        self.otherIDLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
        self.driverLicenceNumLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        self.licenseExpirydateLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        self.nationalityLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]'
        self.maritalStatusLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'
        self.DOBLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        self.maleRadioBtnLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        self.femaleRadioBtnLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
        self.savePersonalDetailsBtnLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
        # self.savePersonalDetailsBtnLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        self.editOptionLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]'
        self.deleteEmployeeLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'
        self.deleteconfirmationLocator ='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
        self.popupLocator = "oxd-toaster_1"
        self.popupeditLocator = "oxd-toaster_1"
        self.popupDeletionLocator = "oxd-toaster_1"

    def enterText(self, driver, locator, textvalue):
        """
        Function to enter the data by finding the location by using Xpath locators

        """
        driver.find_element(by=By.XPATH, value=locator).send_keys(textvalue)

    def clickBtn(self,driver,locator):
        """
        Function to do click action by finding the location by using Xpath locators

        """
        driver.find_element(by=By.XPATH, value=locator).click()

    def clickRadioBtn(self,driver,locator):
        """
        function to click on the Radio button

        """
        driver.find_element(by=By.XPATH, value=locator).click()



