#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# def test_case1():
#     print("testcase1")

# def setup_module():
#     print("资源准备")
#
# def teardown_module():
#     print("资源销毁")
#
# def setup_function():
#     print("资源准备")
#
# def teardown_function():
#     print("资源销毁")

class TestDemo:

    # 执行类前后执行
    # def setup_class(self):
    #     print("TestDemo setup_class")
    #
    # def teardown_class(self):
    #     print("TestDemo teardown_class")

    def setup(self):
        print("TestDemo setup_function")

    def teardown(self):
        print("TestDemo teardown_function")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
