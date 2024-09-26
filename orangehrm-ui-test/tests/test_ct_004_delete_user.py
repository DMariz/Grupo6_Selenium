# from selenium.webdriver.common.by import By
import time
from webbrowser import Error

# from pages.UserManagementPage import UserManagementPage

import logging

LOGGER = logging.getLogger(__name__)


class TestDeleteUser:
    
    # def test_ct_004_deletar_usuario(self, login_with_success):
    #     login_with_success.click_menu_admin()
    #     driver = login_with_success.get_driver()
    #     user_management_p = UserManagementPage(driver)
    #     assert user_management_p.is_title(), "Erro!!"
    #     user_management_p.fill_username()
    #     user_management_p.click_search()
    #     assert user_management_p.has_record_found(), "Erro! Nao encontrado"
    #     user_management_p.delete_first_record()
    #     assert user_management_p.is_toast_visible(), "Erro! Nao encontrada mensagem de sucesso"

    def test_ct_004_deletar_usuario(self, add_user):
        # login_with_success.click_menu_admin()
        # driver = login_with_success.get_driver()
        # user_management_p = UserManagementPage(driver)
        user_management_p = add_user
        assert user_management_p.is_title(), "Erro!!"
        user_management_p.fill_username()
        user_management_p.click_search()
        assert user_management_p.has_record_found(), "Erro! Nao encontrado"
        user_management_p.delete_first_record()
        assert user_management_p.is_toast_visible(), "Erro! Nao encontrada mensagem de sucesso"
