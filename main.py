#/usr/bin/python
# coding:utf-8
# File: main.py
"""
本模块用于获取智联招聘上的招聘信息
"""

# 获取第一层工作分类，链接
import get_first_url

first_list = get_first_url.get_first_url()

# 获取第二层工作分类，链接，招聘信息数

import get_second_url

for (j,u) in first_list:
    second_list = get_second_url.get_second_url(u)
    print(len(second_list))
    
