#!/usr/bin/env python3
# coding:utf-8
"""
Name: dirlister.py
Author: murphy
Email: zd_wangfenglin@163.com
Time: 2020/6/29 4:51 下午
Desc:
"""


import os


def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return files


if __name__ == '__main__':
    run()
