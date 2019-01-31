#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/16 16:58
# Author  : gaojiewen
# Version : 1.0
# Desc    : 辅助工具类

import time
import subprocess


def run_command(cmd):
    """
    运行系统命令
    :param cmd: 命令
    :return: 运行命令后返回的信息
    """
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = output.stdout.read().decode(encoding='utf-8')
    output.kill()
    return result


def get_time():
    """
    获取指定格式的当前字符串，如：20181016-162638
    :return: 当前时间字符串
    """
    return time.strftime(r'%Y%m%d-%H%M%S', time.localtime())


def check_is_none(content):
    """
    检查指定的信息是否为空
    :param content: 检查的信息
    :return: 是否为空
    """
    if content is '' or content is None:
        return True
    elif type(content) is list and len(content) == 0:
        return True
    else:
        return False
