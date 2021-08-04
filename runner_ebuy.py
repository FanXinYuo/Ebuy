import unittest
from Ebuy.Common.TestReport import test_report
from Ebuy.Common.SendMail import send_mail
import os


dir = './Ebuy/TestCase'
dis = unittest.defaultTestLoader.discover(dir, pattern='Ebuy_Test.py')

# 生成测试报告
test_report(dis, r'./Ebuy/TestReport/', '资讯中心+商品上架_', '易买网测试报告')

# 发送邮件
# 测试报告
lists1 = os.listdir(r'./Ebuy/TestReport')    # 遍历 资讯报告 测试报告文件夹，将文件名保存在列表
ff = r'./Ebuy/TestReport/'+lists1[-1]   # 使用最后一个文件
# 日志
lists1 = os.listdir(r'./Ebuy/Logs')
ff1 = r'./Ebuy/Logs/'+lists1[-1]

# 截图
currentPath = os.getcwd()
target_path = os.path.join(currentPath, 'Ebuy', 'ScreenShot')
file_list = os.listdir(target_path)

send_mail(ff, ff1, target_path, file_list)









