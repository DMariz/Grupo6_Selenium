
class Test1:

    def test_efetuar_login(self,open_browser):

        login_p = open_browser
        login_p.faz_login('Admin','admin123')

        assert login_p.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', "Login nao esta funcionando"


