from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageObject(object):

    def __init__(self, driver):
        self.driver = driver

    def waitElementToLoad(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            )
        except:
            print("Element did not appear")
        return element