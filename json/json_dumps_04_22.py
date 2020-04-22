#!/usr/bin/python
# coding:utf-8
# json_dumps

import json
a = {'name': 'sdn', 'age': 20}

b = json.dumps(a)

print b


c = json.loads(b)

print c
