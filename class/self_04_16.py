#!/usr/bin/python
# -*- coding: UTF-8 -*-

# self代表类的实例，而非类。self__class__指向类


class Test:
    '测试self'

    def prt(self):
        # <__main__.Test instance at 0x10511def0>
        print self

        # 测试self
        print self.__class__.__doc__

        # {'prt': <function prt at 0x1051130c8>, '__module__': '__main__', '__doc__': '\xe6\xb5\x8b\xe8\xaf\x95self'}
        print self.__class__.__dict__

        # ()
        print self.__class__.__bases__

        # 测试self
        print self.__doc__


# 类的实例化，不用new，类的实例化类似于函数的调用方式
t = Test()
t.prt()
 # ()
print Test.__bases__
# __main__
print Test.__module__
# Test
print Test.__name__

