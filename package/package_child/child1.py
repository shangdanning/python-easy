#!/usr/bin/python
# coding:utf-8

# from package.runoob1 import runoob1

# import runoob1

import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

# sys.path.insert(0, os.path.abspath('..'))


def child1():

    print "i am in package_child/child1"


# child1()
# runoob1()


# /Users/shangdanning/Documents/code/python-easy/package

# print os.path.abspath(os.path.dirname(__file__) + '/' + '..')
# print sys.path
# print os.path.abspath('..')
# print parentdir
