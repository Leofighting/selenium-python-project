# -*- coding:utf-8 -*-
__author__ = "leo"

import ddt
import unittest


@ddt.ddt
class DataTest(unittest.TestCase):

    def setUp(self) -> None:
        print("前置")

    def tearDown(self) -> None:
        print("后置")

    @ddt.data(
        ["1", "2"],
        ["3", "4"],
        ["5", "6"]
        # [1, 2],
        # [3, 4]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)


if __name__ == '__main__':
    unittest.main()
