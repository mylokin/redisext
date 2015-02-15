from __future__ import absolute_import

import redisext.serializer
import redisext.utils


class HashMap(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def get(cls, key, hash_key):
        value = cls.connect().hget(key, hash_key)
        if value and issubclass(cls, redisext.serializer.ISerializer):
            return cls.decode(value)
        else:
            return value

    @classmethod
    def put(cls, key, hash_key, value):
        if issubclass(cls, redisext.serializer.ISerializer):
            value = cls.encode(value)
        return cls.connect().hset(key, hash_key, value)

    @classmethod
    def remove(cls, key, hash_key):
        return bool(cls.connect().hdel(key, hash_key))


class Map(object):
    __metaclass__ = redisext.utils.KeyHandler

    @classmethod
    def get(cls, key):
        value = cls.connect().get(key)
        if value and issubclass(cls, redisext.serializer.ISerializer):
            return cls.decode(value)
        else:
            return value

    @classmethod
    def put(cls, key, value):
        if issubclass(cls, redisext.serializer.ISerializer):
            value = cls.encode(value)
        return cls.connect().set(key, value)

    @classmethod
    def incr(cls, key, amount=1):
        value = cls.connect().incr(key, amount)
        if value and issubclass(cls, redisext.serializer.ISerializer):
            return cls.decode(value)
        else:
            return value

    @classmethod
    def decr(cls, key, amount=1):
        value = cls.connect().decr(key, amount)
        if value and issubclass(cls, redisext.serializer.ISerializer):
            return cls.decode(value)
        else:
            return value

    @classmethod
    def remove(cls, key):
        return bool(cls.connect().delete(key))
