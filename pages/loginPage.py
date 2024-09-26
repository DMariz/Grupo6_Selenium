from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base

class LoginPage(Base):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    title = "OrangeHRM"
    login_btn = (By.CLASS_NAME, 'orangehrm-login-button')

    def __init__(self, browser):
        super(LoginPage, self).__init__(driver=None, browser=browser)

    def open_login(self):
        self.driver.get(self.url)

    def faz_login(self, user, password):
        # Aguarda até o campo de username estar visível
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys(user)
        # Aguarda até o campo de senha estar visível
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys(password)
        self.click_login_button()

    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_login_title(self):
        return self.driver.title == self.title

    '''
    def has_login_message_error(self):
        error = self.driver.find_element(By.XPATH, "//*[contains(text(),'Epic sad face: Username is required')]")
        return error.is_displayed()
    '''
