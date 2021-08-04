from HTMLTestRunner import HTMLTestRunner
import time


def test_report(dis, path, name, title):
    # 新建一个用于保存测试结果的文件，html
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # 定义文件的名字
    filename = path + name + now + ".html"
    # 执行我们的报告写入
    file = open(filename, "wb")
    # 加入HTMLTestRunner之后运行文件
    runner = HTMLTestRunner(stream=file, title=title, description="用例执行情况:")
    """ stream：是指定测试报告文件
        title：指定报告的标题
        description:指定报告的副标题 """
    # 执行我们测试用例
    runner.run(dis)
    time.sleep(3)
    # 要进行关闭
    file.close()

