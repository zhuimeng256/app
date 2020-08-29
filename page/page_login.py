from selenium.webdriver.common.by import By

from base.base import Base


class PageLogin(Base):

    login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
    login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_btn = By.ID, "com.yunmall.lc:id/logon_button"

    def input_username(self, x):
        self.base_input(self.login_username, x)

    def input_pwd(self, x):
        self.base_input(self.login_pwd, x)

    def click_login(self):
        self.base_click(self.login_btn)

    def is_exist_toast(self, message):
        return self.base_is_toast_exist(message)