from __future__ import absolute_import

import redisext.serializer
import redisext.utils


class Stack(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        item = cls.connect().lpop(key)
        if item and issubclass(cls, redisext.serializer.ISerializable):
            return cls.decode(item)
        else:
            return item

    @classmethod
    def push(cls, key, item):
        if issubclass(cls, redisext.serializer.ISerializable):
            item = cls.encode(item)
        return cls.connect().lpush(key, item)
