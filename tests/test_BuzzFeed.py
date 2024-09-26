import time

import pytest
from pages.buzzPage import BuzzPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBuzz:
    def test_inserir_post_texto(self, open_browser):
        #. . . TESTE CRIAR POST ,  CT-006 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        # Cria um post com "Hello World!"
        buzz_page.create_post("Hello World!")

        # Verifica se o toast apareceu
        assert buzz_page.is_toast_visible(), "O toast de confirmação não apareceu"

        # Força uma atualização da página
        buzz_page.driver.refresh()

        # Obtém o texto do post mais recente
        latest_post = buzz_page.get_latest_post_text()

        # Faz assert para verificar se o post mais recente tem o texto "Hello World!"
        assert latest_post.strip() == "Hello World!", "O post mais recente não é 'Hello World!'"


    def test_comment_post(self, open_browser):
        # . . . CASO TESTE DE LIKE CT-007 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        #Clica no Icone, Escreve no campo e Apertar Enter
        buzz_page.comment_lastest("Comentário teste")

        # Verifica se o toast apareceu
        assert buzz_page.is_toast_visible(), "O toast de confirmação não apareceu"


    def test_like_post(self, open_browser):
        # . . . CASO TESTE DE LIKE CT-008 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        #Guarda o Estado do like antes de dar like
        liked = buzz_page.get_lastest_like()

        #Dar like
        buzz_page.like_lastest_post()

        #INFELIZMENTE ELE PRECISA DO TIME.SLEEP, POIS A ANIMAÇÃO É MUITO LENTA
        time.sleep(2)

        new_liked = buzz_page.get_lastest_like()

        #Verifica a qtd de likes
        assert abs(int(new_liked.split()[0]) - int(liked.split()[0])) == 1, "Não contabilizou o like"


    def test_editar_post(self, open_browser):
        # . . . CASO TESTE DE EDITAR CT-010 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        # Obtém o texto do post que será deletado
        post_text = buzz_page.get_latest_post_text()

        # Edita o post
        edited_text = "This was edited"
        buzz_page.edit_latest_post(edited_text)

        # Verifica se o toast de confirmação apareceu
        assert buzz_page.is_toast_visible(), "O toast de confirmação não apareceu após deletar"

        # Força uma atualização da página
        #buzz_page.driver.refresh()

        # Verifica se o post não está mais presente
        assert buzz_page.get_latest_post_text() == post_text + edited_text, "O post parece não ter sido editado"

    def test_share_post(self, open_browser):
        # . . . CASO TESTE DE EDITAR CT-011 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        # Edita o post
        shared_text = "This is nice! I'm sharing it"
        buzz_page.share_latest_post(shared_text)

        # Verifica se o toast de confirmação apareceu
        assert buzz_page.is_toast_visible(), "O toast de confirmação não apareceu após deletar"

        # Força uma atualização da página
        buzz_page.driver.refresh()

        assert buzz_page.get_latest_post_text() == shared_text, "O compartilhamento não pareceu"

    def test_deletar_post(self, open_browser):

        # . . . CASO TESTE DE DELETAR CT-009 . . .

        login_p = open_browser
        login_p.faz_login('Admin', 'admin123')

        # Instancia a classe BuzzPage
        buzz_page = BuzzPage(driver=login_p.driver)

        # Verifica se está na página Buzz
        assert buzz_page.is_url_buzzfeeds(), "Não está na página Buzz"

        # Obtém o texto do post que será deletado
        post_text = buzz_page.get_latest_post_text()

        # Deleta o post
        buzz_page.delete_latest_post()

        # Verifica se o toast de confirmação apareceu
        assert buzz_page.is_toast_visible(), "O toast de confirmação não apareceu após deletar"

        # Força uma atualização da página
        #buzz_page.driver.refresh()

        # Verifica se o post não está mais presente
        assert not buzz_page.get_latest_post_text() == post_text, "O post ainda está presente após deletar"