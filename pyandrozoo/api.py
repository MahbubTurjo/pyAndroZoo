#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

import requests

ANDROZOO_URL = 'https://androzoo.uni.lu/api/download'

class pyAndroZoo():
    def __init__(self, apikey=None, url=ANDROZOO_URL):
        self.root_url = url
        self.apikey = apikey or os.getenv('androzoo_api_key', default=None)
        self.payload = {'apikey': self.apikey}

    def get(self, sha256):
        payload = {'sha256': sha256}
        payload.update(self.payload)
        with open(sha256+'.apk', "wb") as apk_file:
            r = requests.get(self.root_url, payload)
            apk_file.write(r.content)
            return r
