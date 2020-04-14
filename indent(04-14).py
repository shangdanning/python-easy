#!/usr/bin/python
# coding:utf-8
#行和缩进
if True:
    print("True")
else:
    print "False"


if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")