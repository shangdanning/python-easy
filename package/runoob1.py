#!/usr/bin/python
# coding:utf-8
# 在包中引用同级模块或者子级模块比较简单，直接引用即可.引用的文件里的代码先执行
from runoob2 import runoob2
from package_child.child1 import child1


def runoob1():

    print "i am in runoob1"
    print "runoob1 __name:"+__name__


'''
i am in package_child/child1
i am in runoob2
i am in package_child/child1
'''

runoob2()
child1()
