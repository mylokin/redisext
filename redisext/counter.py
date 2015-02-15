from __future__ import absolute_import

import redisext.utils


class Counter(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def increment(cls, key):
        value = cls.connect().incr(key)
        if value and issubclass(cls, redisext.serializer.ISerializable):
            return cls.decode(value)
        else:
            return value

    @classmethod
    def get(cls, key):
        value = cls.connect().get(key)
        if value and issubclass(cls, redisext.serializer.ISerializable):
            return cls.decode(value)
        else:
            return value
