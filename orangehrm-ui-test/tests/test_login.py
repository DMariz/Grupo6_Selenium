# from selenium.webdriver.common.by import By
import time

# from pages.login_page import Login_Page
# from pages.products_page import Products_Page

import logging

LOGGER = logging.getLogger(__name__)


class TestLogin:
    
    def test_login_with_success(self, login_with_success):
        LOGGER.info("====> Iniciando test_login_with_success...")
        assert login_with_success.has_side_panel(), "Erro: Nao encontrado o Painel Lateral de Menu do site!!"
        login_with_success.click
        LOGGER.info("==> Login realizado")
        LOGGER.info("====> Finalizando test_login_with_success com sucesso")
