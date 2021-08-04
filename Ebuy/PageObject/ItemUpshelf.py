from selenium.webdriver.common.by import By
import operator
import random
import pywinauto
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from Ebuy.Common.Random_String import RandomString


def web_data_deal(elements):
    list1 = []
    for i in range(1, len(elements)):
        list1.append(elements[i].text)
    return list1


def database_data_all(res):
    """all"""
    list1 = []
    for i in range(0, len(res)):
        list1.append(res[i][0])
    return list1


def database_data_one(res):
    """one"""
    list1 = []
    for i in range(0, len(res[0])):
        list1.append(res[0][i])
    return list1


def item_up_shelf(pageobject, database, index, flag, lg):
    good_info = []
    rs = RandomString()
    count1 = database.selectdate("select count(*) from easybuy_product")
    pageobject.click(By.LINK_TEXT, "商品上架")
    pageobject.driver.implicitly_wait(5)  # 隐式等待5s

    if flag == '重复':
        res = database.selectdate(
            "select categoryLevel1Id,categoryLevel2Id,categoryLevel3Id,name,price,stock from easybuy_product order by rand() limit 1")
        list1 = database_data_one(res)
        # 获取一级分类元素
        pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel1Id']")
        element = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel1>option")
        for i in range(1, len(element)):    # 0是请选择
            if element[i].get_attribute("value") == str(list1[0]):
                element[i].click()
                break
        # 获取二级分类元素
        pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel2Id']")
        element1 = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel2>option")
        for i in range(1, len(element1)):    # 0是请选择
            if element1[i].get_attribute("value") == str(list1[1]):
                element1[i].click()
                break
        # 获取三级分类元素
        pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel3Id']")
        element2 = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel3>option")
        for i in range(1, len(element2)):    # 0是请选择
            if element2[i].get_attribute("value") == str(list1[2]):
                element2[i].click()
                break
        # 写入商品名称
        pageobject.send_key(By.CSS_SELECTOR, "[name='name']", value=str(list1[3]))
        # 写入单价
        pageobject.send_key(By.CSS_SELECTOR, "[name='price']", value=str(list1[4]))
        # 写入库存
        pageobject.send_key(By.CSS_SELECTOR, "[name='stock']", value=str(list1[5]))
        # 点击【商品上架】
        pageobject.click(By.CSS_SELECTOR, "[value='商品上架']")
        database.commit()
        time.sleep(0.5)  # 给提交命令一个缓冲时间
        pageobject.screenshot("./Ebuy/ScreenShot/", "item_up_shelf_" + index + ".png")
        # 查询数据库
        count2 = database.selectdate("select count(*) from easybuy_product")
        assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！重复数据插入成功。")

    else:
        if flag[0] == '1':
            # 一级分类
            pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel1Id']")
            element = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel1>option")
            list1 = web_data_deal(element)
            res = database.selectdate("select name from easybuy_product_category where type='1'")
            list2 = database_data_all(res)
            assert operator.eq(list1, list2), "一级分类数据有误"
            # 任意选择一个一级分类
            i = random.randint(1, len(element) - 1)
            element[i].click()
            category1 = element[i].text
            parentid = database.selectdate(
                "select id from easybuy_product_category where name='" + category1 + "'")
            good_info.append(int(parentid[0][0]))

        if flag[1] == '1':
            # 二级分类
            pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel2Id']")
            element1 = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel2>option")
            list3 = web_data_deal(element1)
            res = database.selectdate(
                "select name from easybuy_product_category where type='2' and parentId='" + str(parentid[0][0]) + "'")
            list4 = database_data_all(res)
            assert operator.eq(list3, list4), "二级分类数据有误"
            # 任意选择一个二级分类
            i = random.randint(1, len(element1) - 1)
            element1[i].click()
            category2 = element1[i].text
            parentid = database.selectdate(
                "select id from easybuy_product_category where name='" + category2 + "'")
            good_info.append(int(parentid[0][0]))
        else:
            good_info.append(0)

        if flag[2] == '1':
            # 三级分类
            pageobject.click(By.CSS_SELECTOR, "[name='categoryLevel3Id']")
            element2 = pageobject.get_elements(By.CSS_SELECTOR, "select#productCategoryLevel3>option")
            list5 = web_data_deal(element2)
            res = database.selectdate(
                "select name from easybuy_product_category where type='3' and parentId='" + str(parentid[0][0]) + "'")
            list6 = database_data_all(res)
            assert operator.eq(list5, list6), "三级分类数据有误"
            # 任意选择一个三级分类
            i = random.randint(1, len(element2) - 1)
            element2[i].click()
            category3 = element2[i].text
            parentid = database.selectdate(
                "select id from easybuy_product_category where name='" + category3 + "'")
            good_info.append(int(parentid[0][0]))
        else:
            good_info.append(0)

        if flag[3] == "1":
            # 填写商品名称
            if flag[4] == '1':
                good_name = '可口可乐' + str(random.randint(1, 1000))
            elif flag[4] == '2':   # 名称超长
                good_name = '可口可乐1234567890987'
            elif flag[4] == '3':
                good_name = '可'
            elif flag[4] == '4':
                good_name = '可口可乐 '
            pageobject.send_key(By.CSS_SELECTOR, "[name='name']", value=good_name)
            good_info.append(good_name)
        else:
            good_info.append('')

        if flag[5] == "1":
            # 上传商品图片
            # 点击【上传文件】按钮
            click = pageobject.find(By.CSS_SELECTOR, "[name='photoFile']")
            ActionChains(pageobject.driver).click(click).perform()
            # 使用 pywinauto 来选择文件
            app = pywinauto.Desktop()
            # 选择文件上传的窗口
            dlg = app["打开"]
            # 选择文件地址输入框，点击激活
            dlg["Toolbar3"].click()
            # 键盘输入上传文件的路径
            send_keys(os.getcwd() + "\Ebuy\Data")
            # 键盘输入回车，打开该路径
            send_keys("{VK_RETURN}")
            # 选中文件名输入框，输入文件名
            if flag[6] == '1':
                dlg["文件名(&N):Edit"].type_keys("goods.jpg")
            else:
                dlg["文件名(&N):Edit"].type_keys("test.txt")
            # 点击打开
            dlg["打开(&O)"].click()

        if flag[7] == "1":
            # 填写单价
            if flag[8] == '1':
                price = str(rs.digit(3))
                good_info.append(float(price))
            elif flag[8] == '2':
                price = 'a1'
                good_info.append(price)
            elif flag[8] == '3':
                price = '56.765'
                good_info.append(price)
            pageobject.send_key(By.CSS_SELECTOR, "[name='price']", value=price)

        if flag[9] == "1":
            # 填写库存
            if flag[10] == '1':
                stock = str(rs.digit(4))
                good_info.append(int(stock))
            elif flag[10] == '2':
                stock = 'b1'
                good_info.append(stock)
            elif flag[10] == '3':
                stock = '34.5'
                good_info.append(stock)
            pageobject.send_key(By.CSS_SELECTOR, "[name='stock']", value=stock)


        if flag[11] == "1":
            # 填写描述
            pageobject.send_key(By.CSS_SELECTOR, "[name='description']", value="值得购买！")
            good_info.append("值得购买！")
        else:
            good_info.append("")

        # 点击
        pageobject.click(By.CSS_SELECTOR, "[value='商品上架']")
        database.commit()
        time.sleep(0.3)

        # 截图
        pageobject.screenshot("./Ebuy/ScreenShot/", "item_up_shelf_"+index+".png")
        count2 = database.selectdate("select count(*) from easybuy_product")

        """数据未插入成功"""
        if flag[0] == '0':   # 未填写一级分类
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！一级商品分类未选择！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '请选择商品分类', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '请选择商品分类', lg.info("警示框进行提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[3] == '0':     # 未填写商品名称
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品名称未填写！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '清填写商品名称', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '清填写商品名称', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[4] == '2' or flag[4] == '3':
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品名称长度有误！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '商品名称', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '商品名称为2到16个字符', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[4] == '4':
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品名称格式有误！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '商品名称', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '商品名称格式有误', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[7] == '0':     # 未填写商品价格
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品价格未填写！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '清填写商品价格', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '清填写商品价格', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[8] == '2' or flag[8] == '3':
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品价格格式有误！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '商品价格格式有误', lg.info("未出现警示框进行提示！")
            else:
                print(tip)
                assert tip == '商品价格格式有误', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[9] == "0":     # 未填写库存
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品库存未填写！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '清填写商品库存', lg.info("未出现警示框进行提示！")
                lg.info("未出现警示框进行提示！")
            else:
                assert tip == '清填写商品库存', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[10] == '2' or flag[10] == '3':
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！商品库存格式有误！")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '商品库存', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '商品库存格式有误', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        elif flag[6] == '2':    # 上传错误格式的商品图片
            if count1[0][0] == count2[0][0]:
                lg.info("数据库未插入数据！")
            assert count1[0][0] == count2[0][0], lg.info("数据库插入了不该插入的数据！图片格式有误。")
            tip = pageobject.text(By.CSS_SELECTOR, "[id='showMessage']")
            if tip == '':
                assert tip == '图片格式不对', lg.info("未出现警示框进行提示！")
            else:
                assert tip == '图片格式不对', lg.info("警示框提示有误！")
                # 点击【x】
                pageobject.click(By.CSS_SELECTOR, "[src='/ebuy/statics/images/close.gif']")
        else:
            pass

        if count1[0][0]+1 == count2[0][0]:
            lg.info("数据已插入数据库！")
            # 验证是否成功插入
            result2 = database.selectdate(
                "select categoryLevel1Id,categoryLevel2Id,categoryLevel3Id,name,price,stock,description from easybuy_product where name='"+good_name+"'")
            list8 = database_data_one(result2)
            assert operator.eq(good_info, list8), "数据库中插入数据与界面提交数据不符！"

