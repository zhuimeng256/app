from selenium.webdriver.common.by import By

from base.base import Base


class PageHome(Base):

    me = By.ID, "com.yunmall.lc:id/tab_me"
    category = By.ID, "com.yunmall.lc:id/tab_category"
    cart = By.ID, "com.yunmall.lc:id/tab_shopping_cart"
    search = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    def click_me(self):
        self.base_click(self.me)

    def login_if_not(self, page):
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        page.page_me_login.click_goto_login()
        page.page_login.input_username("itheima_test")
        page.page_login.input_pwd("itheima")
        page.page_login.click_login()

    def click_category(self):
        self.base_click(self.category)

    def click_cart(self):
        self.base_click(self.cart)

    def click_search(self):
        self.base_click(self.search)