#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/16 19:39
# Author  : gaojiewen
# Version : 1.0
# Desc    : 测试adb.py


import unittest
from eadb import adb


class Adb_test(unittest.TestCase):

    def setUp(self):
        self.adb = adb.AndroidAdb()

    def test_get_devices(self):
        print(self.adb.devices())
        self.assertIsNotNone(self.adb.devices())

