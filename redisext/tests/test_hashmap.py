from __future__ import absolute_import

import redisext.hashmap
import redisext.serializer
import redisext.tests.fixture as fixture


class HashMap(fixture.Redis, redisext.hashmap.HashMap):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class HashMapTestCase(fixture.TestCase):
    def test_single_put_into_hashmap(self):
        key, value = 'key1', 'value1'
        HashMap.put(key, value)
        self.assertEqual(HashMap.get(key), value)

    def test_single_removal_from_hashmap(self):
        key, value = 'key1', 'value1'
        HashMap.put(key, value)
        HashMap.remove(key)
        self.assertIsNone(HashMap.get(key))

    def test_multiple_put_and_removal_into_hashmap(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        for key, value in data.iteritems():
            HashMap.put(key, value)
            self.assertEqual(HashMap.get(key), value)
            HashMap.remove(key)
            self.assertIsNone(HashMap.get(key))

    def test_empty_hashmap(self):
        self.assertIsNone(HashMap.get('non-esixsted'))


class Map(fixture.Redis, redisext.hashmap.Map):
    SERIALIZER = redisext.serializer.Pickle


class MapTestCase(fixture.TestCase):
    def test_multiple_map_set(self):
        data = {'map_key1': 'value1', 'map_key2': 'value2'}
        for key, value in data.iteritems():
            Map.put(key, value)
            self.assertEqual(Map.get(key), value)

    def test_empty_map(self):
        key, value = 'key1', 'value1'
        Map.put(key, value)
        Map.remove(key)
        self.assertIsNone(Map.get(key))


class NumericMap(fixture.Redis, redisext.hashmap.Map):
    SERIALIZER = redisext.serializer.Numeric
    KEY = 'key1'


class NumericMapTestCase(fixture.TestCase):
    def test_incr(self):
        NumericMap.incr()
        self.assertEqual(NumericMap.get(), 1)

    def test_decr(self):
        NumericMap.incr()
        NumericMap.decr()
        self.assertEqual(NumericMap.get(), 0)
