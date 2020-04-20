#!/usr/bin/python
# coding:utf-8
# type


# class example(object):
#     pass


# object1 = example()

# print type(example)

class_example = type('class_example', (), {})
a = class_example()

# 获取a实例的class
# <class '__main__.class_example'>
print a.__class__


# <type 'type'>
print a.__class__.__class__

'''
可以看出，所有的class都来自于type。type，作为metaclass，创建了以上所有的class object。

type是Python定义好的metaclass。当然，我们也可以自定义metaclass。
'''
