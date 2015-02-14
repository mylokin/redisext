import redisext.backend.abc
import rm.rmredis


class Client(redisext.backend.abc.IClient):
    def __init__(self, database=None, role=None):
        self._redis = rm.rmredis.RmRedis.get_instance(database, role)


class Redis(redisext.backend.abc.IRedis):
    CLIENT = Client
