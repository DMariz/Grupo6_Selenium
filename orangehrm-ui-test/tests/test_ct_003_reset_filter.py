# from selenium.webdriver.common.by import By
import time
from webbrowser import Error

from pages.UserManagementPage import UserManagementPage

import logging

LOGGER = logging.getLogger(__name__)


class TestResetFilter:
    
    def test_ct_003_resetar_filtro_de_pesquisa_por_username(self, login_with_success):
        login_with_success.click_menu_admin()
        driver = login_with_success.get_driver()
        user_management_p = UserManagementPage(driver)
        assert user_management_p.is_title(), "Erro!!"
        # user_management_p.fill_username()
        user_management_p.fill_username_admin()
        user_management_p.click_reset()
        assert user_management_p.is_username_empty(), "Erro! Ainda preenchido!"

    # def test_ct_003_resetar_filtro_de_pesquisa_por_username(self, add_user):
    #     # login_with_success.click_menu_admin()
    #     # driver = login_with_success.get_driver()
    #     # user_management_p = UserManagementPage(driver)
    #     user_management_p = add_user
    #     assert user_management_p.is_title(), "Erro!!"
    #     user_management_p.fill_username()
    #     user_management_p.click_reset()
    #     assert user_management_p.is_username_empty(), "Erro! Ainda preenchido!"
