# -*- coding:utf-8 -*-
__author__ = "leo"

from page.register_page import RegisterPage


class RegisterHandle:
    """处理注册"""

    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    def send_user_name(self, username):
        self.register_p.get_username_element().send_keys(username)

    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    def send_user_code(self, code_text):
        self.register_p.get_code_text_element().send_keys(code_text)

    def get_user_text(self, info, user_info):
        if info == "email_error":
            text = self.register_p.get_email_error_element().get_attribute("value")
        elif info == "username_error":
            text = self.register_p.get_username_error_error_element().get_attribute("value")
        elif info == "password_error":
            text = self.register_p.get_password_error_element().get_attribute("value")
        else:
            text = self.register_p.get_code_text_error_element().get_attribute("value")
        return text

    def click_register_button(self):
        self.register_p.get_register_button_element().click()

    def get_register_button_text(self):
        self.register_p.get_register_button_element().get_attribute("value")

