#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2019-01-30 14:48
# Author  : gaojiewen
# Version : 1.0
# Desc    : 命令行的配置


import argparse
from eadb.adb import AndroidAdb
from eadb.__about__ import __description__, __version__
from eadb.help_content import device_name_help, device_version_help, screenshot_help, device_id_help
from eadb.utils import json_print


myadb = AndroidAdb()
parser = argparse.ArgumentParser(description=__description__)


def main_eadb():
    parser.add_argument('-v', dest='version', action='store_true', help="show version")
    parser.add_argument('--devices', dest='devices', action='store_true', help=device_id_help)
    parser.add_argument('--name', nargs='?', const=myadb.ids, dest='name', help=device_name_help)
    parser.add_argument('--version', nargs='?', const=myadb.ids, dest='adversion', help=device_version_help)
    parser.add_argument('--screenshot', nargs='?', const=myadb.ids, dest='screenshot', help=screenshot_help)

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    if args.devices:
        print(myadb.ids)
        exit(0)

    if args.adversion:
        json_print(myadb.versions(id=args.adversion))

    if args.name:
        json_print(myadb.deviceNames(id=args.name))

    if args.screenshot:
        myadb.screenshot(id=args.screenshot)


def custom_cmd(fun_name, help=None):
    """
    常用adb命令自定义封装
    :param fun_name: adb封装命令函数名
    :param help: 帮助信息，可以为空
    :return: 返回结果
    """
    parser.add_argument('--id', dest='id', help=help)
    args = parser.parse_args()
    content = getattr(myadb, fun_name)(id=args.id)
    return json_print(content)


def get_version():
    custom_cmd(myadb.versions.__name__, help=device_version_help)


def get_screenshot():
    custom_cmd(myadb.screenshot.__name__, help=screenshot_help)


def get_device_name():
    custom_cmd(myadb.deviceNames.__name__, help=device_name_help)


if __name__ == '__main__':
    main_eadb()
