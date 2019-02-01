#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/16 16:58
# Author  : gaojiewen
# Version : 1.0
# Desc    : 辅助工具类

import time
import subprocess
import logging
import json


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
    # 检查str是否为空
    if content is '' or content is None:
        return True
    # 检查list是否为空
    elif type(content) is list and len(content) == 0:
        return True
    # 检查dict是否为空
    elif type(content) is dict and len(content) == 0:
        return True
    else:
        return False


def json_print(dict_str):
    if check_is_none(dict_str):
        return
    try:
        j = json.dumps(dict_str, sort_keys=True, indent=4)
        print(j)
    except ValueError:
        logging.error('输出的json字符串解析失败')
