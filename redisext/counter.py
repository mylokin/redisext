from .utils import KeyHandler


class Counter(object):
    __metaclass__ = KeyHandler
    KEY = None

    @classmethod
    def increment(cls, key):
        return cls.connect().incr(key)

    @classmethod
    def get(cls, key):
        return cls.connect().get(key)
