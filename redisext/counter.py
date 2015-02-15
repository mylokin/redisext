from __future__ import absolute_import

import redisext.utils


class Counter(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def increment(cls, key):
        value = cls.connect().incr(key)
        return redisext.utils.decode(cls, value)

    @classmethod
    def get(cls, key):
        value = cls.connect().get(key)
        return redisext.utils.decode(cls, value)
