#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 单双星号合起来使用


def foo(a, b=10, *args, **kwargs):
    print a
    print b
    print args
    print kwargs


foo(1, 2, 3, 4, e=5, f=6, g=7)
