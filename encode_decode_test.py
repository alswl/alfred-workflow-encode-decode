# coding=utf-8
import os
from unittest import TestCase

import encode_decode

# force timezone to Asia/Shanghai when running tests
os.environ['TZ'] = 'Asia/Shanghai'


class Test(TestCase):
    def test_encode_url(self):
        res = encode_decode.encode_url('abc')
        self.assertEqual(res, 'abc')

        res = encode_decode.encode_url('&')
        self.assertEqual(res, '%26')

    def test_encode_html(self):
        res = encode_decode.encode_html('abc')
        self.assertEqual(res, 'abc')

        res = encode_decode.encode_html('&')
        self.assertEqual(res, '&amp;')

    def test_encode_base64(self):
        res = encode_decode.encode_base64('abc')
        self.assertEqual(res, 'YWJj')

        res = encode_decode.encode_base64('&')
        self.assertEqual(res, 'Jg==')

    def test_decode_url(self):
        res = encode_decode.decode_url('abc')
        self.assertEqual(res, 'abc')

        res = encode_decode.decode_url('%26')
        self.assertEqual(res, '&')

    def test_decode_html(self):
        res = encode_decode.decode_html('abc')
        self.assertEqual(res, 'abc')

        res = encode_decode.decode_html('&amp;')
        self.assertEqual(res, '&')

    def test_decode_base64(self):
        res = encode_decode.decode_base64('YWJj')
        self.assertEqual(res, 'abc')

        res = encode_decode.decode_base64('Jg==')
        self.assertEqual(res, '&')

    def test_encode_hex(self):
        res = encode_decode.encode_hex('abc')
        self.assertEqual(res, '616263')

        res = encode_decode.encode_hex('&')
        self.assertEqual(res, '26')

        res = encode_decode.encode_hex('你好')
        self.assertEqual(res, 'e4bda0e5a5bd')

    def test_decode_hex(self):
        res = encode_decode.decode_hex('616263')
        self.assertEqual(res, 'abc')

        res = encode_decode.decode_hex('26')
        self.assertEqual(res, '&')

        res = encode_decode.decode_hex('e4bda0e5a5bd')
        self.assertEqual(res, '你好')

    def test_encode_unicode(self):
        res = encode_decode.encode_unicode('abc')
        self.assertEqual(res, '\\u0061\\u0062\\u0063')

        res = encode_decode.encode_unicode('&')
        self.assertEqual(res, '\\u0026')

        res = encode_decode.encode_unicode('你好')
        self.assertEqual(res, '\\u4f60\\u597d')

    def test_decode_unicode(self):
        res = encode_decode.decode_unicode('\\u0061\\u0062\\u0063')
        self.assertEqual(res, 'abc')

        res = encode_decode.decode_unicode('\\u0026')
        self.assertEqual(res, '&')

        res = encode_decode.decode_unicode('\\u4f60\\u597d')
        self.assertEqual(res, '你好')

    def test_encode_timestamp(self):
        res = encode_decode.encode_timestamp('2022-01-01 01:01:01')
        self.assertEqual(res, '1640970061')

        res = encode_decode.encode_timestamp('2022-01-01 01:02')
        self.assertEqual(res, '1640970120')

        res = encode_decode.encode_timestamp('2022-01-02')
        self.assertEqual(res, '1641052800')

        res = encode_decode.encode_timestamp('abc')
        self.assertEqual(res, '')
