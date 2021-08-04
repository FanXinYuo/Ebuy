from Ebuy.Base.PageBase import Base
from selenium.common.exceptions import NoSuchElementException


class PageObject(Base):
    # *代表可以接收任意多个非关键字参数
    # 查找元素
    def find(self, *args):
        try:
            return self.driver.find_element(*args)
        except NoSuchElementException:
            print("定位失败")

    # 点击动作
    def click(self, *args):
        self.find(*args).click()

    # 清除
    def clear(self, *args):
        self.find(*args).clear()

    # 输入
    def send_key(self, *args, value):
        self.find(*args).send_keys(value)

    # 获取文本
    def text(self, *args):
        return self.find(*args).text

    # 操作滚动条
    def js(self, row, col):
        string = 'window.scrollTo('+str(row)+','+str(col)+')'
        self.driver.execute_script(string)

    # 获取URL的方法
    def get_url(self):
        return self.driver.current_url

    # 后退的回退
    def back(self):
        self.driver.back()

    # 前进的方法
    def forward(self):
        self.driver.forward()

    # 关闭的浏览器与驱动的方法
    def quit(self):
        self.driver.quit()

    # 切换默认frame
    def default_frame(self):
        self.driver.switch_to.default_content()

    # 获取所有frame
    def get_all_frame(self):
        return self.driver.find_elements_by_tag_name("frame")

    # 切换frame
    def switch_frame(self, frame, i):
        self.driver.switch_to.frame(frame[i])

    # 获取警示框文本
    def alert_text(self):
        return self.driver.switch_to.alert.text

    # 接收警示框
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    # 获取一组元素
    def get_elements(self, *args):
        return self.driver.find_elements(*args)

    # 截图
    def screenshot(self, post, name):
        self.driver.get_screenshot_as_file(post+name)

    # 判断元素是否存在
    def element_exists(self, *args):
        try:
            self.driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False