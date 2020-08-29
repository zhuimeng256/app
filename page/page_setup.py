from selenium.webdriver.common.by import By

from base.base import Base


class PageSetup(Base):

    about = By.ID, "com.yunmall.lc:id/setting_about_yunmall"
    clear = By.ID, "com.yunmall.lc:id/setting_clear_cache"
    site = By.ID, "com.yunmall.lc:id/setting_address_manage"

    def click_about(self):
        self.base_find_element_with_scroll(self.about).click()

    def click_clear(self):
        self.base_click(self.clear)

    def is_exist_toast(self, x):
        return self.base_is_toast_exist(x)

    def click_adress(self):
        self.base_click(self.site)

