from selenium.webdriver.common.by import By

from base.base import Base


class PageMe(Base):

    username = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    set_up = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    take_part_in =By.ID, "android.widget.RelativeLayout"

    def get_username(self):
        return self.base_get_text(self.username)

    def click_setup(self):
        self.base_click(self.set_up)

    def click_take_part(self):
        self.base_click(self.take_part_in)

