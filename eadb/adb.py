#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/15 18:23
# Author  : gaojiewen
# Version : 1.0
# Desc    : 封装 adb 常用命令


import re
import os
import logging
from eadb.utils import check_is_none, get_time, run_command


class AndroidAdb(object):

    def __init__(self):
        check_adb_is_ok = run_command('adb start-server')
        if 'command not found' in check_adb_is_ok:
            logging.error(r'请添加 ANDROID_HOME 环境变量')
            raise EnvironmentError(r'Please set ANDROID_HOME first.')
        self.ids = self.devices()

    def devices(self):
        """
        获取当前连接的设备
        :return: 设备列表
        """
        devices = []
        output = run_command('adb devices')
        lines = output.split('\n')
        for i in range(1, len(lines)):
            if 'device' in lines[i]:
                devices.append(lines[i].replace('\tdevice', ''))
        logging.info(r'获取到已连接的设备：{0}'.format(devices))
        if check_is_none(devices):
            logging.warning(r'当前无设备连接')
        return devices

    def deviceNames(self, id=None):
        """
        获取指定设备的名称
        :param id: 设备 id
        :return: 设备名称
        """
        name_dict = {}
        if check_is_none(id) and not check_is_none(self.ids):
            # 如果不指定设备号且当前有连接设备，默认全部获取当前连接所有设备的名称
            return self.deviceNames(id=self.ids)
        else:
            if type(id) is str:
                model = run_command('adb -s {0} shell getprop ro.product.model'.format(id)).replace(' ', '_')
                model = re.sub('\r\n|\n', '', model)
                brand = run_command('adb -s {0} shell getprop ro.product.brand'.format(id))
                brand = re.sub('\r\n|\n', '', brand)
                # 找到字符串返回0，找不到返回-1
                if model.find(brand) == 0:
                    name_dict[id] = model.replace('_', '-')
                else:
                    name_dict[id] = '{0}-{1}'.format(brand, model)
                logging.info(r"获取到设备'{0}'的名称：'{1}'".format(id, name_dict))
            elif type(id) is list:
                names_dict = {}
                for aid in id:
                    names_dict.update(self.deviceNames(id=aid))
                name_dict.update(names_dict)
            else:
                logging.error(r'获取设备名称失败')
        return name_dict

    def versions(self, id=None):
        """
        获取指定设备的系统版本
        :param id: 设备 id
        :return: 系统版本
        """
        version_dict = {}
        if check_is_none(id) and not check_is_none(self.ids):
            # 如果不指定设备号且当前有连接设备，默认全部获取当前连接所有设备的版本号
            return self.versions(id=self.ids)
        else:
            if type(id) is str:
                version = run_command('adb -s {0} shell getprop ro.build.version.release'.format(id))
                version_dict[id] = re.sub('\r\n|\n', '', version)
                logging.info(r"获取到设备'{0}'的系统版本号为'{1}'".format(id, version))
            elif type(id) is list:
                versions_dict = {}
                for aid in id:
                    versions_dict.update(self.versions(id=aid))
                version_dict.update(versions_dict)
            else:
                logging.error(r'获取设备版本号失败')
        return version_dict

    def screenshot(self, id=None):
        """
        对指定设备进行截屏，并放到电脑的桌面上
        :param id: 设备号
        """
        if check_is_none(id) and not check_is_none(self.ids):
            # 如果不指定设备号且当前有连接设备，默认全部获取当前连接所有设备的版本号
            return self.screenshot(id=self.ids)
        else:
            if type(id) is str:
                device_name = self.deviceNames(id)[id]
                version = self.versions(id)[id]
                screen_file = '{0}-{1}-{2}.png'.format(device_name, version, get_time())
                screen_path = '{0}/Desktop/{1}'.format(os.environ['HOME'], screen_file)
                logging.info(r'截图存放路径：{0}'.format(screen_path))
                screen_in_device = '/sdcard/{0}'.format(screen_file)
                run_command('adb -s {0} shell screencap {1}'.format(id, screen_in_device))
                run_command('adb -s {0} pull {1} {2}'.format(id, screen_in_device, screen_path))
                run_command('adb -rs {0} shell rm {1}'.format(id, screen_in_device))
                print(r"'{0}'截屏成功，存放路径为'{1}'".format(device_name, screen_path))
            elif type(id) is list:
                for aid in id:
                    self.screenshot(id=aid)
            else:
                logging.error(r'截屏失败')
