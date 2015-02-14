import redisext.utils


class Counter(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def increment(cls, key):
        return cls.connect().incr(key)

    @classmethod
    def get(cls, key):
        return cls.connect().get(key)
