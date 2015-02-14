import redisext.utils
import redisext.serializer


class Pool(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def pop(cls, key):
        item = cls.connect().spop(key)
        return cls.decode(item) if item and issubclass(cls, redisext.serializer.ISerializable) else item

    @classmethod
    def push(cls, key, item):
        if issubclass(cls, redisext.serializer.ISerializable):
            item = cls.encode(item)
        return cls.connect().sadd(key, item)


class SortedSet(object):
    __metaclass__ = redisext.utils.KeyHandler
    KEY = None

    @classmethod
    def add(cls, key, element, score):
        if issubclass(cls, redisext.serializer.ISerializable):
            element = cls.encode(element)
        cls.connect().zadd(key, score, element)

    @classmethod
    def length(cls, key, start_score, end_score):
        return cls.connect().zcount(key, start_score, end_score)

    @classmethod
    def members(cls, key):
        elements = cls.connect().zrevrange(key, 0, -1)
        if elements and issubclass(cls, redisext.serializer.ISerializable):
            return map(cls.decode, elements)
        else:
            return elements

    @classmethod
    def contains(cls, key, element):
        if issubclass(cls, redisext.serializer.ISerializable):
            element = cls.encode(element)
        return cls.connect().zscore(key, element) is not None

    @classmethod
    def truncate(cls, key, size):
        return cls.connect().zremrangebyrank(key, 0, -1 * size - 1)

    @classmethod
    def clean(cls, key):
        return cls.connect().delete(key)
