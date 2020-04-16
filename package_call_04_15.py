#!/usr/bin/python
# coding:utf-8

from package.runoob1 import runoob1
from package.runoob2 import runoob2
# 当引用同级目录时，没有__init__.py文件亦可
import frozenset_04_14
'''
package_runoob 初始化
i am in runoob1
i am in runoob2
'''
runoob1()
runoob2()

# __main__
print __name__
