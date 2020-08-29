import sys
sys.path.append(r'D:\BaiduNetdiskDownload\app')

from base.read_yaml import analyze_file


import pytest
from page.page import Page

from time import sleep
from base.get_driver import get_driver



class TestLogin:

    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)
        self.page.page_home.login_if_not(self.page)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]

        self.page.page_me.click_setup()
        self.page.page_setup.click_adress()
        self.page.page_adress.click_new_adress()
        self.page.page_edit_adress.input_name(name)
        self.page.page_edit_adress.input_phone(phone)
        self.page.page_edit_adress.input_detail_adress(info)
        self.page.page_edit_adress.input_postcode(post_code)
        self.page.page_edit_adress.click_default_adress()
        self.page.page_edit_adress.choose_region()
        self.page.page_edit_adress.click_reverse()
        if toast is None:
            assert self.page.page_adress.get_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.page_edit_adress.is_exist_toast(toast)

    def test_edit_address(self):
        self.page.page_me.click_setup()
        self.page.page_setup.click_adress()
        if not self.page.page_adress.is_exist_default():
            self.page.page_adress.click_new_adress()
            self.page.page_edit_adress.input_name("zhangsan")
            self.page.page_edit_adress.input_phone("18888888888")
            self.page.page_edit_adress.input_detail_adress("三单元 504")
            self.page.page_edit_adress.input_postcode("100000")
            self.page.page_edit_adress.click_default_adress()
            self.page.page_edit_adress.choose_region()
            self.page.page_edit_adress.click_reverse()
        self.page.page_adress.click_default()
        self.page.page_edit_adress.input_name("李四")
        self.page.page_edit_adress.input_phone("18888888888")
        self.page.page_edit_adress.input_detail_adress("三单元 504")
        self.page.page_edit_adress.input_postcode("100000")
        self.page.page_edit_adress.choose_region()
        self.page.page_edit_adress.click_reverse()
        assert self.page.page_adress.base_is_toast_exist("保存成功")

    def test_delete_address(self):
        self.page.page_me.click_setup()
        self.page.page_setup.click_adress()
        assert self.page.page_adress.is_exist_default()

        for i in range(10):
            self.page.page_adress.click_edit()
            if not self.page.page_adress.is_exist_remove():
                break
            self.page.page_adress.click_remove()
            self.page.page_adress.click_confirm_remove()
        self.page.page_adress.click_edit()
        assert not self.page.page_adress.is_exist_remove()
