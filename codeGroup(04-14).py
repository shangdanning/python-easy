#!/usr/bin/python
# coding:utf-8
# 多个语句构成代码组

"""
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
"""

a = 3
if a == 1:
    print a
elif a == 2:
    print a
else:
    print a
