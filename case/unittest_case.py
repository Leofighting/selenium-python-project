# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest


class FirstCase01(unittest.TestCase):
    """创建继承 unittest.TestCase 的用例"""

    @classmethod
    def setUpClass(cls) -> None:
        print("前置条件")

    @classmethod
    def tearDownClass(cls) -> None:
        print("后置条件")

    def setUp(self) -> None:
        print("这是case 的前置条件")

    def tearDown(self) -> None:
        print("这是case 的后置条件")

    def testfirst01(self):
        print("第一条 case")

    def testfirst02(self):
        print("第二条 case")

    def testfirst03(self):
        print("第3条 case")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01("testfirst03"))
    suite.addTest(FirstCase01("testfirst01"))
    suite.addTest(FirstCase01("testfirst02"))
    unittest.TextTestRunner().run(suite)

