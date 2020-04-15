#!/usr/bin/python
# coding:utf-8
# while循环语句

# ------------------------------------------
# continue用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i


# -------------------------------------------
# break用法
i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break

# -------------------------------------------
# 无限循环

# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = raw_input("Enter a number  :")
#    print "You entered: ", num

# print "Good bye!"

# --------------------------------------------
# 循环使用else语句

# 在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
count = 0
while count < 5:
    print count, "is less than 5"
    count += 1
    break
else:
    print count, "is not less than 5"


# -------------------------------------------------
flag = 1

while (flag):  
    print 'Given flag is really true!'
    break

print "Good bye!"
