# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from PIL import Image

from page.register_page import RegisterPage


class GetCode:

    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(driver)

    def get_code_image(self, file_name="E:\测试\selenium_project\image.png"):
        """获取二维码图片"""
        self.driver.save_screenshot(file_name)
        code_element = self.register_p.get_check_code_element()
        left = code_element.location["x"]
        top = code_element.location["y"]
        width = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, width, height))
        img.save(file_name)
        time.sleep(1)
