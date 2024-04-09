# Test case ID: TC_PIM_01:

# Importing Data and Locator details from respective files:
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing Exceptions
from selenium.common.exceptions import NoSuchElementException
# importing keys
from selenium.webdriver.common.keys import Keys
# importing Actions Chains
from selenium.webdriver import ActionChains
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMmoduleOne:

    def __init__(self):
        # initializing the driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
    def boot(self):
        """
        To boot the webpage with the url
        """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()


    def quit(self):
        """
        To quit the webpage
        """
        self.driver.quit()

    def addEmployee(self):
        """
        function to add employee to the portal

        """

        try:
            # boot the webpage
            self.boot()
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
            # print the pop up message:
            print(popup)

            print("Employee added successfully")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = PIMmoduleOne()
obj.addEmployee()

