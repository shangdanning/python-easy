#!/usr/bin/python
# coding:utf-8
# break语句，打破了最小的封闭for或while循环

for itemOut in range(9):
    for itemIn in range(9):
        if(itemIn*itemOut > 50 or itemOut > 5):
            break
        else:
            print "%d * %d = %d" % (itemOut, itemIn, itemOut*itemIn)
    print str(itemOut) + "开始循环"
print "good bye!"
