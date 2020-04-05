# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import random

from selenium import webdriver
from PIL import Image

from base.find_element import FindElement


class RegisterFunction:
    """注册"""
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        if i == 0:
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        return driver

    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    def click_element(self, key):
        self.get_user_element(key).click()

    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):
        """随机生成用户"""
        user_info = "".join(random.sample("1234567890asdfghjkl", 6))
        return user_info

    def get_code_image(self, file_name):
        """获取二维码图片"""
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location["x"]
        top = code_element.location["y"]
        width = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, width, height))
        img.save(file_name)

    def main(self):
        user_name = self.get_range_user()
        email = user_name + "@163.com"
        file_name = "E:\测试\selenium_project\image.png"
        code_text = "1234"
        self.get_code_image(file_name)
        self.send_user_info("user_name", user_name)
        self.send_user_info("password", "123456")
        self.send_user_info("user_email", email)
        self.send_user_info("code_text", code_text)
        self.click_element("register_button")
        code_error = self.get_user_element("code_text_error")

        if not code_error:
            print("注册成功~")
        else:
            file_name = "E:\测试\selenium_project\error.png"
            self.driver.save_screenshot(file_name)
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    for i in range(2):
        register_func = RegisterFunction("http://my.cnki.net/Register/", i)
        register_func.main()