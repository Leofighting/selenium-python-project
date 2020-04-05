# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest
import time
import os

from selenium import webdriver
import HTMLTestRunner_PY3

from business.register_business import RegisterBusiness


class FirstCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://my.cnki.net/Register/")
        self.register = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        self.driver.close()

    def test_login_email_error(self):
        email_error = self.register.login_email_error("34", "user11", "123qwe", "1234")
        self.assertTrue(email_error, "无效邮箱，注册失败~")

    def test_login_username_error(self):
        username_error = self.register.login_username_error("123456@163.com", "12", "123qwe", "1234")
        self.assertTrue(username_error, "无效用户名，注册失败~")

    def test_login_password_error(self):
        password_error = self.register.login_password_error("123456@163.com", "user123qwe", "123", "1234")
        self.assertTrue(password_error, "无效密码，注册失败~")
        if password_error:
            print("无效密码，注册失败~")

    def test_code_error(self):
        code_error = self.register.login_code_text_error_error("123456@163.com", "user123qwe", "123qweasd", "1234")
        self.assertTrue(code_error, "无效验证码，注册失败~")
        if code_error:
            print("无效验证码，注册失败~")

    def test_login_success(self):
        success = self.register.user_base("123456@163.com", "user123qwe", "123qweasd", "1234")
        self.assertTrue(success, "注册成功~")


# def main():
#     first = FirstCase()
#     first.test_login_email_error()
#     first.test_login_username_error()
#     first.test_login_password_error()
#     first.test_code_error()
#     first.test_login_success()


if __name__ == '__main__':
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_path = os.path.join(BASE_DIR, "report", "first.html")
    f = open(r"E:\测试\selenium_project\report\first.html", "wb")
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_success"))
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title="this is first report", description=u"第一次测试报告",
                                               verbosity=1)
    runner.run(suite)
