import random

from selenium.webdriver.common.by import By

from base.base import Base


class PageCategory(Base):

    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    def click_goods_list(self):
        goods_lists = self.base_finds(self.goods_list_button)
        goods_lists_count = len(goods_lists)
        goods_lists_index = random.randint(0, goods_lists_count - 1)
        goods_lists[goods_lists_index].click()