from .serializer import ISerializable
from .utils import KeyHandler


class Queue(object):
    __metaclass__ = KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        item = cls.connect().rpop(key)
        return cls.decode(item) if item and issubclass(cls, ISerializable) else item

    @classmethod
    def push(cls, key, item):
        if issubclass(cls, ISerializable):
            item = cls.encode(item)
        return cls.connect().lpush(key, item)


class PriorityQueue(object):
    __metaclass__ = KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        redis = cls.connect()
        item = redis.zrangebyscore(key, '-inf', '+inf', num=1)
        item = item[0] if item else None
        redis.zrem(key, item)
        return cls.decode(item) if item and issubclass(cls, ISerializable) else item

    @classmethod
    def push(cls, key, item, priority):
        if issubclass(cls, ISerializable):
            item = cls.encode(item)
        return cls.connect().zadd(key, int(priority), item)
