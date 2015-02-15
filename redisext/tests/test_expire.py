from __future__ import absolute_import

import redisext.counter
import redisext.key
import redisext.serializer
import redisext.tests.fixture as fixture


class ExpireCounter(fixture.Redis,
                    redisext.counter.Counter,
                    redisext.key.Expire,
                    redisext.serializer.Numeric):
    EXPIRE = 60


class ExpireCounterTestCase(fixture.TestCase):
    def setUp(self):
        self.key = 'key'
        ExpireCounter.increment(self.key)
        ExpireCounter.expire(self.key)

    def test_expire(self):
        self.assertTrue(60 >= ExpireCounter.ttl(self.key) > 0)

    def test_persist(self):
        ExpireCounter.persist(self.key)
        self.assertEqual(ExpireCounter.ttl(self.key), -1)


class UnspecifiedExpireCounter(fixture.Redis,
                               redisext.counter.Counter,
                               redisext.key.Expire,
                               redisext.serializer.Numeric):
    pass


class UnspecifiedExpireCounterTestCase(fixture.TestCase):
    def setUp(self):
        self.key = 'key'

    def test_expire_unspecified(self):
        UnspecifiedExpireCounter.increment(self.key)
        with self.assertRaises(ValueError):
            UnspecifiedExpireCounter.expire(self.key)

    def test_expire_specified(self):
        UnspecifiedExpireCounter.increment(self.key)
        UnspecifiedExpireCounter.expire(self.key, 60)
        self.assertTrue(60 >= UnspecifiedExpireCounter.ttl(self.key) > 0)
