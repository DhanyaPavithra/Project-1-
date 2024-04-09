# Test case ID: TC_Login_01

# Importing Data and Locator details from respective files:

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# importing explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TCLogin02:

    def __init__(self):
        # initializing the driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

    def LoginPage(self):
        """
        function to Login the webpage using the username and password
        """
        try:
            # boot the webpage
            self.boot()
            # Login page credentials:
            # Using explicit wait, locate and enter username details:
            WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().usernameLocator))).send_keys(data.WebData().username_TCLogin02)
            # Using explicit wait, locate and enter password details:
            WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().passwordLocator))).send_keys(data.WebData().password_TCLogin02)
            # Using explicit wait, locate and click the login button:
            WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locator.WebLocators().loginBtnLocator))).click()

            # The login process is successful:
            if self.driver.current_url == data.WebData().dashboardURL:
                print("The user is logged in successfully")
            else:
                # the login process is not successful and so locate and print the error message:
                errorMessage = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().errorMsgLocator))).text
                print(errorMessage)

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()


obj = TCLogin02()
obj.LoginPage()




