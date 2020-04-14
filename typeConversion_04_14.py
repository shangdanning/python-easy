#!/usr/bin/python
# coding:utf-8
# python数据类型转换

# a=int()
# a = int(3)
# a = int(3.6)
# a = int('12', 16)
# a = int('0xa',16)
a = int('10', 8)

print a

# s = "runoob"
# b = str(s)

s = {'1', '2'}
b = str(s)
c = repr(s)
print b
print c

print "---------------------------"

aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)

print "Tuple elements : ", aTuple
