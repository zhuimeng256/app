import sys

sys.path.append(r'D:\BaiduNetdiskDownload\app')
import pytest
from page.page import Page

from time import sleep
from base.read_yaml import analyze_file
from base.get_driver import get_driver



class TestLogin:

    def setup(self):
        self.driver = get_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        self.page.page_home.click_me()
        self.page.page_me_login.click_goto_login()
        self.page.page_login.input_username(username)
        self.page.page_login.input_pwd(password)
        self.page.page_login.click_login()
        if toast is None:
            assert self.page.page_me.get_username() == username
        else:
            assert self.page.page_login.is_exist_toast(toast)
