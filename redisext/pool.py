from __future__ import absolute_import

import functools

import redisext.utils


class Pool(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        item = cls.connect().spop(key)
        return redisext.utils.decode(cls, item)

    @classmethod
    def push(cls, key, item):
        item = redisext.utils.encode(cls, item)
        return cls.connect().sadd(key, item)


class SortedSet(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def add(cls, key, element, score):
        element = redisext.utils.encode(cls, element)
        cls.connect().zadd(key, score, element)

    @classmethod
    def length(cls, key, start_score, end_score):
        return cls.connect().zcount(key, start_score, end_score)

    @classmethod
    def members(cls, key):
        elements = cls.connect().zrevrange(key, 0, -1)
        if not elements:
            return elements

        decode = functools.partial(redisext.utils.decode, cls)
        return map(decode, elements)

    @classmethod
    def contains(cls, key, element):
        element = redisext.utils.encode(cls, element)
        return cls.connect().zscore(key, element) is not None

    @classmethod
    def truncate(cls, key, size):
        return cls.connect().zremrangebyrank(key, 0, -1 * size - 1)

    @classmethod
    def clean(cls, key):
        return cls.connect().delete(key)
