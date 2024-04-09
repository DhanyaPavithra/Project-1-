# Test case ID: TC_PIM_02:

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



class PIMmoduleTwo:

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

    def editEmployee(self):
        """
        function to edit the employee details in the portal

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
            print("Successfully edited employee details")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()


obj = PIMmoduleTwo()
obj.editEmployee()