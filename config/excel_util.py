# -*- coding:utf-8 -*-
__author__ = "leo"

import xlrd
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if not excel_path:
            self.excel_path = "E:\\测试\\selenium_project\\config\\casedata.xls"
        else:
            self.excel_path = excel_path
        if not index:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    def get_lines(self):
        """获取行数"""
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_col_value(self, row, col):
        """获取单元格内容"""
        if row < self.get_lines():
            data = self.table.cell(row, col).value
            return data
        return None

    def write_value(self, row, value):
        """向Excel表写入数据"""
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    test = ExcelUtil(excel_path="E:\\测试\\selenium_project\\config\\keyword.xls")
