from __future__ import absolute_import

import redisext.pool
import redisext.serializer
import redisext.tests.fixture as fixture


class Pool(fixture.Redis, redisext.pool.Pool):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class PoolTestCase(fixture.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, {'a': 5}]
        self.length = len(self.data)
        for item in self.data:
            Pool.push(item)

    def test_pool_single_pop(self):
        self.assertIn(Pool.pop(), self.data)

    def test_pool_multiple_pop(self):
        for x in xrange(self.length):
            self.assertIn(Pool.pop(), self.data)


class EmptyPoolTestCase(fixture.TestCase):
    def test_empty_pool(self):
        self.assertIsNone(Pool.pop())


class KeyPicklePool(fixture.Redis, redisext.pool.Pool):
    SERIALIZER = redisext.serializer.Pickle


class KeyPoolTestCase(fixture.KeyTestCase):
    STORAGE = KeyPicklePool


class SortedSet(fixture.Redis, redisext.pool.SortedSet):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Pickle


class SortedSetTestCase(fixture.TestCase):
    def setUp(self):
        self.data = {'string1': 0, 'string2': 1, 'string3': 2, 'string4': 3}
        for element, score in self.data.iteritems():
            SortedSet.add(element, score)

    def test_sortedset_multiple_add(self):
        self.assertEquals(SortedSet.length(0, 3), 4)

    def test_sortedset_element_availability(self):
        element, score = self.data.iteritems().next()
        self.assertTrue(SortedSet.contains(element))

    def test_sortedset_members(self):
        expected_members = sorted(self.data.keys(), reverse=True)
        self.assertEqual(SortedSet.members(), expected_members)

    def test_sortedset_truncated_members(self):
        SortedSet.truncate(2)
        truncated = sorted(self.data.keys(), reverse=True)[:-2]
        self.assertEqual(SortedSet.members(), truncated)

    def test_sortedset_clean(self):
        SortedSet.clean()
        self.assertEqual(SortedSet.members(), [])


class EmptySortedSetTestCase(fixture.TestCase):
    def test_empty_sorted_set(self):
        self.assertEqual(SortedSet.members(), [])
