from __future__ import absolute_import

import redisext.counter
import redisext.serializer
import redisext.tests.fixture as fixture


class Counter(fixture.Redis, redisext.counter.Counter):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Numeric


class CounterTestCase(fixture.TestCase):
    def test_single_increment(self):
        Counter.increment()
        self.assertEquals(Counter.get(), 1)

    def test_multiple_increment(self):
        for x in xrange(10):
            Counter.increment()
        self.assertEquals(Counter.get(), 10)

    def test_empty_counter(self):
        self.assertIsNone(Counter.get())

if __name__ == '__main__':
    import unittest
    unittest.main()
