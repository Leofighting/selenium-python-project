# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver

from base.find_element import FindElement


class ActionMethod:
    # def __init__(self, driver):
    #     self.driver = driver

    def open_browser(self, browser):
        """打开浏览器"""
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def get_url(self, url):
        """输入url"""
        self.driver.get(url)

    def get_element(self, key):
        """获取元素"""
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self, value, key):
        """输入元素"""
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self, key):
        """点击元素"""
        element = self.get_element(key)
        element.click()

    def sleep_time(self):
        """等待时间"""
        time.sleep(2)

    def close_browser(self):
        """关闭浏览器"""
        self.driver.close()

    def get_title(self):
        """获取标题"""
        return self.driver.title
