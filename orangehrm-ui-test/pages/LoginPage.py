from selenium import webdriver
from selenium.webdriver.common.by import By
# from base_page import Base_Page
# import Base_Page
# import Base_Page
from pages.BasePage import BasePage

class Login_Page(BasePage):

    url_login = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    title = "Swag Labs"

    username = (By.CSS_SELECTOR, '[name="username"]')
    password = (By.CSS_SELECTOR, '[name="password"]')
    login_btn = (By.CLASS_NAME, 'orangehrm-login-button')

    
    def __init__(self, browser):
        super(Login_Page, self).__init__(driver=None, browser=browser)
    
    def open(self):
        self.driver.get(self.url_login)
        self.driver.implicitly_wait(5)
    
    def get_driver(self):
        return self.driver
    
    # def click_login_button(self):
    #     self.driver.find_element(*self.login_btn).click()
    #
    # def is_url(self):
    #     return self.driver.current_url == self.url_demo
    #
    # def is_title(self):
    #     return self.driver.title == self.title
    
    # def has_login_message_error(self):
    #     is_error = self.driver.find_element(*self.error_message).text == self.error_message_text
    #     return is_error
    
    def login_with_admin_user(self):
        self.driver.find_element(*self.username).send_keys('Admin')
        self.driver.find_element(*self.password).send_keys('admin123')
        self.driver.find_element(*self.login_btn).click()
    