# -*- coding:utf-8 -*-
__author__ = "leo"

import random
import time

from PIL import Image
from selenium import webdriver

# from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()

def driver_init():
    """初始化浏览器"""
    driver.get("http://my.cnki.net/Register/")
    driver.maximize_window()
    time.sleep(3)


def get_element(id):
    """获取 element 元素"""
    element = driver.find_element_by_id(id)
    return element


def get_range_user():
    """随机生成用户"""
    user_info = "".join(random.sample("1234567890asdfghjkl", 6))
    return user_info


def get_code_image(file_name):
    """获取二维码图片"""
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("checkcode")
    left = code_element.location["x"]
    top = code_element.location["y"]
    width = code_element.size["width"] + left
    height = code_element.size["height"] + top
    im = Image.open(file_name)
    img = im.crop((left, top, width, height))
    img.save(file_name)


# def get_code(file_name):
#     """解析验证码图片"""
#     r = ShowapiRequest("https://www.showapi.com/184-4", "用户的key", "秘钥")
#     r.addBodyPara("typeId", "35")
#     r.addBodyPara("covert_to_jpg", "0")
#     r.addFilePara("image", file_name)
#     res = r.post()
#     text = res.json()["showapi_res_body"]["Result"]
#     return text


def main():
    user_name = get_range_user()
    email = get_range_user() + "@163.com"
    file_name = "E:\测试\selenium_project\image.png"
    driver_init()
    get_element("username").send_keys(user_name)
    get_element("txtPassword").send_keys("123456")
    get_element("txtEmail").send_keys(email)
    get_code_image(file_name)

    get_element("ButtonRegister").click()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    main()
