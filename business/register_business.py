# -*- coding:utf-8 -*-
__author__ = "leo"

from handle.register_handle import RegisterHandle


class RegisterBusiness:

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    def register_success(self):
        return True if self.register_h.get_register_button_text() else False

    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)

        if not self.register_h.get_user_text("email_error", "请输入电子邮箱"):
            print("邮箱校验不成功~")
            return True
        else:
            return False

    def login_username_error(self, email, name, password, code):
        self.user_base(email, name, password, code)

        if not self.register_h.get_user_text("username_error", "请输入用户名"):
            print("用户名校验不成功~")
            return True
        else:
            return False

    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)

        if not self.register_h.get_user_text("password_error", "请输入密码"):
            print("密码校验不成功~")
            return True
        else:
            return False

    def login_code_text_error_error(self, email, name, password, code):
        self.user_base(email, name, password, code)

        if not self.register_h.get_user_text("code_text_error", "请输入验证码"):
            print("验证码校验不成功~")
            return True
        else:
            return False