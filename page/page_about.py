from selenium.webdriver.common.by import By

from base.base import Base


class PageAbout(Base):

    version = By.ID, "com.yunmall.lc:id/about_version_update"

    def click_version(self):
        self.base_click(self.version)

    def is_exist_toast(self, x):
        return self.base_is_toast_exist(x)