# Test case ID: TC_PIM_03:
# Importing Data and Locator details from respective files:
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing Exceptions
from selenium.common.exceptions import NoSuchElementException
# importing Actions Chains
from selenium.webdriver import ActionChains
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMmoduleThree:

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

    def deleteEmployee(self):
        """
        function to delete the employee details in the portal

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
            # Using explicit wait, locate and click the 'delete employee' field:
            WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().deleteEmployeeLocator))).click()
            # Using explicit wait, locate and click the 'delete confirmation' option:
            WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().deleteconfirmationLocator))).click()
            # Using explicit wait, wait for the pop up message to show and fetch the text of the pop up message:
            popupDelete = WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.ID, data.WebData().popupDeletionMsg))).text
            # print the pop up message:
            print(popupDelete)
            print("Successfully deleted")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = PIMmoduleThree()
obj.deleteEmployee()