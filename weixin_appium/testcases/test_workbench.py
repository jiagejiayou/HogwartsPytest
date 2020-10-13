from weixin_appium.pages.app import App


class TestWorkbench:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()
    def teardown_class(self):
        self.app.stop()
    def setup(self):
        self.app.start().goto_main()
    def teardown(self):
        self.app.back(5)

    def test_daka(self):
        re = self.main.goto_workbench().goto_daka().daka_task().out_daka().is_success()
        assert '打卡成功' in re
        self.app.back()