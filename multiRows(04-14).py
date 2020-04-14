#!/usr/bin/python
# coding:utf-8
# 多行语句

# 我们可以使用斜杠（ \）将一行的语句分为多行显示
item_one = "1"
item_two = "2"
item_three = "3"
total = item_one +\
    item_two +\
    item_three
print (total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)


# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')