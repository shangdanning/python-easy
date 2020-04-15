#!/usr/bin/python
# coding:utf-8
# Python中for循环语句可以遍历任何序列的项目，如每一个列表或者一个字符串

for letter in 'Python':
    print letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print fruit
print "good bye"


# -------------------------------------
# 通过序列索引迭代
# 内置函数：len()、range()
# len()是返回列表的长度，即元素的个数
# range()是返回一个序列的数

#[0, 1, 2, 3, 4, 5, 6, 7, 8]
# print range(9)
print "--------------------------------"
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print fruits[index]
else:
    print "最后一种水果是orange"

# -------------------------------------
print "--------------------------------"
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:      # 确定第一个因子
            j = num/i          # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print num, '是一个质数'


# -------------------------------------
print "--------------------------------"

print '%d 等于 %d * %d' % (10, 2, 5)



