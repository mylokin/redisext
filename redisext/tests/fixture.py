from __future__ import absolute_import

import unittest

import redisext.backend.redis


class Redis(redisext.backend.redis.Redis):
    SETTINGS = {'host': 'localhost', 'port': 6379, 'db': 0}


class TestCase(unittest.TestCase):
    def tearDown(self):
        Redis.connect().flushdb()
