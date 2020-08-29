from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self, driver):
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_finds(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_is_exist_element(self, x):
        try:
            self.base_find(x, 5, 0.5)
            return True
        except:
            return False

    def base_click(self, loc):
        self.base_find(loc).click()

    def base_input(self, loc, x):
        self.base_find(loc).send_keys(x)

    def base_get_text(self, loc):
        return self.base_find(loc).text

    def base_is_toast_exist(self, message):
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.base_find(message_xpath, 5, 0.1)
            return True
        except:
            return False

    def base_get_toast(self, message):
        if self.base_is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.base_find(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    def base_scroll_page_one(self, direction="up"):
        """
        滑动一次屏幕
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = height / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def base_find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找 某个元素的特征
        :param feature: 元素的特征
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.base_find(feature)
            except Exception:

                self.base_scroll_page_one(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    def base_press_back(self):
        self.driver.press_keycode(4)

