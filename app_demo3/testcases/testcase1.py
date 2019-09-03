# -*- coding: utf-8 -*-
import time,os
import unittest
from app_demo3.lib.page_handler import Pagehandler

class Base_t1(unittest.TestCase):  # 继承unittest.TestCase

    def __init__(self,browser='chrome'):

        Base_t1.handler = Pagehandler(browser)
        self.handler = Base_t1.handler
        self.handler.load_element_location_file("lianjia")

    @classmethod
    def setUpClass(cls): #每个测试套件执行之前动作
        cls.handler = None

    @classmethod
    def tearDownClass(cls): #每个测试套件执行之后动作
        cls.handler.close()
        cls.handler.quit()


    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('in teardown')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('in setup')



    def test_run(self):
        self.handler.get("http://www.lianjia.com")
        self.handler.click("board","城市")
        self.handler.clear("city","搜索框")
        self.handler.send_keys("city","武汉")
        self.handler.wait_until_page_contain_element("city","搜索提示框")
        self.handler.click("city","搜索按钮")
        self.handler.switch_to_next_windows()
        self.handler.clear("board","搜索框")
        self.handler.send_keys("board","当代卡梅尔小镇")
        self.handler.click("board","搜索按钮")
        self.handler.wait_until_page_contain_element("二手房在售","经纪人",10)
        self.handler.click("二手房在售","经纪人")
        self.handler.send_keys("经纪人","搜索框","123")
        self.handler.click("经纪人","搜索按钮")

    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(4)
        self.assertEqual(-1, mins(1, 2))  # 对待测方法进行测试
        # 测试用例

    def test_run3(self):
        # self.assertEqual(1,1)
        print("111111111111111111111")
        print(time.localtime())
        time.sleep(5)
        self.assertIs(1, 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(6)
        # 测试用例
if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    test_result = unittest.TextTestRunner(verbosity=2).run(discover)
    print('All case number')
    print(test_result.testsRun)
    print('Failed case number')
    print(len(test_result.failures))
    print('Failed case and reason')
    print(test_result.failures)
    for case, reason in test_result.failures:
        print(case.id())
        print(reason)

    print('skiped case')
    print(test_result.skipped)
    print('expectedFailures case')
    print(test_result.expectedFailures)
    print('unexpectedSuccesses case')
    print(test_result.unexpectedSuccesses)
    print('errors case')
    print(test_result.errors)