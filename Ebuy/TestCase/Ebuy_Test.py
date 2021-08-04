import unittest
from Ebuy.PageObject.Login import Login
from Ebuy.DataBase.DatabaseExecute import DatabaseExecute
from selenium.webdriver.common.by import By
from Ebuy.PageObject.ItemUpshelf import item_up_shelf
import math
import random
from Ebuy.Common.Logger import Logger
lg = Logger('Ebuy').get_log()

class Ebuy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 打开网页
        Ebuy.webpage = Login("http://localhost:8080/ebuy")
        Ebuy.pageobject = Ebuy.webpage.login()
        Ebuy.database = DatabaseExecute('127.0.0.1', 'root', '123456', 'easybuy')
        Ebuy.pageobject.click(By.LINK_TEXT, "后台管理")

    def test_itemupshelf_01(self):
        """全填，且均正确填写"""
        lg.info("商品上架-1-全部正确填写")
        flag = list('111111111111')
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '01', flag, lg)

    def test_itemupshelf_02(self):
        """全不填"""
        lg.info("商品上架-2-全不填")
        flag = '000000000000'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '02', flag, lg)

    def test_itemupshelf_03(self):
        """只填必填项：一级分类、商品名称、价格、库存，且均正确填写"""
        lg.info("商品上架-3-只正确填写必填项：一级分类、商品名称、价格、库存")
        flag = '100110011110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '03', flag, lg)

    def test_itemupshelf_04(self):
        """填非必填项：上传正确格式的商品图片，并填写描述"""
        lg.info("商品上架-4-填非必填项：上传正确格式的商品图片，并填写描述")
        flag = '000001100001'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '04', flag, lg)

    def test_itemupshelf_05(self):
        """填非必填项：选择一、二级分类"""
        lg.info("商品上架-5-填非必填项：选择一、二级分类")
        flag = '110000000000'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '05', flag, lg)

    def test_itemupshelf_06(self):
        """填非必填项：选择一、二、三级分类"""
        lg.info("商品上架-6-填非必填项：选择一、二、三级分类")
        flag = '111000000000'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '06', flag, lg)

    def test_itemupshelf_07(self):
        """必填项除名称均正确填写，名字超长17个字符"""
        lg.info("商品上架-7-必填项除名称均正确填写，名字超长17个字符")
        flag = '100120011110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '07', flag, lg)

    def test_itemupshelf_08(self):
        """必填项除名称均正确填写，名字1个字符"""
        lg.info("商品上架-8-必填项除名称均正确填写，名字1个字符")
        flag = '100130011110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '08', flag, lg)

    def test_itemupshelf_09(self):
        """必填项除名称均正确填写，名字含特殊字符空格"""
        lg.info("商品上架-9-必填项除名称均正确填写，名字含特殊字符空格")
        flag = '100140011110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '09', flag, lg)

    def test_itemupshelf_10(self):
        """必填项均正确填写，商品图片格式错误"""
        lg.info("商品上架-10-必填项均正确填写，商品图片格式错误")
        flag = '100111211110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '10', flag, lg)

    def test_itemupshelf_11(self):
        """必填项均正确填写，单价格式错误，非数字"""
        lg.info("商品上架-11-必填项均正确填写，单价格式错误，非数字")
        flag = '100111112110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '11', flag, lg)

    def test_itemupshelf_12(self):
        """必填项均正确填写，单价格式错误，三位小数"""
        lg.info("商品上架-12-必填项均正确填写，单价格式错误，三位小数")
        flag = '100111113110'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '12', flag, lg)

    def test_itemupshelf_13(self):
        """必填项均正确填写，库存格式错误，非数字"""
        lg.info("商品上架-13-必填项均正确填写，库存格式错误，非数字")
        flag = '100111111120'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '13', flag, lg)

    def test_itemupshelf_14(self):
        """必填项均正确填写，库存格式错误，非整数"""
        lg.info("商品上架-14-必填项均正确填写，库存格式错误，非整数")
        flag = '100111111120'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '14', flag, lg)

    def test_itemupshelf_15(self):
        """插入重复数据"""
        lg.info("商品上架-15-重复数据的插入")
        flag = '重复'
        item_up_shelf(Ebuy.pageobject, Ebuy.database, '15', flag, lg)

    def test_message_cilck_01(self):
        """任意点击一条资讯标题"""
        lg.info("资讯中心-1-任意点击一条资讯标题")
        Ebuy.pageobject.driver.implicitly_wait(5)  # 隐式等待5s
        # 切换资讯列表
        Ebuy.pageobject.click(By.LINK_TEXT, "资讯列表")
        # 获取资讯标题
        element = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')
        # 随机点击一条资讯
        i = random.randint(0, len(element) - 1)
        element[i].click()
        if Ebuy.pageobject.element_exists(By.CLASS_NAME, 'mem_tit'):
            lg.info("点击任意一条资讯标题，可成功切换！")
        assert Ebuy.pageobject.element_exists(By.CLASS_NAME, 'mem_tit'), lg.info("点击任意一条资讯标题，未切换成功！")

    def test_message_data_match_02(self):
        """页面资讯条数是否与数据库一致"""
        lg.info("资讯中心-2-页面资讯条数是否与数据库一致")
        Ebuy.pageobject.driver.implicitly_wait(5)  # 隐式等待5s
        # 切换资讯列表
        Ebuy.pageobject.click(By.LINK_TEXT, "资讯列表")
        # 获取页码元素
        element = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 点击【尾页】
        element[len(element) - 1].click()
        # 重新获取页面元素
        element1 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 总页码数 element1[len(element1)-2].text
        # 查询数据库中存在的资讯条数
        res = Ebuy.database.selectdate("select count(*) from easybuy_news")
        if math.ceil(res[0][0] / 10) == int(element1[len(element1) - 2].text):
            lg.info("资讯条数与数据库中存在条数匹配")
        assert math.ceil(res[0][0] / 10) == int(element1[len(element1) - 2].text), "资讯条数与数据库中存在条数不匹配"


    def test_message_switch_page_03(self):
        """页面切换功能是否正常"""
        lg.info("资讯中心-3-页面切换功能是否正常")
        Ebuy.pageobject.driver.implicitly_wait(5)  # 隐式等待5s
        # 切换资讯列表
        Ebuy.pageobject.click(By.LINK_TEXT, "资讯列表")
        # 获取页码元素
        element = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 获取页码1的第一个资讯标题
        title = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')[0].text
        # 点击页码【2】
        element[2].click()
        # 重新获取页码元素
        element1 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 获取页码2的第一个资讯标题
        title1 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')[0].text
        assert title != title1, "页面未切换成功，展示内容未发生改变"
        # 点击页码【3】
        element1[4].click()
        # 获取页码元素
        element2 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 获取页码3的第一个资讯标题
        title2 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')[0].text
        assert title2 != title1 and title2 != title1, "页面未切换成功，展示内容未发生改变"
        # 点击页码【上一页】，到页码【2】
        element2[1].click()
        # 获取页码元素
        element3 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 获取该页码中第一条资讯标题
        title3 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')[0].text
        assert title3 == title1, "页面切换存在问题，页码2中的内容发生改变"
        # 点击页码【下一页】，回到页码3
        element3[len(element3) - 2].click()
        # 获取页码3中第一条资讯标题
        title4 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'tbody>tr>td>a')[0].text
        assert title2 == title4, "页码切换存在问题，页码3中的内容发生改变"
        # 获取页码元素
        element4 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 点击【首页】
        element4[0].click()
        # time.sleep(1)
        # 获取页码元素
        element5 = Ebuy.pageobject.get_elements(By.CSS_SELECTOR, 'div.pages>a')
        # 点击【尾页】
        element5[len(element5) - 1].click()
        # time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        Ebuy.pageobject.driver.quit()
