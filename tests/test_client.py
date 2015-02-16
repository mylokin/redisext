from __future__ import absolute_import

import unittest

import redisext.backend.abc
import redisext.backend.redis


class Connection(redisext.backend.abc.IConnection):
    MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}


class IConnectionTestCase(unittest.TestCase):
    def test_abstract_connection(self):
        with self.assertRaises(NotImplementedError):
            Connection.connect_to_master()


class ReplicatedConnection(redisext.backend.redis.Connection):
    MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}
    SLAVE = {'host': 'localhost', 'port': 6379, 'db': 1}


class ReplicatedConnectionTestCase(unittest.TestCase):
    def tearDown(self):
        ReplicatedConnection.connect_to_master().flushdb()
        ReplicatedConnection.connect_to_slave().flushdb()

    def test_slave(self):
        ReplicatedConnection.connect_to_master().set('key', 'value')
        self.assertIsNone(ReplicatedConnection.connect_to_slave().get('key'))
