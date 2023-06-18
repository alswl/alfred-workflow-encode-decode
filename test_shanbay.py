#!/usr/bin/env python
# coding: utf-8


import unittest
from distutils.version import LooseVersion, StrictVersion

import shanbay

class TestShanbay(unittest.TestCase):

    def test__parse_version(self):
        version = LooseVersion('1.5')
        self.assertEqual(1, version.version[0])
        self.assertEqual(5, version.version[1])

    def test__version_compare(self):
        self.assertTrue(LooseVersion('1.4.0') < LooseVersion('1.5.0'))
        self.assertTrue(LooseVersion('1.5.0') == LooseVersion('1.5.0'))
        self.assertTrue(LooseVersion('1.5') < LooseVersion('1.5.0'))
        self.assertTrue(LooseVersion('2.5') > LooseVersion('1.7.0'))
        self.assertTrue(LooseVersion('0.1') < LooseVersion('1.0'))


if __name__ == '__main__':
    unittest.main()

