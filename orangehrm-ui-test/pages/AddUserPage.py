import time

from pages.BasePage import BasePage
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from faker import Faker



class AddUserPage(BasePage):

    title = (By.CLASS_NAME, 'orangehrm-main-title')
    select_list = (By.CLASS_NAME, 'oxd-select-text--active')
    employee_name = (By.CLASS_NAME, 'oxd-autocomplete-text-input')
    input_list = (By.CLASS_NAME, 'oxd-input--active')
    btn_save = (By.CLASS_NAME, 'orangehrm-left-space')
    fake = Faker()


    def __init__(self, driver):
        super(AddUserPage, self).__init__(driver=driver)

    def is_title(self):
        return self.driver.find_element(*self.title).text == "Add User"

    def click_user_role_select_admin(self):
        select_list = self.driver.find_elements(*self.select_list)
        user_role_select = select_list[0]
        user_role_select.click()
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Admin')]"))).click()
        # ActionChains(self.driver).key_down(Keys.DOWN).perform()
        # ActionChains(self.driver).click(user_role_select).perform()

    def click_status_select_enabled(self):
        select_list = self.driver.find_elements(*self.select_list)
        status_select = select_list[1]
        status_select.click()
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Enabled')]"))).click()
        # ActionChains(self.driver).key_down(Keys.DOWN).perform()
        # ActionChains(self.driver).click(status_select).perform()

    def fill_employee_name(self):
        employee_name = self.driver.find_element(*self.employee_name)
        # employee_name.click()
        ActionChains(self.driver).click(employee_name).send_keys('James Butler').perform()
        # employee_name.send_keys('James Butler')

        WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'James  Butler')]"))).click()

    def fill_username(self):
        input_list = self.driver.find_elements(*self.input_list)
        input_username = input_list[1]
        # input_username.send_keys('A. James Jr. '+datetime.now().strftime("%H-%M-%S"))
        input_username.send_keys('James Jr. ')
        self.fake.name()

    def fill_random_username(self):
        input_list = self.driver.find_elements(*self.input_list)
        input_username = input_list[1]
        input_username.send_keys('A. '+self.fake.name())

    def fill_password(self):
        input_list = self.driver.find_elements(*self.input_list)
        input_username = input_list[1]
        input_username.send_keys('Teste123')

    def fill_confirm_password(self):
        input_list = self.driver.find_elements(*self.input_list)
        input_username = input_list[2]
        input_username.send_keys('Teste123')

    def click_save(self):
        self.driver.find_element(*self.btn_save).click()
        
    def add_user_with_success(self):
        self.click_user_role_select_admin()
        self.click_status_select_enabled()
        self.fill_employee_name()
        self.fill_username()
        self.fill_password()
        self.fill_confirm_password()
        self.click_save()

    def add_random_user_with_success(self):
        self.click_user_role_select_admin()
        self.click_status_select_enabled()
        self.fill_employee_name()
        self.fill_random_username()
        self.fill_password()
        self.fill_confirm_password()
        self.click_save()