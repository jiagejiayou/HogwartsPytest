import time

import pytest
import yaml

from weixin_appium.pages.app import App


with open("../datas/add_contact.yaml") as f:
    datas_add = yaml.safe_load(f)
with open("../datas/del_contact.yaml") as f:
    datas_del = yaml.safe_load(f)
class TestContact:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()
    def teardown_class(self):
        self.app.stop()
    def setup(self):
        self.app.start().goto_main()
    def teardown(self):
        self.app.back(5)

    @pytest.mark.skip
    @pytest.mark.parametrize("name,gender,phone",datas_add)
    def test_contactadd(self,name,gender,phone):
        # name = '阿尔法'
        # gender = '男'
        # phone = '15378946321'
        mypage = self.main.goto_contactlist().add_contact().add_manual().set_name(name).set_gender(gender).set_phone(phone).click_save()
        re = mypage.get_toast()
        assert '成功' in re
        self.app.back()

    @pytest.mark.parametrize("name", datas_del)
    def test_contactdel(self,name):

        self.main.goto_contactlist().search_contact(name).goto_edit_page().edit_member().del_member()