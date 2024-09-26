# from selenium.webdriver.common.by import By
import time

from pages.UserManagementPage import UserManagementPage
from pages.AddUserPage import AddUserPage

import logging

LOGGER = logging.getLogger(__name__)


class TestAddUser:
    
    def test_ct_001_adicionar_usuario(self, login_with_success):
        login_with_success.click_menu_admin()
        driver = login_with_success.get_driver()
        user_management_p = UserManagementPage(driver)
        assert user_management_p.is_title(), "Erro!!"
        user_management_p.click_btn_add()
        add_user_p = AddUserPage(driver)
        assert add_user_p.is_title(), "Erro!!"
        add_user_p.add_user_with_success()
        assert add_user_p.is_toast_visible(), "Erro! NAo encontrada mensagem de sucesso"


