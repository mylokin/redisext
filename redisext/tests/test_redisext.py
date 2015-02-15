#!/usr/bin/env python

import sys
import os.path

CURRENT = os.path.dirname(__file__)
sys.path.insert(0, os.path.realpath(os.path.join(CURRENT, os.pardir, os.pardir)))

import unittest

from redisext.backend.redis import Redis
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


class TestHashMap(TestRedis, HashMap, Pickle):
    KEY = 'hashmap'


class TestMap(TestRedis, Map, Pickle):
    pass


class TestSortedSet(TestRedis, SortedSet, Pickle):
    KEY = 'sortedset'


class TestMultiHashMap(TestRedis, HashMap, Pickle):
    pass


class TestRedisext(unittest.TestCase):

    def tearDown(self):
        TestRedis.connect().flushdb()

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
        self.assertIsNone(TestHashMap.get('non-esixsted'))

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
