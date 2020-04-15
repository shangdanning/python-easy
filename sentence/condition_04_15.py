#!/usr/bin/python
# coding:utf-8
# 条件语句  Python程序语言指定任何非0或者非空（null）值为true,0或者null为false

if "":
    print "123"
else:
    print "234"

# --------------------------
a = 1
while a < 7:
    if(a % 2 == 0):
        print a, "is even"
    else:
        print a, "is odd"
    a += 1
# --------------------------

num = 5
if num == 3:
    print "boss"
elif num == 2:
    print "user"
else:
    print "roadman"

# ----------------------------
# 也可以在同一行的位置上使用if条件判断语句

var = 100
if var == 100:  print"变量var的值为100"
print "Good bye"
