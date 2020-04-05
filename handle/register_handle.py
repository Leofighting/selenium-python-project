# -*- coding:utf-8 -*-
__author__ = "leo"

from page.register_page import RegisterPage
from util.get_code import GetCode


class RegisterHandle:
    """处理注册"""

    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    def send_user_name(self, username):
        self.register_p.get_username_element().send_keys(username)

    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    def send_user_code(self, code_text):
        get_code_image = GetCode(self.driver)
        code_image = get_code_image.get_code_image()
        self.register_p.get_code_text_element().send_keys(code_text)

    def get_user_text(self, info, user_info):
        try:
            if info == "email_error":
                text = self.register_p.get_email_error_element().text
            elif info == "username_error":
                text = self.register_p.get_username_error_error_element().text
            elif info == "password_error":
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_text_error_element().text
        except:
            text = None
        return text

    def click_register_button(self):
        self.register_p.get_register_button_element().click()

    def get_register_button_text(self):
        self.register_p.get_register_button_element().get_attribute("value")
