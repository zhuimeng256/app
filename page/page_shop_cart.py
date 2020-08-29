from selenium.webdriver.common.by import By

from base.base import Base


class PageShopcart(Base):

    edit = By.ID, "com.yunmall.lc:id/tv_right_second"
    add = By.ID, "com.yunmall.lc:id/iv_add"
    all_select = By.ID, "com.yunmall.lc:id/iv_select_all"
    all_price = By.ID, "com.yunmall.lc:id/tv_count_money"
    simple_price = By.ID, "com.yunmall.lc:id/tv_price"
    delete = By.ID, "com.yunmall.lc:id/tv_del_all"
    del_confirm = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
    empty_tip = By.ID, "com.yunmall.lc:id/tv_empty_tip"


    def is_goods_title_exist(self, title):
        title_xpath = By.XPATH, "//*[@text='%s']" % title
        return self.base_is_exist_element(title_xpath)

    def click_edit(self):
        self.base_click(self.edit)

    def click_add(self):
        self.base_click(self.add)

    def click_all_select(self):
        self.base_click(self.all_select)

    def get_all_price(self):
        price = self.base_get_text(self.all_price)
        price = price.split(" ")[1]
        return float(price)

    def get_simple_price(self):
        price = self.base_get_text(self.simple_price)
        price = price.split(" ")[1]
        return float(price)

    def click_del_good(self):
        self.base_click(self.delete)

    def click_confirm_del(self):
        self.base_click(self.del_confirm)

    def get_empty_tip(self):
        return self.base_get_text(self.empty_tip)

    def is_exist_goods(self):
        return self.base_is_exist_element(self.empty_tip)
