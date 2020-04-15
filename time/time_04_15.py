#!/usr/bin/python
# coding:utf-8
# 时间

import time
import calendar
ticks = time.time()
# 1586942856.44
print ticks

localtime = time.localtime(time.time())
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=15, tm_hour=17, tm_min=28, tm_sec=57, tm_wday=2, tm_yday=106, tm_isdst=0)
print localtime

print "-----------------------格式化日期--------------------------------"

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print "-----------------------获取某月的日历--------------------------------"

cal = calendar.month(2020, 4)
print cal
