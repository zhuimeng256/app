from appium import webdriver


def get_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '127.0.0.1:7555'
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # toast
    desired_caps['automationName'] = 'Uiautomator2'
    # 是否重置应用 True:不重置 False:重置
    desired_caps['noReset'] = no_reset

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
