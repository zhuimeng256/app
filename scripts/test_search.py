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
        # self.page.page_home.login_if_not(self.page)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_search(self):
        self.page.page_home.click_search()
        self.page.page_search.input_search("nike")
        self.page.page_search.click_search_btn()
        self.page.page_search.click_back()
        assert self.page.page_search.is_keyword_exist("nike")