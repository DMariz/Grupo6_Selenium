from .basePage import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

LOGGER = logging.getLogger(__name__)

class UserManagementPage(Base):

    title = (By.CLASS_NAME, 'oxd-topbar-header-breadcrumb-level')
    btn_add = (By.CLASS_NAME, 'oxd-button-icon')
    username = (By.CSS_SELECTOR, 'div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > input')
    btn_search = (By.CLASS_NAME, 'orangehrm-left-space')
    record_found_label = (By.CLASS_NAME, 'orangehrm-vertical-padding')
    btn_reset = (By.CLASS_NAME, 'oxd-button--ghost')
    chk_records = (By.CLASS_NAME, 'bi-check')
    btn_trash = (By.CLASS_NAME, 'oxd-icon.bi-trash')
    btn_deleted_selected = (By.CLASS_NAME, 'bi-trash-fill')
    btn_yes_selected = (By.CLASS_NAME, 'oxd-button--label-danger.orangehrm-button-margin')

    def __init__(self, driver):
        super(UserManagementPage, self).__init__(driver=driver)

    def is_title(self):
        return self.driver.find_element(*self.title).text == "User Management"

    def click_btn_add(self):
        self.driver.find_element(*self.btn_add).click()

    def fill_username(self):
        self.driver.find_element(*self.username).send_keys("James Jr.")
        # print("\n==> Texto username: "+self.driver.find_element(*self.username).text)

    def fill_username_admin(self):
        self.driver.find_element(*self.username).send_keys("Admin")

    def click_search(self):
        self.driver.find_element(*self.btn_search).click()

    def has_record_found(self):
        self.wait_element(self.record_found_label, 10)
        for i in range(180):
            if not self.driver.find_element(*self.record_found_label).text == "(1) Record Found":
                continue
            else:
                return True
        return False

    def click_reset(self):
        self.driver.find_element(*self.btn_reset).click()

    def is_username_empty(self):
        return self.driver.find_element(*self.username).text == ""

    def is_checkbox_first_record_exists(self):
        try:
            self.wait_element(self.chk_records, timeout=10)
            return True
        except NoSuchElementException:
            return False

    def click_checkbox_first_record(self):
        self.driver.find_elements(*self.chk_records)[1].click()

    def click_btn_deleted_selected(self):
        self.driver.find_element(*self.btn_deleted_selected).click()

    def click_btn_trash(self):
        self.driver.find_element(*self.btn_trash).click()

    def click_btn_yes_selected(self):
        self.driver.find_element(*self.btn_yes_selected).click()

    def delete_first_record(self):
        self.click_btn_trash()
        self.click_btn_yes_selected()

    def delete_multiple_records(self):
        self.driver.find_elements(*self.chk_records)[1].click()
        self.driver.find_elements(*self.chk_records)[2].click()
        self.click_btn_deleted_selected()
        self.click_btn_yes_selected()

