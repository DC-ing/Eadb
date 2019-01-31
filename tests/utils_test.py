#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Time    : 2018/10/16 19:39
# Author  : gaojiewen
# Version : 1.0
# Desc    : 测试utils


import unittest
from eadb import utils


class Utils_test(unittest.TestCase):

    def test_run_command(self):
        self.assertIsNotNone(utils.run_command('ls'))

    def test_get_time(self):
        self.assertIsNotNone(utils.get_time())

    def test_check_is_none(self):
        self.assertEqual(True, utils.check_is_none(''))
        self.assertEqual(True, utils.check_is_none(None))
        self.assertEqual(True, utils.check_is_none([]))
        self.assertEqual(False, utils.check_is_none('Test'))
        self.assertEqual(False, utils.check_is_none(['a', 'b']))
