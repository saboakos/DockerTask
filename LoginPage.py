from selenium.webdriver.common.by import By
from BasePage import BasePageObject

class LoginPageObject(BasePageObject):

    def clickSignInButton(self):
        print("Click on the Sign in button")
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        signin_button.click()

    def enterEmail(self):
        print("Enter email address")
        email_input = self.driver.find_element(By.ID, "sign-in-email")
        email_input.send_keys("test@test.com")

    def enterPassword(self):
        print("Enter user password")
        email_input = self.driver.find_element(By.ID, "sign-in-passowrd")
        email_input.send_keys("Password123!@#")

    def getErrorMessage(self):
        return self.waitElementToLoad("p[id='sign-in-email-helper']").text