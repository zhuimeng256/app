from selenium.webdriver.common.by import By

from base.base import Base


class PageMeLogin(Base):

    goto_login = By.ID, "com.yunmall.lc:id/textView1"


    def click_goto_login(self):
        self.base_click(self.goto_login)
