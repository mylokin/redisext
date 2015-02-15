from __future__ import absolute_import

import redisext.utils


class Expire(object):
    __metaclass__ = redisext.utils.KeyHandler
    EXPIRE = None

    @classmethod
    def expire(cls, key, seconds=None):
        if seconds is None:
            try:
                seconds = int(cls.EXPIRE)
            except TypeError:
                raise ValueError(seconds)
        return cls.connect().expire(key, seconds)

    @classmethod
    def ttl(cls, key):
        return cls.connect().ttl(key)

    @classmethod
    def persist(cls, key):
        return cls.connect().persist(key)
