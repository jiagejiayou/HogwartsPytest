from Selenium.test_wework_login.index_po import Index
class TestRegister:
    def setup(self):
        self.index = Index()
    def test_register(self):
        result = self.index.goto_register().register()
        assert result