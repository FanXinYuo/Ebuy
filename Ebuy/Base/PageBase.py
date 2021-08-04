from selenium import webdriver


class Base:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    def __init__(self, web):   # 初始化一个页面
        self.driver.get(web)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
