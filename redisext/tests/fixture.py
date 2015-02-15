from __future__ import absolute_import

import unittest

import redisext.backend.redis


class Redis(redisext.backend.redis.Redis):
    MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}


class TestCase(unittest.TestCase):
    def tearDown(self):
        Redis.connect().flushdb()


class KeyTestCase(TestCase):
    STORAGE = None

    def test_keys(self):
        key, data = 'key', [{'key': 'value'}, 1, 'string', (1, 2, 3)]
        self.STORAGE.push(key, data)
        self.assertEqual(self.STORAGE.pop(key), data)
