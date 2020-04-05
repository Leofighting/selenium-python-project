# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import unittest

import HTMLTestRunner_PY3
import ddt
from selenium import webdriver

from business.register_business import RegisterBusiness
from config.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()


class FirstDdtCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://my.cnki.net/Register/")
        self.register = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close()

    @ddt.data(*data)
    @ddt.unpack
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.register.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")


if __name__ == '__main__':
    f = open(r"E:\测试\selenium_project\report\first.html", "wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title="this is first report", description=u"第一次测试报告",
                                               verbosity=1)
    runner.run(suite)
