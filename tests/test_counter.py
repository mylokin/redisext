from __future__ import absolute_import

import redisext.counter
import redisext.serializer

from . import fixture


class Counter(fixture.Connection, redisext.counter.Counter):
    KEY = 'key'
    SERIALIZER = redisext.serializer.Numeric


class CounterTestCase(fixture.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_single_increment(self):
        self.counter.increment()
        self.assertEquals(self.counter.get(), 1)

    def test_multiple_increment(self):
        for x in range(10):
            self.counter.increment()
        self.assertEquals(self.counter.get(), 10)

    def test_empty_counter(self):
        self.assertIsNone(self.counter.get())
