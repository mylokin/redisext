#!/usr/bin/env python

import sys
import os.path

CURRENT = os.path.dirname(__file__)
sys.path.insert(0, os.path.realpath(os.path.join(CURRENT, os.pardir, os.pardir)))

import unittest

from redisext.backend.redispy import Redis
from redisext.hashmap import (
    HashMap,
    Map,
)
from redisext.pool import (
    Pool,
    SortedSet,
)

from redisext.stack import Stack
from redisext.queue import (
    Queue,
    PriorityQueue,
)
from redisext.serializer import (
    JSON,
    String,
    Numeric,
    Pickle,
)
from redisext.key import Expire


class TestRedis(Redis):
    SETTINGS = {'host': 'localhost', 'port': 6379, 'db': 0}


class TestRawStack(TestRedis, Stack):
    KEY = 'raw_stack'


class TestJSONStack(TestRedis, Stack, JSON):
    KEY = 'json_stack'


class TestStringStack(TestRedis, Stack, String):
    KEY = 'string_stack'


class TestDecimalStack(TestRedis, Stack, Numeric):
    KEY = 'decimal_stack'


class TestStack(TestRedis, Stack, Pickle):
    KEY = 'stack'


class TestPool(TestRedis, Pool, Pickle):
    KEY = 'pool'


class TestQueue(TestRedis, Queue, Pickle):
    KEY = 'queue'


class TestPriorityQueue(TestRedis, PriorityQueue, Pickle):
    KEY = 'priority'


class TestHashMap(TestRedis, HashMap, Pickle):
    KEY = 'hashmap'


class TestMap(TestRedis, Map, Pickle):
    pass


class TestSortedSet(TestRedis, SortedSet, Pickle):
    KEY = 'sortedset'


class TestMultiStack(TestRedis, Stack, Pickle):
    pass


class TestMultiPool(TestRedis, Pool, Pickle):
    pass


class TestMultiQueue(TestRedis, Queue, Pickle):
    pass


class TestMultiPriorityQueue(TestRedis, PriorityQueue, Pickle):
    pass


class TestMultiHashMap(TestRedis, HashMap, Pickle):
    pass


class TestExpire(TestRedis, HashMap, Pickle, Expire):
    EXPIRE = 60


class TestExpireUndefined(TestRedis, HashMap, Pickle, Expire):
    pass


class TestRedisext(unittest.TestCase):

    def tearDown(self):
        TestRedis.connect().flushdb()

    def __stack(self, Stack, data):
        for item in data:
            Stack.push(item)
        for item in reversed(data):
            self.assertEqual(item, Stack.pop())

    def test_rawstack(self):
        data = ['1', '2', '3']
        self.__stack(TestRawStack, data)

    def test_decimalstack(self):
        data = [1, 2, 3]
        self.__stack(TestDecimalStack, data)

    def test_jsonstack(self):
        data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 'e'}]
        self.__stack(TestJSONStack, data)

    def test_stringstack(self):
        data = ['abc', 'qwe']
        self.__stack(TestStringStack, data)

    def test_stack(self):
        data = [1, 'a', [1, 2, 3], (1, 2, 3), {'a': 'b'}]
        self.__stack(TestStack, data)

    def test_pool(self):
        data = [1, 2, 3, 4, {'a': 5}]
        for item in data:
            TestPool.push(item)
        for x in xrange(5):
            self.assertIn(TestPool.pop(), data)

    def test_queue(self):
        data = [1, 2, 3]
        for item in data:
            TestQueue.push(item)
        for item in data:
            self.assertEqual(TestQueue.pop(), item)

    def test_priorityqueue(self):
        data = [('a', 1), ('b', 3), ('c', 3)]
        for item in data:
            TestPriorityQueue.push(*item)
        self.assertEqual(TestPriorityQueue.pop(), 'a')
        self.assertIn(TestPriorityQueue.pop(), ['b', 'c'])
        self.assertIn(TestPriorityQueue.pop(), ['b', 'c'])

    def test_hashmap(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        for key, value in data.iteritems():
            TestHashMap.put(key, value)
            self.assertEqual(TestHashMap.get(key), value)
            TestHashMap.remove(key)
            self.assertIsNone(TestHashMap.get(key))

    def test_sortedset(self):
        data = {'string1': 0, 'string2': 1, 'string3': 2, 'string4': 3}
        for element, score in data.iteritems():
            TestSortedSet.add(element, score)
        self.assertEquals(TestSortedSet.length(0, 3), 4)
        element, score = data.iteritems().next()
        self.assertTrue(TestSortedSet.contains(element))
        expected_members = sorted(data.keys(), reverse=True)
        self.assertEqual(TestSortedSet.members(), expected_members)
        TestSortedSet.truncate(2)
        truncated = sorted(data.keys(), reverse=True)[:-2]
        self.assertEqual(TestSortedSet.members(), truncated)

    def test_empty(self):
        self.assertIsNone(TestPool.pop())
        self.assertIsNone(TestQueue.pop())
        self.assertIsNone(TestPriorityQueue.pop())
        self.assertIsNone(TestStack.pop())
        self.assertIsNone(TestRawStack.pop())
        self.assertIsNone(TestJSONStack.pop())
        self.assertIsNone(TestStringStack.pop())
        self.assertIsNone(TestDecimalStack.pop())
        self.assertIsNone(TestHashMap.get('non-esixsted'))

    def test_multi(self):
        storages = [TestMultiStack, TestMultiPool, TestMultiQueue]
        key, data = 'key', [{'key': 'value'}, 1, 'string', (1, 2, 3)]
        for storage in storages:
            storage.push(key, data)
            self.assertEqual(storage.pop(key), data)
        TestMultiPriorityQueue.push(key, data, 0)
        self.assertEqual(TestMultiPriorityQueue.pop(key), data)

        key, data = 'key', {'key1': 'value1', 'key2': 'value2'}
        for hash_key, value in data.iteritems():
            TestMultiHashMap.put(key, hash_key, value)
            self.assertEqual(TestMultiHashMap.get(key, hash_key), value)

    def test_expire(self):
        key, hash_key, value = 'expire', 'hash_key', 'value'
        TestExpire.put(key, hash_key, value)
        TestExpire.expire(key)
        self.assertTrue(60 >= TestExpire.ttl(key) > 0)
        TestExpire.persist(key)
        self.assertEqual(TestExpire.ttl(key), -1)

    def test_expire_undefined(self):
        key, hash_key, value = 'expire_undefined', 'hash_key', 'value'
        TestExpireUndefined.put(key, hash_key, value)
        self.assertRaises(ValueError, TestExpireUndefined.expire, key)
        TestExpire.expire(key, 60)
        self.assertTrue(60 >= TestExpire.ttl(key) > 0)

    def test_map(self):
        data = {'map_key1': 'value1', 'map_key2': 'value2'}
        for key, value in data.iteritems():
            TestMap.put(key, value)
            self.assertEqual(TestMap.get(key), value)

        TestMap.put(key, value)
        TestMap.remove(key)
        self.assertIsNone(TestMap.get(key))


if __name__ == '__main__':
    unittest.main()
