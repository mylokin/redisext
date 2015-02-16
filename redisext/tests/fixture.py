from __future__ import absolute_import

import unittest

import redisext.backend.redis


class Connection(redisext.backend.redis.Connection):
    MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}


class TestCase(unittest.TestCase):
    def tearDown(self):
        Connection.connect_to_master().flushdb()


class KeyTestCase(TestCase):
    STORAGE = None

    def test_keys(self):
        key, data = 'key', [{'key': 'value'}, 1, 'string', (1, 2, 3)]
        self.STORAGE(key).push(data)
        self.assertEqual(self.STORAGE(key).pop(), data)
