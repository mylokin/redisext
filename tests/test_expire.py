from __future__ import absolute_import

import redisext.counter
import redisext.key
import redisext.serializer

from . import fixture


class ExpireCounter(fixture.Connection,
                    redisext.counter.Counter,
                    redisext.key.Expire,
                    redisext.serializer.Numeric):
    EXPIRE = 60


class ExpireCounterTestCase(fixture.TestCase):
    def setUp(self):
        self.counter = ExpireCounter('key')
        self.counter.increment()
        self.counter.expire()

    def test_expire(self):
        self.assertTrue(60 >= self.counter.ttl() > 0)

    def test_persist(self):
        self.counter.persist()
        self.assertEqual(self.counter.ttl(), -1)


class UnspecifiedExpireCounter(fixture.Connection,
                               redisext.counter.Counter,
                               redisext.key.Expire,
                               redisext.serializer.Numeric):
    pass


class UnspecifiedExpireCounterTestCase(fixture.TestCase):
    def setUp(self):
        self.counter = UnspecifiedExpireCounter('key')

    def test_expire_unspecified(self):
        self.counter.increment()
        with self.assertRaises(ValueError):
            self.counter.expire()

    def test_expire_specified(self):
        self.counter.increment()
        self.counter.expire(60)
        self.assertTrue(60 >= self.counter.ttl() > 0)
