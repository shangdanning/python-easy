#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一个异常可以带上参数，可作为输出的异常信息参数。

# 定义函数


def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument


# 调用函数
temp_convert("xyz")
