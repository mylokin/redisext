from __future__ import absolute_import

import redisext.hashmap
import redisext.serializer

from . import fixture


class HashMap(fixture.Connection, redisext.hashmap.HashMap):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class HashMapTestCase(fixture.TestCase):
    def setUp(self):
        self.hashmap = HashMap()

    def test_single_put_into_hashmap(self):
        key, value = 'key1', 'value1'
        self.hashmap.put(key, value)
        self.assertEqual(self.hashmap.get(key), value)

    def test_single_removal_from_hashmap(self):
        key, value = 'key1', 'value1'
        self.hashmap.put(key, value)
        self.hashmap.remove(key)
        self.assertIsNone(self.hashmap.get(key))

    def test_multiple_put_and_removal_into_hashmap(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        for key, value in data.items():
            self.hashmap.put(key, value)
            self.assertEqual(self.hashmap.get(key), value)
            self.hashmap.remove(key)
            self.assertIsNone(self.hashmap.get(key))

    def test_empty_hashmap(self):
        self.assertIsNone(self.hashmap.get('non-esixsted'))


class Map(fixture.Connection, redisext.hashmap.Map):
    SERIALIZER = redisext.serializer.Pickle


class MapTestCase(fixture.TestCase):
    def test_multiple_map_set(self):
        data = {'map_key1': 'value1', 'map_key2': 'value2'}
        for key, value in data.items():
            Map(key).put(value)
            self.assertEqual(Map(key).get(), value)

    def test_empty_map(self):
        key, value = 'key1', 'value1'
        Map(key).put(value)
        Map(key).remove()
        self.assertIsNone(Map(key).get())


class NumericMap(fixture.Connection, redisext.hashmap.Map):
    SERIALIZER = redisext.serializer.Numeric
    KEY = 'key1'


class NumericMapTestCase(fixture.TestCase):
    def setUp(self):
        self.numeric_map = NumericMap()

    def test_incr(self):
        self.numeric_map.incr()
        self.assertEqual(self.numeric_map.get(), 1)

    def test_decr(self):
        self.numeric_map.incr()
        self.numeric_map.decr()
        self.assertEqual(self.numeric_map.get(), 0)
