from .serializer import ISerializable
from .utils import KeyHandler


class HashMap(object):
    __metaclass__ = KeyHandler
    KEY = None

    @classmethod
    def get(cls, key, hash_key):
        value = cls.connect().hget(key, hash_key)
        return cls.decode(value) if value and issubclass(cls, ISerializable) else value

    @classmethod
    def put(cls, key, hash_key, value):
        if issubclass(cls, ISerializable):
            value = cls.encode(value)
        return cls.connect().hset(key, hash_key, value)

    @classmethod
    def remove(cls, key, hash_key):
        return bool(cls.connect().hdel(key, hash_key))


class Map(object):
    __metaclass__ = KeyHandler

    @classmethod
    def get(cls, key):
        value = cls.connect().get(key)
        return cls.decode(value) if value and issubclass(cls, ISerializable) else value

    @classmethod
    def put(cls, key, value):
        if issubclass(cls, ISerializable):
            value = cls.encode(value)
        return cls.connect().set(key, value)

    @classmethod
    def incr(cls, key, amount=1):
        value = cls.connect().incr(key, amount)
        return cls.decode(value) if value and issubclass(cls, ISerializable) else value

    @classmethod
    def decr(cls, key, amount=1):
        value = cls.connect().decr(key, amount)
        return cls.decode(value) if value and issubclass(cls, ISerializable) else value

    @classmethod
    def remove(cls, key):
        return bool(cls.connect().delete(key))
