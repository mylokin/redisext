from __future__ import absolute_import

import redisext.queue
import redisext.serializer
import redisext.tests.fixture as fixture


class Queue(fixture.Redis,
            redisext.queue.Queue,
            redisext.serializer.Pickle):
    KEY = 'queue'


class QueueTestCase(fixture.TestCase):
    def test_single_push_to_queue(self):
        item = 1
        Queue.push(item)
        self.assertEqual(Queue.pop(), item)

    def test_multiple_push_to_queue(self):
        data = [1, 2, 3]
        for item in data:
            Queue.push(item)
        for item in data:
            self.assertEqual(Queue.pop(), item)

    def test_empty_counter(self):
        self.assertIsNone(Queue.pop())


class PriorityQueue(fixture.Redis,
                    redisext.queue.PriorityQueue,
                    redisext.serializer.Pickle):
    KEY = 'priority_queue'


class PriorityQueueTestCase(fixture.TestCase):
    def test_push_to_priority_queue(self):
        data = [('a', 1), ('b', 3), ('c', 3)]
        for item in data:
            PriorityQueue.push(*item)
        self.assertEqual(PriorityQueue.pop(), 'a')
        self.assertIn(PriorityQueue.pop(), ['b', 'c'])
        self.assertIn(PriorityQueue.pop(), ['b', 'c'])

    def test_unordered_push_to_priority_queue(self):
        data = [('a', 3), ('b', 2), ('c', 1)]
        for item in data:
            PriorityQueue.push(*item)
        self.assertEqual(PriorityQueue.pop(), 'c')
        self.assertEqual(PriorityQueue.pop(), 'b')
        self.assertEqual(PriorityQueue.pop(), 'a')


class KeyPickleQueue(fixture.Redis,
                     redisext.queue.Queue,
                     redisext.serializer.Pickle):
    pass


class KeyQueueTestCase(fixture.KeyTestCase):
    STORAGE = KeyPickleQueue
