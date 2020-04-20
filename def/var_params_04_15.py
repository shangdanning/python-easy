#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *是将参数以元组的形式进行传递


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    print vartuple
    vartuple = [1, 2, 3]
    for var in vartuple:
        print var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)
