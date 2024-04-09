# Importing Data and Locator details from respective files:
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing keys
from selenium.webdriver.common.keys import Keys
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

class TestPOM:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(25)
        yield
        self.driver.quit()

    @pytest.mark.html
    def testTitle(self,boot):
        self.driver.get(data.WebData().url)
        assert self.driver.title == data.WebData().title


    def testLoginTC01(self,boot):
        # boot the webpage using url
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin01)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin01)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

        assert self.driver.current_url == data.WebData().dashboardURL

    def testLoginTC02(self,boot):
        # boot the webpage using url
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin02)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin02)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

        assert self.driver.current_url != data.WebData().dashboardURL

    def testTCPim01(self, boot):
        # boot the webpage using url
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin01)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin01)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

        # PIM module:
        # Using explicit wait, locate and click the PIM module:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().pimLocator))).click()
        # Using explicit wait, locate and click the 'add employee' option:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().addEmployeeLocator))).click()
        # Using explicit wait, locate and fill the data for 'first name':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().firstNameLocator))).send_keys(data.WebData().firstName)
        # Using explicit wait, locate and fill the data for 'middle name':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().middleNameLocatorPIM1))).send_keys(data.WebData().middleName)
        # Using explicit wait, locate and fill the data for 'last name':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().lastNameLocator))).send_keys(data.WebData().lastName)
        # Using explicit wait, locate, clear the 'employee id' field:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().employeeIDLocator))).send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        # Using explicit wait, locate and fill the data for 'employee id':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().employeeIDLocator))).send_keys(data.WebData().employeeID)
        # Using explicit wait, locate and click the 'save' button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().saveBtnLocator))).click()

        # Personal details:

        # Using explicit wait, locate and fill the data for 'other id':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().otherIDLocator))).send_keys(data.WebData().otherID)
        # Using explicit wait, locate and fill the data for 'driver license number':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().driverLicenceNumLocator))).send_keys(data.WebData().driverLicenseNum)
        # Using explicit wait, locate and fill the data for 'license Expiry date':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().licenseExpirydateLocator))).send_keys(data.WebData().licenseExpiryDate)
        # Using explicit wait, locate and fill the data for 'Date of birth':
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().DOBLocator))).send_keys(data.WebData().DOB)
        # Using explicit wait, locate and click the 'female' radio button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().femaleRadioBtnLocator))).click()
        # Using explicit wait, locate and click the 'save' button to save the personal details:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().savePersonalDetailsBtnLocator))).click()
        # Using explicit wait, wait for the pop up message to show and fetch the text of the pop up message:
        popup = (WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.ID, locator.WebLocators().popupLocator)))).text

        assert popup == data.WebData().popupMsg

    def testTCPim02(self, boot):
        # boot the webpage using url
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin01)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin01)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

        # PIM module:
        # Using explicit wait, locate and click the PIM module:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().pimLocator))).click()
        # Using explicit wait, locate and click the 'edit' option:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().editOptionLocator))).click()
        # Using explicit wait, locate and clear the 'middle name' field:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().middleNameLocator))).send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        # Using explicit wait, locate and fill the 'middle name' field:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().middleNameLocator))).send_keys(data.WebData().editMiddleName)
        # Using explicit wait, locate and click the 'save' option to save the personal details:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().savePersonalDetailsBtnLocator))).click()
        # Using explicit wait, wait for the pop up message to show and fetch the text of the pop up message:
        popupedit = (WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.ID, locator.WebLocators().popupeditLocator)))).text
        # print the pop up message:
        print(popupedit)
        assert popupedit == data.WebData().popupeditMsg

    def testTCPim03(self,boot):
        # boot the webpage using url
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin01)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin01)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

        # PIM module:
        # Using explicit wait, locate and click the PIM module:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().pimLocator))).click()
        # Using explicit wait, locate and click the 'delete employee' field:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().deleteEmployeeLocator))).click()
        # Using explicit wait, locate and click the 'delete confirmation' option:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().deleteconfirmationLocator))).click()
        # Using explicit wait, wait for the pop up message to show and fetch the text of the pop up message:
        popupDelete = WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.ID, locator.WebLocators().popupDeletionLocator))).text

        assert popupDelete == data.WebData().popupDeletionMsg

