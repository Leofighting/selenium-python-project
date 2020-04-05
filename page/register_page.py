# -*- coding:utf-8 -*-
__author__ = "leo"

from base.find_element import FindElement


class RegisterPage:
    """注册页面元素"""

    def __init__(self, driver):
        self.find_el = FindElement(driver)

    def get_email_element(self):
        return self.find_el.get_element("user_email")

    def get_username_element(self):
        return self.find_el.get_element("user_name")

    def get_password_element(self):
        return self.find_el.get_element("password")

    def get_code_text_element(self):
        return self.find_el.get_element("code_text")

    def get_code_image_element(self):
        return self.find_el.get_element("code_image")

    def get_register_button_element(self):
        return self.find_el.get_element("register_button")

    def get_code_text_error_element(self):
        return self.find_el.get_element("code_text_error")

    def get_username_error_error_element(self):
        return self.find_el.get_element("username_error")

    def get_password_error_element(self):
        return self.find_el.get_element("password_error")

    def get_email_error_element(self):
        return self.find_el.get_element("email_error")