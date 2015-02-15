from __future__ import absolute_import

import redisext.pool
import redisext.serializer
import redisext.tests.fixture as fixture


class Pool(fixture.Redis,
           redisext.pool.Pool,
           redisext.serializer.Pickle):
    KEY = 'key'


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


class KeyPicklePool(fixture.Redis,
            redisext.pool.Pool,
            redisext.serializer.Pickle):
    pass


class KeyPoolTestCase(fixture.KeyTestCase):
    STORAGE = KeyPicklePool
