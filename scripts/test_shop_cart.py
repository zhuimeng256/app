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


    def test_add_shop_cart(self):
        self.page.page_home.click_category()
        self.page.page_category.click_goods_list()
        self.page.page_goodlist.click_good()
        good_title = self.page.page_gooddetail.get_good_title()
        self.page.page_gooddetail.click_add_cart()
        self.page.page_gooddetail.click_spec()

        self.page.page_gooddetail.find_element_cart()
        self.page.page_gooddetail.click_cart()
        self.page.page_shopcart.is_goods_title_exist(good_title)

    def test_shop_cart_price(self):
        self.page.page_home.click_cart()
        price = self.page.page_shopcart.get_simple_price()
        self.page.page_shopcart.click_all_select()
        all_price = self.page.page_shopcart.get_all_price()
        self.page.page_shopcart.click_edit()
        self.page.page_shopcart.click_add()
        self.page.page_shopcart.click_edit()
        new_price = self.page.page_shopcart.get_all_price()
        assert new_price == all_price + price

    def test_del_shop_cart(self):
        self.page.page_home.click_cart()
        if self.page.page_shopcart.is_exist_goods():
            self.page.page_home.click_category()
            self.page.page_category.click_goods_list()
            self.page.page_goodlist.click_good()
            self.page.page_gooddetail.click_add_cart()
            self.page.page_gooddetail.click_spec()

            self.page.page_gooddetail.find_element_cart()
            self.page.page_gooddetail.click_cart()
        self.page.page_shopcart.click_edit()
        self.page.page_shopcart.click_all_select()
        self.page.page_shopcart.click_del_good()
        self.page.page_shopcart.click_confirm_del()
        assert self.page.page_shopcart.get_empty_tip().find("购物车还是空的") != -1
