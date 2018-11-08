#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/07 10:00
# @Author  : Nana Xing
# @Site    : 
# @File    : issues_crawler.py
# @Software: PyCharm
from redminelib import Redmine
import os

# #redmine = Redmine('http://api.redmine.meizu.com', username='xingnana',password='xnn0118&&')
# REDMINE_URL = 'http://redmine.meizu.com'
# REDMINE_KEY = 'fb88cc2ee088296f1cfeac00846cdac197cba867'
# redmine = Redmine(REDMINE_URL, key=REDMINE_KEY)
# #redmine = Redmine('http://redmine.meizu.com', key='a4b85b6af28223193f3e89899f23f240dcc7d686')

'''
全局变量：URL，和用户Redmine Key,Authentication:登录Redmine的key
'''
# 声明全局变量
global REDMINE_URL, REDMINE_KEY
REDMINE_URL = 'http://redmine.meizu.com'
REDMINE_KEY = '50fe29df93ea5c125e9ac3cba81d176208d7e9f6'


# 设置用户Redmine Key
def set_redmine_key(redmine_key):
    global REDMINE_KEY  #再次声明，使用全局变量
    REDMINE_KEY = redmine_key


# 根据机型项目名称，获得项目
def get_project(project_name):
    global REDMINE_URL, REDMINE_KEY
    redmine = Redmine(REDMINE_URL, key=REDMINE_KEY)
    project = redmine.project.get(project_name)
    return project

def get_all_issues(project_id):
    global REDMINE_URL, REDMINE_KEY
    redmine = Redmine(REDMINE_URL, key=REDMINE_KEY)
    project = redmine.project.get(project_name)
    issues = redmine.issue.all(project_id=project_id, status_id='*')
    issues = redmine.issue.filter(project_id='M1809')
    issues.export('csv', savepath=os.getcwd())  # 保存到当前目录下


    # today = redmine.issue.filter(project_id='M1809',updated_on="><2018-01-10|2018-03-30" )
    # today.export('csv', savepath=os.getcwd())  # 保存到当前目录下
    # issue = redmine.issue.get(753252, include=['children', 'journals', 'watchers'] )
    # print("问题:",issue.created_on)

    time_entries = redmine.time_entry.all()
    print(time_entries)
    return issues

def gwt_issues_length(issues):
    i =0
    for issue in issues:
        i = i+1
    print(i)


#  Authentication:登录Redmine的key
REDMINE_KEY = '50fe29df93ea5c125e9ac3cba81d176208d7e9f6'
project_name = 'm1811-intl'
set_redmine_key(REDMINE_KEY)
project = get_project(project_name)
print('项目名称，id：', project.name, project.id)

isssues = get_all_issues(project_name)

for issue in isssues:
    print('Issue_Id：', issue.id, issue.subject, project.id)

gwt_issues_length(isssues)
