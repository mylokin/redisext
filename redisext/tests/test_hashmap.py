from __future__ import absolute_import

import redisext.hashmap
import redisext.serializer
import redisext.tests.fixture as fixture


class HashMap(fixture.Redis,
              redisext.hashmap.HashMap,
              redisext.serializer.Pickle):
    KEY = 'key'


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
