from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver, browser = None ):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            else:
                raise Exception('Browser with no support!')

    def is_url(self,url):
        return self.driver.current_url==url

    def wait_element(self, element_tuple,timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(element_tuple))

    def close(self):
        self.driver.quit()