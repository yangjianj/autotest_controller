# -*- coding: utf-8 -*-
import time,os
import unittest

class Demo(unittest.TestCase):

    def test_q1(self):
        print("ss")
        print(self.mydata2)

    def test_q2(self):
        print("ww")

    @classmethod
    def setUpClass(cls): #每个测试套件执行之前动作
        cls.mydata1 =1
        print("all start")
        print(Demo.mydata1)
        print("in class setup")
        print(cls.mydata1)

    @classmethod
    def tearDownClass(cls): #每个测试套件执行之后动作
        print("in class teardown")


    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('in teardown')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print("@@@@@@@@@@@@@@@@")
        self.mydata2 =2
        print("###################case start")
        print(self.mydata2)
        print('in setup')

if __name__ == '__main__':
    pass