from socket import send_fds
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    side_panel = (By.CLASS_NAME, "oxd-sidepanel-body")
    menu_admin = (By.CSS_SELECTOR, '[href="/web/index.php/admin/viewAdminModule"]')
    toast = (By.CSS_SELECTOR, 'div.oxd-toast-container.oxd-toast-container--bottom')

    def __init__(self, driver, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception('Browser nao suportado!')

    def is_url(self,url):
        return self.driver.current_url==url

    def wait_element(self, element_tuple,timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element_tuple))

    def close(self):
        self.driver.quit()

    # def wait_element(self, element_tuple, timeout=5):
    #     WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located((element_tuple)))

    def has_side_panel(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.side_panel))
            return True
        except NoSuchElementException:
            return False

    def click_menu_admin(self):
        self.driver.find_element(*self.menu_admin).click()

    def is_toast_visible(self):
        try:
            self.wait_element(self.toast, timeout=5)
            return True
        except NoSuchElementException:
            return False

    def close(self):
        self.driver.quit()