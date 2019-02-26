#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2019-02-25 16:52
# Author  : gaojiewen
# Version : 1.0
# Desc    : 


import logging
from eadb.android_cmd import AndroidAdb
from eadb.ios_cmd import IOSCmd
from eadb.utils import check_is_none


android = AndroidAdb()
ios = IOSCmd()


def get_connect_devices():
    """
    返回连接设备列表
    :return: 返回连接设备列表
    """
    devices = []
    # 有设备连接才显示
    if not check_is_none(android.ids):
        devices.append(android.ids)
    if not check_is_none(ios.ids):
        devices.append(ios.ids)

    return devices


def print_connect_device():
    """
    {
        "android": ['dsfkjw', 'werwr'],
        "ios": ['ertgffddfg', 'dfgd']
    }
    获取当前连接的 Android 和 iOS 设备
    :return: 设备列表
    """
    print_devices = {}
    # 有设备连接才显示
    if not check_is_none(android.ids):
        print_devices['android'] = android.ids
    if not check_is_none(ios.ids):
        print_devices['ios'] = ios.ids
    return print_devices


def run_device_cmd(fun_name, device_id=None, error_mes=None):
    """
    获得设备相关信息的基础方法，所有命令行均可以套取此方法的使用
    :param fun_name: 相关命令行函数
    :param device_id: 设备号
    :param error_mes: 错误信息
    :return: 设备信息的dict字符串
    """
    device_dict = {}

    # 判断当前设备是否连接为空
    connect_devices = get_connect_devices()
    if check_is_none(device_id) and not check_is_none(connect_devices):
        return run_device_cmd(fun_name, device_id=connect_devices)
    else:
        if type(device_id) is str:
            # 判断当前设备号是 Android 还是 iOS
            if not check_is_none(android.ids) and device_id in android.ids:
                obj = android
            elif not check_is_none(ios.ids) and device_id in ios.ids:
                obj = ios
            else:
                error_mes = r"输入的设备号错误，请重新尝试。"
                logging.error(error_mes)
                raise ValueError(error_mes)

            # 改用getatter方法, 并运行
            device_dict = getattr(obj, fun_name)(id=device_id)

        elif type(device_id) is list:
            devices_dict = {}
            for aid in device_id:
                tmp_dict = run_device_cmd(fun_name, device_id=aid)
                if not check_is_none(tmp_dict):
                    devices_dict.update(tmp_dict)
            device_dict.update(devices_dict)
        else:
            pass

    return device_dict
