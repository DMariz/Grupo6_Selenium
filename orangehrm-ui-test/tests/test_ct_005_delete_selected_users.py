# from selenium.webdriver.common.by import By
import time
from webbrowser import Error

from pages.UserManagementPage import UserManagementPage

import logging

LOGGER = logging.getLogger(__name__)


class TestDeleteSelectedUser:
    
    # def test_ct_005_deletar_usuarios_selecionados(self, login_with_success):
    #     login_with_success.click_menu_admin()
    #     driver = login_with_success.get_driver()
    #     user_management_p = UserManagementPage(driver)
    #     assert user_management_p.is_title(), "Erro!!"
    #     user_management_p.delete_multiple_records()
    #     assert user_management_p.is_toast_visible(), "Erro! Nao encontrada mensagem de sucesso"

    def test_ct_005_deletar_usuarios_selecionados(self, add_two_random_users):
        # login_with_success.click_menu_admin()
        # driver = login_with_success.get_driver()
        user_management_p = add_two_random_users
        assert user_management_p.is_title(), "Erro!!"
        user_management_p.delete_multiple_records()
        assert user_management_p.is_toast_visible(), "Erro! Nao encontrada mensagem de sucesso"
