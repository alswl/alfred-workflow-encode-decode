# coding=utf-8
from unittest import TestCase

import encode_decode


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
