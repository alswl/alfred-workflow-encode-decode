#!/usr/bin/env python
# coding: utf-8

import argparse
import base64
import html
import json
import os
import socket
import urllib.error
import urllib.request
from distutils.version import LooseVersion
from urllib.parse import urlparse, urlencode

from workflow import Workflow

TOKEN_FILE = os.path.abspath('token')
ALFRED_WORD_AUDIO_MP3_FILE = '/tmp/alfred_word_audio.mp3'


VERSION_DOMAIN = 'alfred-workflow-encode-decode-version.alswl.com'


def _get_current_version():
    with open('./VERSION', 'r') as version_file:
        return version_file.read().strip()


CURRENT_VERSION = _get_current_version()


def _request(path, params=None, method='GET', data=None, headers=None):
    params = params or {}
    headers = headers or {}
    if params:
        url = path + '?' + urlencode(params)
    else:
        url = path

    request = urllib.request.Request(url, data, headers)
    request.get_method = lambda: method
    response = urllib.request.urlopen(request)
    return response.read()


def _api(path, params=None, method='GET', data=None, headers=None):
    response = _request(path=path, params=params, method=method, data=data,
                        headers=headers)
    result = json.loads(response)
    if result['status_code'] != 0:
        return None
    return result['data']


def _fetch_version_by_domain(domain):
    """
    eg. request ip is 1.5.0.0, but replace `.0$` to ``, then return 1.5.0
    :param domain: 
    :return: version
    """
    ip = _resolve_dns(domain)
    if ip is None:
        return ip
    return ip[:-2]


def _resolve_dns(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None


def is_upgrade_available():
    available_version = _fetch_version_by_domain(VERSION_DOMAIN)
    if available_version is None:
        return False

    current_version = CURRENT_VERSION
    return LooseVersion(available_version) > LooseVersion(current_version)


def encode_url(text: str) -> str:
    return urllib.parse.quote(text)


def encode_html(text: str) -> str:
    return html.escape(text)


def encode_base64(text: str) -> str:
    bs = base64.b64encode(text.encode('utf-8'))
    return bs.decode('utf-8')


def decode_url(text: str) -> str:
    return urllib.parse.unquote(text)


def decode_html(text: str) -> str:
    return html.unescape(text)


def decode_base64(text: str) -> str:
    bs = base64.b64decode(text.encode('utf-8'))
    return bs.decode('utf-8')


def encode(text: str):
    wf = Workflow()
    encoded_url = encode_url(text)
    encoded_html = encode_html(text)
    encoded_based64 = encode_base64(text)
    wf.add_item(title=encoded_url, arg=encoded_url, subtitle='URL encoded', valid=True)
    wf.add_item(title=encoded_html, arg=encoded_html, subtitle='HTML encoded', valid=True)
    wf.add_item(title=encoded_based64, arg=encoded_based64, subtitle='base64 encoded', valid=True)
    wf.send_feedback()


def decode(text: str):
    wf = Workflow()
    decoded_url = decode_url(text)
    decoded_html = decode_html(text)
    decoded_based64 = decode_base64(text)
    wf.add_item(title=decoded_url, arg=decoded_url, subtitle='URL decoded', valid=True)
    wf.add_item(title=decoded_html, arg=decoded_html, subtitle='HTML decoded', valid=True)
    wf.add_item(title=decoded_based64, arg=decoded_based64, subtitle='base64 decoded', valid=True)
    wf.send_feedback()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--encode', nargs='?', type=str)
    parser.add_argument('--decode', nargs='?', type=str)
    args = parser.parse_args()

    if args.encode:
        encode(args.encode)
    elif args.decode:
        decode(args.decode)
    else:
        raise ValueError()


if __name__ == '__main__':
    main()
