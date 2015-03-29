from __future__ import absolute_import

import os
import unittest

import redisext.backend.redis

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)


class Connection(redisext.backend.redis.Connection):
    MASTER = {'host': REDIS_HOST, 'port': REDIS_PORT, 'db': REDIS_DB}


class TestCase(unittest.TestCase):
    def tearDown(self):
        Connection.connect_to_master().flushdb()


class KeyTestCase(TestCase):
    STORAGE = None

    def test_keys(self):
        key, data = 'key', [{'key': 'value'}, 1, 'string', (1, 2, 3)]
        self.STORAGE(key).push(data)
        self.assertEqual(self.STORAGE(key).pop(), data)
