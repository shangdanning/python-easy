#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义一个简单的类


class Employee:
    '所有员工的基类'
    empCount = 0
    # 私有变量，仅可在类内访问 或者通过Obj._classname__private来访问
    __private_name = "员工的薪资"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployee(self):
        print "name :", self.name, ": salary: ", self.salary


sdn = Employee('sdn', 100)
qq = Employee('qq', 200)
# sdn.displayCount()
# sdn.displayEmployee()
sdn.age = 27
print sdn.age


# 可以使用以下函数的方式访问属性
print hasattr(sdn, 'age')
print getattr(sdn, 'age')
setattr(sdn, 'age', 10)
delattr(sdn, 'age')
print getattr(sdn, 'empCount')
# 通过这种方式也可以访问到类的私有属性
print sdn._Employee__private_name
