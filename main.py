import unittest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from LoginPage import LoginPageObject

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        options.log.level = "trace"
        print("Setting up Firefox driver")
        self.driver = webdriver.Firefox(options=options,executable_path="/usr/bin/geckodriver")
        print("Navigate to the Argyle URL")
        self.driver.get('https://console.argyle.com/')

    def test_upper(self):
        loginPageObject = LoginPageObject(self.driver)
        loginPageObject.enterEmail()
        loginPageObject.enterPassword()
        loginPageObject.clickSignInButton()
        error = loginPageObject.getErrorMessage()
        print("Displayed error message: " + error)
        assert "Invalid email and password combination" == error, "Error messages do not match"
        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()