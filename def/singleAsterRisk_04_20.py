#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 单星号可以用来解压参数列表


def foo(runoob_1, runoob_2):
    print(runoob_1, runoob_2)


l = {'a': 1, 'b': 2}
foo(*l)
l1 = [1, 2]
foo(*l1)
l2 = {1, 2}
foo(*l2)
