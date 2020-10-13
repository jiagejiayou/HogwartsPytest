from Selenium.Main import Main


class TestWait:
    def setup(self):
        main=Main()
        main.click_first_link().title()