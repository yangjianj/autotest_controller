import os,time
import unittest
#import xmlrunner
import ddt
from  app_demo1.lib.tool import *

configpath=os.path.join(os.path.dirname(os.path.abspath(__file__)),"config//ddt_test_001.csv")
testdata = import_excel_data_for_ddt(configpath)
@ddt.ddt
class MyTest1(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('in teardown')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('in setup')

    @classmethod
    def tearDownClass(cls): #每个测试套件执行之后动作
        print('in teardownclass')

    @classmethod
    def setUpClass(cls): #每个测试套件执行之前动作
        print('in setUpClass')

    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(3)
        result=self.assertEqual(3,2)
        print('11111111111 in test ')
        print(result)
        # 测试用例

    def test_run2(self):
        # self.assertEqual(1,1)
        print("111111111111111111111")
        print(time.localtime())
        time.sleep(5)
        self.assertIs(1, 1)
        # 测试用例

    @ddt.data(*testdata)
    def test_run1(self,data):
        print(data)
if __name__ == '__main__':
     pass