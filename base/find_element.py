# -*- coding:utf-8 -*-
__author__ = "leo"

from util.read_ini import ReadIni


class FindElement:
    """查找元素"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        """获取元素"""
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "classname":
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            self.driver.save_screenshot("E:\\测试\\selenium_project\\error.png")
            return None
