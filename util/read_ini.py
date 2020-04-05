# -*- coding:utf-8 -*-
__author__ = "leo"

import configparser

# cf = configparser.ConfigParser()
# cf.read("E:\测试\selenium_project\config\LocalElement.ini")
# res = cf.get("RegisterElement", "user_email")
# print(res)


class ReadIni:
    """读取 ini 文件"""
    def __init__(self, file_name=None, node=None):
        if not file_name:
            file_name = "E:\测试\selenium_project\config\LocalElement.ini"

        if not node:
            self.node = "RegisterElement"
        else:
            self.node = node

        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        """加载 ini 文件"""
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        """获取值"""
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    read_ini.get_value("password")
