from Ebuy.Base.PageObject import PageObject
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, url):
        # 打开易买网的网页
        self.web = PageObject(url)

    def login(self):
        self.web.driver.implicitly_wait(5)    # 隐式等待5s
        self.web.click(By.LINK_TEXT, "登录")
        self.web.send_key(By.ID, "loginName", value='admin')
        self.web.send_key(By.ID, "password", value='123456')
        self.web.click(By.CLASS_NAME, "log_btn")
        return self.web
