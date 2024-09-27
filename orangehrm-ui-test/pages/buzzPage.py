import time
from time import sleep

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# from pages.base import Base
from .basePage import Base


class BuzzPage(Base):
    url_buzzfeeds = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    botao_buzz = (By.XPATH, '//*[contains(@href, "/buzz/viewBuzz")]')
    field_text_post = (By.CLASS_NAME, "oxd-buzz-post-input")

    post_button =  (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--main')

    tri_dot = (By.CLASS_NAME, 'bi-three-dots')
    delete_icon = (By.CLASS_NAME, 'bi-trash')
    edit_icon = (By.CLASS_NAME, 'bi-pencil')
    comment_icon =(By.CLASS_NAME, 'bi-chat-text-fill')
    post_heart = (By.ID, 'heart')
    share_icon =(By.CLASS_NAME, "bi-share-fill")

    post = (By.CLASS_NAME, 'oxd-grid-item--gutters')

    post_text = (By.CLASS_NAME, 'orangehrm-buzz-post-body-text')
    toast = (By.CSS_SELECTOR, 'div.oxd-toast-container.oxd-toast-container--bottom')
    
    #infelizmente tem que usar o xpath pra pegar o texto de likes, pois nao tem id nem classe unica
    like_text = (By.XPATH, './/i[contains(@class, "orangehrm-buzz-stats-like-icon")]/following-sibling::p')
    comment_field =(By.CLASS_NAME, 'oxd-input')

    delete_dialog =(By.CLASS_NAME, 'orangehrm-dialog-popup')
    dialog = (By.CLASS_NAME, 'orangehrm-dialog-modal')

    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver=driver)
        self.go_to_buzzfeeds()

    def go_to_buzzfeeds(self):
        self.wait_element(self.botao_buzz).click()

    def is_url_buzzfeeds(self):
        return self.is_url(self.url_buzzfeeds)

    def create_post(self, text_post):
        self.wait_element(self.field_text_post).send_keys(text_post)
        self.wait_element(self.post_button).click()

    def like_lastest_post(self):
        like_button = self.wait_element(self.post_heart)
        like_button.click()

    def get_lastest_like(self):
        try:

            # Encontra o texto de likes dentro do primeiro post
            like_count_element = self.wait_element(self.post).find_element(*self.like_text)

            # Retorna o texto dos likes
            return like_count_element.text.strip()

        except NoSuchElementException:
            return "0 Likes"
        except TimeoutException:
            return "ERRO TIMEOUT"

    def comment_lastest(self, text_comment):
        #Pega o primeiro post
        post_element = self.wait_element(self.post)

        #Clica no icone de Comentar
        post_element.find_element(*self.comment_icon).click()

        #Aguarda campo para escrever
        field = post_element.find_element(*self.comment_field)

        #Escreve o texto
        field.send_keys(text_comment)

        #Pressiona Enter
        field.send_keys(Keys.ENTER)



    def get_latest_post_text(self):
        try:
          return self.wait_element(self.post_text).text.strip()
        except NoSuchElementException:
            return 'Nao tem post'
        except TimeoutException:
            return 'Timeout: Não foi possível localizar o post'


    def is_toast_visible(self):
        try:
            self.wait_element(self.toast, timeout=5)
            return True
        except NoSuchElementException:
            return False

    def first_tridot(self):

        # Provavelmente pega todos os tri-dots
        return self.wait_element(self.tri_dot, timeout=10)


    # Verifica se o diálogo de confirmação está visível
    def is_delete_dialog_visible(self):

        return self.wait_element(self.dialog_selector, timeout=5)

    def delete_latest_post(self):

        self.first_tridot().click()

        #Pega onde ta icon da lixeira
        self.wait_element(self.delete_icon, timeout=10).click()

        self.wait_element(self.delete_dialog).find_element(*self.delete_icon).click()

    def edit_latest_post(self,edit_text):

        self.first_tridot().click()

        #Pega onde ta icon da lapis
        self.wait_element(self.edit_icon, timeout=10).click()

        #Escreve DENTRO dialogo que abriu
        self.wait_element(self.dialog).find_element(*self.field_text_post).send_keys(edit_text)

        #Aperta no botão de postar DENTRO do dialogo
        self.wait_element(self.dialog).find_element(*self.post_button).click()

    def share_latest_post(self,share_text):
        # Clica no icone de compartilhar
        self.wait_element(self.share_icon).click()

        #Escreve DENTRO do dialogo que abriu
        self.wait_element(self.dialog).find_element(*self.field_text_post).send_keys(share_text)

        # Aperta no botão de postar DENTRO do dialogo
        self.wait_element(self.dialog).find_element(*self.post_button).click()