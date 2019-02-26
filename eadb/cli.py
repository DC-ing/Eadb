#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2019-01-30 14:48
# Author  : gaojiewen
# Version : 1.0
# Desc    : 命令行的配置


import argparse
from eadb.common_cmd import get_connect_devices, print_connect_device, run_device_cmd
from eadb.__about__ import __description__, __version__
from eadb import help_content
from eadb.utils import json_print

parser = argparse.ArgumentParser(description=__description__)


def main_eadb():
    ids = get_connect_devices()
    parser.add_argument('-v', dest='version', action='store_true', help="show version")
    parser.add_argument('--devices', dest='devices', action='store_true', help=help_content.device_id_help)
    parser.add_argument('--name', dest='name', nargs='?', const=ids, help=help_content.device_name_help)
    parser.add_argument('--version', dest='adversion', nargs='?', const=ids, help=help_content.device_version_help)
    parser.add_argument('--screenshot', dest='screenshot', nargs='?', const=ids, help=help_content.screenshot_help)
    parser.add_argument('--info', dest='info', nargs='?', const=ids, help=help_content.info_help)
    parser.add_argument('--size', dest='size', nargs='?', const=ids, help=help_content.wm_size_help)

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    if args.devices:
        json_print(print_connect_device())
        exit(0)

    if args.adversion:
        json_print(run_device_cmd('device_version', device_id=args.adversion))

    if args.name:
        json_print(run_device_cmd('device_name', device_id=args.name))

    if args.screenshot:
        run_device_cmd('device_screenshot', device_id=args.screenshot)

    if args.info:
        json_print(run_device_cmd('device_info', device_id=args.info))

    if args.size:
        json_print(run_device_cmd('device_wm_size', device_id=args.size))


def custom_cmd(func, help=None):
    """
    常用adb命令自定义封装
    :param func: 封装命令函数名称
    :param help: 帮助信息，可以为空
    :return: 返回结果
    """
    parser.add_argument('--id', dest='id', help=help)
    args = parser.parse_args()
    # args.id 可以为空，也可以有值
    content = run_device_cmd(func, device_id=args.id)
    return json_print(content)


def get_devices():
    json_print(print_connect_device())


def get_version():
    custom_cmd('device_version', help=help_content.device_version_help)


def get_screenshot():
    custom_cmd('device_screenshot', help=help_content.screenshot_help)


def get_name():
    custom_cmd('device_name', help=help_content.device_name_help)


def get_info():
    custom_cmd('device_info', help=help_content.info_help)


def get_wm_size():
    custom_cmd('device_wm_size', help=help_content.wm_size_help)


if __name__ == '__main__':
    main_eadb()
