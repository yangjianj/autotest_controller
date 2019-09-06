# -*- coding: utf-8 -*-
import time,os
import unittest
from app_demo3.lib.page_handler import Pagehandler

class Base_t1(unittest.TestCase):  # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls): #每个测试套件执行之前动作
        Base_t1.handler = Pagehandler()

    @classmethod
    def tearDownClass(cls): #每个测试套件执行之后动作
        Base_t1.handler.close()
        Base_t1.handler.quit()

    def setUp(self):
        # 每个测试用例执行之前做操作
        self.handler = Base_t1.handler
        self.handler.load_element_location_file("lianjia")
        print('in setup')

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('in teardown')

    @unittest.skipIf(3 > 2, "3大于2，此用例不执行")
    def test_run(self):
        self.handler.get("http://www.lianjia.com")
        self.handler.click("城市","board")
        self.handler.clear("搜索框","city")
        self.handler.send_keys("搜索框","city","武汉")
        self.handler.wait_until_page_contain_element("搜索提示框","city",5)
        self.handler.click("搜索按钮","city")
        self.handler.switch_to_next_windows()
        print("go to city succeed!")
        self.handler.clear("搜索框","board")
        self.handler.send_keys("搜索框","board","当代卡梅尔小镇")
        self.handler.click("搜索按钮","board")
        self.handler.wait_until_page_contain_element("经纪人","二手房在售",5)
        self.handler.click("经纪人","二手房在售")
        self.handler.send_keys("搜索框","经纪人","123")
        self.handler.click("搜索按钮","经纪人")

    @unittest.skipUnless(3 < 2, "2没有大于3，此用例不执行")
    def test_run2(self):
        self.handler.get("http://www.lianjia.com")
        self.handler.click("城市", "board")
        self.handler.clear("搜索框", "city")
        self.handler.send_keys("搜索框", "city", "北京")
        self.handler.wait_until_page_contain_element("搜索提示框", "city", 5)
        self.handler.click("搜索按钮", "city")
        self.handler.switch_to_next_windows()
        self.handler.clear("搜索框", "board")
        self.handler.send_keys("搜索框", "board", "瞰都国际")
        self.handler.click("搜索按钮", "board")

    @unittest.skip("用户名密码都为空用例不执行")
    def test_run3(self):
        # self.assertEqual(1,1)
        print("111111111111111111111")
        print(time.localtime())
        time.sleep(5)
        self.assertIs(1, -1)
        # 测试用例

    def test_run1(self):
        self.handler.get("http://www.lianjia.com")
        self.handler.click("城市", "board")
        self.handler.clear("搜索框", "city")
        self.handler.send_keys("搜索框", "city", "武汉")
        self.handler.wait_until_page_contain_element("搜索提示框", "city", 10)
        self.handler.click("搜索按钮", "city")
        self.handler.switch_to_next_windows()
        print("go to city succeed!")
        self.handler.clear("搜索框", "board")
        self.handler.send_keys("搜索框", "board", "当代卡梅尔小镇")
        self.handler.click("搜索按钮", "board")
        self.handler.wait_until_page_contain_element("顶部菜单", "二手房在售", 10)
        top_menu = self.handler.get_elements("顶部菜单子节点","二手房在售")
        for index in range(len(top_menu)):
            ele_loc = self.handler.build_location_by_param("菜单子项", "二手房在售",index+1)
            text=self.handler.find_element_by_location(ele_loc).text
            print(text)

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="ui*.py", top_level_dir=None)
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