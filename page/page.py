from page.page_about import PageAbout
from page.page_adress_list import PageAdress
from page.page_category import PageCategory
from page.page_edit_adress import PageEditAdress
from page.page_good_detail import PageGooddetail
from page.page_goodlist import PageGoodlist
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_me import PageMe
from page.page_me_login import PageMeLogin
from page.page_search import PageSearch
from page.page_setup import PageSetup
from page.page_shop_cart import PageShopcart


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_home(self):
        return PageHome(self.driver)

    @property
    def page_login(self):
        return PageLogin(self.driver)

    @property
    def page_me_login(self):
        return PageMeLogin(self.driver)

    @property
    def page_me(self):
        return PageMe(self.driver)

    @property
    def page_setup(self):
        return PageSetup(self.driver)

    @property
    def page_about(self):
        return PageAbout(self.driver)

    @property
    def page_adress(self):
        return PageAdress(self.driver)

    @property
    def page_edit_adress(self):
        return PageEditAdress(self.driver)

    @property
    def page_category(self):
        return PageCategory(self.driver)

    @property
    def page_goodlist(self):
        return PageGoodlist(self.driver)

    @property
    def page_gooddetail(self):
        return PageGooddetail(self.driver)

    @property
    def page_shopcart(self):
        return PageShopcart(self.driver)

    @property
    def page_search(self):
        return PageSearch(self.driver)