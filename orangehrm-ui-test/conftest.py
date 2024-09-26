import logging
import time
import pytest
from pages.LoginPage import Login_Page
from pages.UserManagementPage import UserManagementPage
from pages.AddUserPage import AddUserPage

LOGGER = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default="chrome", help="Select browser option")

@pytest.fixture(autouse=True)
def setup_scope():
    LOGGER.info("====> Config Iniciais... <==== ")

@pytest.fixture
def open_browser(request):
    LOGGER.info("====> Inciando execucao...")
    selected_browser = request.config.getoption('browser_selenium').lower()
    login_page = Login_Page(browser=selected_browser)
    login_page.open()
    yield login_page
    LOGGER.info("====> Encerrando execucao...")
    login_page.close()
    
@pytest.fixture
def login_with_success(open_browser):
    LOGGER.info("====> Iniciando login_with_success - orangehrmlive...")
    login_page = open_browser
    login_page.login_with_admin_user()
    time.sleep(3)
    LOGGER.info("====> Finalizando click_login_button com sucesso - orangehrmlive")
    yield login_page

@pytest.fixture
def add_two_random_users(login_with_success):
    LOGGER.info("====> add_two_random_users... first...")
    login_with_success.click_menu_admin()
    driver = login_with_success.get_driver()
    user_management_p = UserManagementPage(driver)
    user_management_p.click_btn_add()
    add_user_p = AddUserPage(driver)
    add_user_p.add_random_user_with_success()
    try:
        user_management_p.is_checkbox_first_record_exists()
    except Exception:
        print("Nao econtrado")
    LOGGER.info("====> add_two_random_users")
    LOGGER.info("====> add_two_random_users... second...")
    login_with_success.click_menu_admin()
    driver = login_with_success.get_driver()
    user_management_p = UserManagementPage(driver)
    user_management_p.click_btn_add()
    add_user_p = AddUserPage(driver)
    add_user_p.add_random_user_with_success()
    try:
        user_management_p.is_checkbox_first_record_exists()
    except Exception:
        print("Nao econtrado")
    LOGGER.info("====> add_two_random_users")
    yield user_management_p

@pytest.fixture
def add_user(login_with_success):
    LOGGER.info("====> add_user... first...")
    login_with_success.click_menu_admin()
    driver = login_with_success.get_driver()
    user_management_p = UserManagementPage(driver)
    user_management_p.click_btn_add()
    add_user_p = AddUserPage(driver)
    add_user_p.add_user_with_success()
    try:
        add_user_p.is_toast_visible()
        user_management_p.is_checkbox_first_record_exists()
    except Exception:
        print("Nao econtrado")
    LOGGER.info("====> add_user")
    yield user_management_p