import random

from selenium.webdriver.common.by import By

from base.base import Base


class PageGoodlist(Base):

    goods_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    def click_good(self):
        goods = self.base_finds(self.goods_button)
        n = random.randint(0, len(goods)-1)
        goods[n].click()