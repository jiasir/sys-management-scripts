#!/usr/bin/env python
# -*- coding: utf-8 -*-



dict_list = [
  { "id": 4, "pid": "b", "name": "004", "info": "描述004" },
  { "id": "a", "pid": "null", "name": "001", "info": "描述001" },
  { "id": 2, "pid": "a", "name": "002", "info": "描述002" },
  { "id": 6, "pid": "b", "name": "006", "info": "描述006" },
  { "id": "b", "pid": "a", "name": "003", "info": "描述003" },
  { "id": 5, "pid": 4, "name": "005", "info": "描述005" },
  { "id": 7, "pid": "a", "name": "007", "info": "描述007" }
]

new_dict = {}

for d in dict_list:
  new_dict.setdefault(d["pid"], []).append(d["id"])

def recursive(id, d=new_dict):
  if id in d:
    return [id] + [recursive(child) for child in d[id]]
  else:
    return id

source = ['result_list = [']
result_list = []

for child in new_dict["null"]:
  source.append(' # %s' % child)
  source.append(' %r,' % recursive(child))
  result_list.append(recursive(child))
  source.append(' ]')
  result_list_source = '\n'.join(source)
  print result_list_source
  print result_list




