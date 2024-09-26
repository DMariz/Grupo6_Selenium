import pytest

from pages.loginPage import LoginPage

def pytest_addoption(parser):
    parser.addoption("--browser",default='chrome',help='Select browser to run tests.')


@pytest.fixture
def open_browser(request):
    selected_browser = request.config.getoption('browser').lower()
    login_p = LoginPage(browser=selected_browser)
    login_p.open_login()
    yield login_p
    login_p.close()


@pytest.fixture
def login_orangehrm(open_browser):

    login_p = open_browser
    login_p.faz_login('Admin','admin123')

    yield login_p.driver