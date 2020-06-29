#!/usr/bin/env python3
# coding:utf-8
"""
Name: git_trojan.py
Author: murphy
Email: zd_wangfenglin@163.com
Time: 2020/6/29 5:14 下午
Desc:
"""


import json
import base64
import sys
import time
import random
import threading
import queue
import os

from github3 import login


trojan_id = "abc"

trojan_config = "%s.json" % trojan_id
data_path = "data/{}/".format(trojan_id)
trojan_modules = []
configured = False
task_queue = queue.Queue()


def connect_to_github(username, password, repo, branch="master"):
    gh = login(username=username, password=password)
    print(gh)
    repo = gh.repository(username, repo)
    print(repo)
    branch = repo.branch(branch)
    return gh, repo, branch


if __name__ == '__main__':
    with open(os.path.join(os.path.expanduser("~"), "online_config/github.json"), 'r') as f:
        account = json.loads(f.read())
    repo = 'tj'
    gh = connect_to_github(username=account['username'], password=account['password'], repo=repo)
    print(gh)
