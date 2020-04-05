# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.webdriver.common.by import By

from features.lib.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, context):
        super().__init__(context.driver)

    def send_username(self, username):
        self.find_element(By.ID, "username").send_keys(username)

    def send_password(self, password):
        self.find_element(By.ID, "txtPassword").send_keys(password)

    def send_email(self, email):
        self.find_element(By.ID, "txtEmail").send_keys(email)

    def send_code(self, code):
        self.find_element(By.ID, "checkcode").send_keys(code)

    def click_register_button(self):
        self.find_element(By.ID, "ButtonRegister").click()

    def get_code_text(self):
        return self.find_element(By.ID, "txtOldCheckCode").text
