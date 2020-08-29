from selenium.webdriver.common.by import By

from base.base import Base


class PageSearch(Base):

    search_input = By.ID, "com.yunmall.lc:id/text_search_keyword"
    search_btn = By.ID, "com.yunmall.lc:id/button_search"
    back = By.ID, "com.yunmall.lc:id/btn_back"

    def input_search(self, x):
        self.base_input(self.search_input, x)

    def click_search_btn(self):
        self.base_click(self.search_btn)

    def is_keyword_exist(self, keyword):
        xpath = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        # xpath = By.XPATH, "//*[@text='%s']" % keyword
        return self.base_is_exist_element(xpath)

    def click_back(self):
        self.base_click(self.back)
