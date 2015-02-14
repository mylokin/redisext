from .serializer import ISerializable
from .utils import KeyHandler


class Stack(object):
    __metaclass__ = KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        item = cls.connect().lpop(key)
        return cls.decode(item) if item and issubclass(cls, ISerializable) else item

    @classmethod
    def push(cls, key, item):
        if issubclass(cls, ISerializable):
            item = cls.encode(item)
        return cls.connect().lpush(key, item)
