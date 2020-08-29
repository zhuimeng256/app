from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class PageGooddetail(Base):

    add_cart = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
    confirm = By.ID, "com.yunmall.lc:id/select_detail_sure_btn"
    cart = By.ID, "com.yunmall.lc:id/btn_shopping_cart"
    good_title = By.ID, "com.yunmall.lc:id/tv_product_title"

    def click_add_cart(self):
        self.base_click(self.add_cart)

    def click_confirm(self):
        self.base_click(self.confirm)

    def get_choose_spec(self, text):
        return text.split(" ")[1]

    def click_spec(self):
        while True:
            self.click_confirm()
            if self.base_is_toast_exist("请选择"):
                spec_name = self.get_choose_spec(self.base_get_toast("请选择"))
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.base_click(spec_feature)
                sleep(2)
            else:
                break
    def click_cart(self):
        self.base_find_element_with_scroll(self.cart).click()

    def get_good_title(self):
        return self.base_get_text(self.good_title)

    def find_element_cart(self):
        self.base_find(self.cart)

