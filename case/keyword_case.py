# -*- coding:utf-8 -*-
__author__ = "leo"

import sys

from config.excel_util import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod

sys.path.append("E:\\测试\\selenium_project")


class KeyWordCase:
    """关键字"""

    def __init__(self):
        self.action_method = ActionMethod()

    def run_main(self):
        handle_excel = ExcelUtil("E:\\测试\\selenium_project\\config\\keyword.xls")
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == "yes":
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)

                    self.run_method(method, send_value, handle_value)
                    if not except_result:
                        print("000000000", except_result)
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == "text":
                            result = self.run_method(except_result_method)
                            print(result)
                            if except_value[1] in result:
                                handle_excel.write_value(i, "pass")
                            else:
                                handle_excel.write_value(i, "fail")
                        elif except_value[0] == "element":
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, "pass")
                            else:
                                handle_excel.write_value(i, "fail")
                    else:
                        print("预期结果为空")

    def run_method(self, method, send_value="", handle_value=""):
        method_value = getattr(self.action_method, method)
        if send_value:
            return method_value(send_value, handle_value)
        elif not send_value and handle_value:
            return method_value(handle_value)
        else:
            return method_value()

    def get_except_result_value(self, data):
        return data.split("=")


if __name__ == '__main__':
    kw = KeyWordCase()
    kw.run_main()
