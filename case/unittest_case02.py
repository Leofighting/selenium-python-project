# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest


class FirstCase02(unittest.TestCase):
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

    @unittest.skip("不执行第一条")
    def testfirst001(self):
        print("第0000一条 case")

    def testfirst002(self):
        print("第0000二条 case")

    def testfirst003(self):
        print("第00003条 case")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase01("testfirst03"))
    # suite.addTest(FirstCase01("testfirst01"))
    # suite.addTest(FirstCase01("testfirst02"))
    # unittest.TextTestRunner().run(suite)

