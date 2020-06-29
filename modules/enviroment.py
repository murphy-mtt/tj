#!/usr/bin/env python3
# coding:utf-8
"""
Name: enviroment.py
Author: murphy
Email: zd_wangfenglin@163.com
Time: 2020/6/29 4:59 下午
Desc:
"""


import os


def run(**kwargs):
    return str(os.environ)


if __name__ == '__main__':
    print(run())
