import random
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class PageEditAdress(Base):

    name = By.ID, "com.yunmall.lc:id/address_receipt_name"
    phone = By.ID, "com.yunmall.lc:id/address_add_phone"
    detail_adress = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    postcode = By.ID, "com.yunmall.lc:id/address_post_code"
    default_adress = By.ID, "com.yunmall.lc:id/address_default"
    adress_provinve = By.ID, "com.yunmall.lc:id/address_province"
    area_feature = By.ID, "com.yunmall.lc:id/area_title"
    reverse = By.ID, "com.yunmall.lc:id/button_send"

    def input_name(self, x):
        self.base_input(self.name, x)

    def input_phone(self, x):
        self.base_input(self.phone, x)

    def input_detail_adress(self, x):
        self.base_input(self.detail_adress, x)

    def input_postcode(self, x):
        self.base_input(self.postcode, x)

    def click_default_adress(self):
        self.base_click(self.default_adress)

    def click_adress_province(self):
        self.base_click(self.adress_provinve)

    def choose_region(self):
        self.click_adress_province()
        sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有的可选你的省市区
            areas = self.base_finds(self.area_feature)
            # 所有的可选的个数
            areas_count = len(areas)
            # 随机数下标
            area_index = random.randint(0, areas_count - 1)
            # 获取随机的城市
            areas[area_index].click()

            sleep(1)
    def click_reverse(self):
        self.base_click(self.reverse)

    def is_exist_toast(self, x):
        return self.base_is_toast_exist(x)

