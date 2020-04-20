#!/usr/bin/python
# coding:utf-8
# class的类型


class MyClass:
    data = 1


# class1 = MyClass()
# print class1
# print type(class1)

print type(MyClass)


class example(object):
    pass


object1 = example()
print(object1)
print example

# 可以给对象添加属性
print hasattr(example, 'new_attribute')
example.new_attribute = 'assign an attribute to the class'
print hasattr(example, 'new_attribute')

# 可以将其赋给一个变量
example_mirror=example
print example_mirror

print example_mirror()

# 可以将其作为参数赋给其他函数
def echo(cls):
    print cls

echo(example)

