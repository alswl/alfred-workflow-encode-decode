#!/usr/bin/env python
# coding: utf-8


import unittest
import shanbay


class ITShanbay(unittest.TestCase):

    def test_is_upgrade_availabe(self):
        self.assertFalse(shanbay.is_upgrade_available())

    def test_resolve_dns(self):
        self.assertEqual('1.6.1.0', shanbay._resolve_dns(shanbay.VERSION_DOMAIN))

    def test_fetch_version_by_domain(self):
        self.assertEqual('1.6.1', shanbay._fetch_version_by_domain(shanbay.VERSION_DOMAIN))


if __name__ == '__main__':
    unittest.main()
