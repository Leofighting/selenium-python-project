### 环境搭建

> 安装 selenium 包：`pip install selenium`

> 关于启动浏览器，以 Chrome 浏览器为例，需要将浏览器插件复制到 python 解释器文件目录下（即安装目录下，`python.exe` 所在的文件夹中）；例如： `D:\install\python37`
>
> 如果使用虚拟环境，需要放置虚拟环境 `python.exe` 所在的文件夹中；例如：`C:\Users\xiaoj\.virtualenvs\selenium_project-4aeFtfY0\Scripts`



### 启动浏览器

> ```python
> from selenium import webdriver
> 
> # driver = webdriver.Chrome()  # 启动 Chrome 浏览器
> # driver = webdriver.Edge()  # 启动 Edge 浏览器
> driver = webdriver.Firefox()  # 启动 Firefox 浏览器
> driver.get("https://www.baidu.com/")  # 打开百度页面
> ```

#### 通过标题判断页面是否为打开的页面

> ```python
> from selenium.webdriver.support import expected_conditions
> 
> driver.get("https://my.cnki.net/Register")
> expected_conditions.title_contains("注册")
> ```

#### 元素定位并输入内容

> ```python
> driver.find_element_by_id("username").send_keys("leo2020")
> driver.find_element_by_name("txtPassword").send_keys("111111")
> driver.find_element_by_xpath("//input[@id='txtEmail']").send_keys("123456@163.com")
> driver.find_element_by_css_selector("#txtOldCheckCode").send_keys("1234")
> ```

#### 判断页面元素是否可见

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

locator = (By.ID, "username")  # 找一个定位器，通过 id，找到"username"
WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located(locator))  # 指定1秒的时间，直到找到元素
```

#### 获取验证码图片

> ```python
> driver.save_screenshot("E:\测试\selenium_project\image1.png")
> code_element = driver.find_element_by_id("checkcode")
> print(code_element.location)  # 输出格式{"x":11, "y":22}
> left = code_element.location["x"]
> top = code_element.location["y"]
> width = code_element.size["width"] + left
> height = code_element.size["height"] + top
> 
> im = Image.open("E:\测试\selenium_project\image1.png")
> img = im.crop((left, top, width, height))
> img.save("E:\测试\selenium_project\image2.png")
> ```