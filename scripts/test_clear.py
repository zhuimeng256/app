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

    def test_clear(self):
        self.page.page_me.click_setup()
        self.page.page_setup.click_clear()
        assert self.page.page_setup.is_exist_toast("清理成功")

