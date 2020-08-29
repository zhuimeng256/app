import sys

sys.path.append(r'D:\BaiduNetdiskDownload\app')
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

    def test_version(self):
        self.page.page_me.click_setup()
        self.page.page_setup.click_about()
        self.page.page_about.click_version()
        assert self.page.page_about.is_exist_toast("当前已是最新版本")

