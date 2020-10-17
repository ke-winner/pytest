#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pythoncode.caculator import Caculator


class TestCalc:
    def setup_class(self):
        print("\n计算开始")
        self.calc = Caculator()

    def teardown_class(self):
        print("\n计算结束")

    # def test_add(self):
    #     # calc = Caculator()
    #     result =self. calc.add(1,1)
    #     assert result == 2
    #
    # def test_add2(self):
    #     # calc = Caculator()
    #     result =self.calc.add(0.1,0.1)
    #     assert result == 0.2
    #
    # def test_add3(self):
    #     # calc = Caculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200

    @pytest.mark.parametrize(["a", "b", "expect"], [[1, 2, 3], [3, 4, 7]], ids=['int_case', 'float_case2'])
    def test_add_all(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    def test_add(self):
        data = [[1, 2, 3], [3, 4, 7]]
        for i in range(1, len(data)):
            result = self.calc.add(data[i][0], data[i][1])
        assert result == data[i][2]
