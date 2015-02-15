from __future__ import absolute_import

import unittest

import redisext.backend.abc


class Redis(redisext.backend.abc.IConnection):
    MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}


class TestCase(unittest.TestCase):
    def test_abstract_connection(self):
        with self.assertRaises(NotImplementedError):
            Redis.connect()
