from selenium.webdriver.common.by import By

from base.base import Base


class PageAdress(Base):

    new_adress = By.ID, "com.yunmall.lc:id/address_add_new_btn"
    name_phone = By.ID, "com.yunmall.lc:id/receipt_name"
    default_address = By.ID, "com.yunmall.lc:id/address_is_default"
    edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
    remove = By.ID, "com.yunmall.lc:id/delete"
    confirm_remove = By.ID, "com.yunmall.lc:id/ymdialog_left_button"


    def click_new_adress(self):
        self.base_find_element_with_scroll(self.new_adress).click()

    def get_name_text(self):
        return self.base_get_text(self.name_phone)

    def is_exist_default(self):
        return self.base_is_exist_element(self.default_address)

    def click_default(self):
        self.base_click(self.default_address)

    def click_edit(self):
        self.base_click(self.edit)

    def click_remove(self):
        self.base_click(self.remove)

    def is_exist_remove(self):
        return self.base_is_exist_element(self.remove)

    def click_confirm_remove(self):
        self.base_click(self.confirm_remove)