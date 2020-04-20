#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **是将参数以字典的形式进行传递


def bar(param1, **param2):
    print param1
    print param2

# 1
# {'a': 1, 'b': 2}
bar(1, a=1, b=2)
