from __future__ import absolute_import

import redisext.pool
import redisext.serializer

from . import fixture


class Pool(fixture.Connection, redisext.pool.Pool):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class PoolTestCase(fixture.TestCase):
    def setUp(self):
        self.pool = Pool()
        self.data = [1, 2, 3, 4, {'a': 5}]
        self.length = len(self.data)
        for item in self.data:
            self.pool.push(item)

    def test_pool_single_pop(self):
        self.assertIn(self.pool.pop(), self.data)

    def test_pool_multiple_pop(self):
        for x in xrange(self.length):
            self.assertIn(self.pool.pop(), self.data)


class EmptyPoolTestCase(fixture.TestCase):
    def test_empty_pool(self):
        self.assertIsNone(Pool().pop())


class KeyPicklePool(fixture.Connection, redisext.pool.Pool):
    SERIALIZER = redisext.serializer.Pickle


class KeyPoolTestCase(fixture.KeyTestCase):
    STORAGE = KeyPicklePool


class SortedSet(fixture.Connection, redisext.pool.SortedSet):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class SortedSetTestCase(fixture.TestCase):
    def setUp(self):
        self.data = {'string1': 0, 'string2': 1, 'string3': 2, 'string4': 3}
        self.sortedset = SortedSet()
        for element, score in self.data.iteritems():
            self.sortedset.add(element, score)

    def test_sortedset_multiple_add(self):
        self.assertEquals(self.sortedset.length(0, 3), 4)

    def test_sortedset_element_availability(self):
        element, score = self.data.iteritems().next()
        self.assertTrue(self.sortedset.contains(element))

    def test_sortedset_members(self):
        expected_members = sorted(self.data.keys(), reverse=True)
        self.assertEqual(self.sortedset.members(), expected_members)

    def test_sortedset_truncated_members(self):
        self.sortedset.truncate(2)
        truncated = sorted(self.data.keys(), reverse=True)[:-2]
        self.assertEqual(self.sortedset.members(), truncated)

    def test_sortedset_clean(self):
        self.sortedset.clean()
        self.assertEqual(self.sortedset.members(), [])


class EmptySortedSetTestCase(fixture.TestCase):
    def test_empty_sorted_set(self):
        self.assertEqual(SortedSet().members(), [])
