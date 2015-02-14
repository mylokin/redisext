from rm.rmredis import RmRedis
from . import IClient, IRedis


class Client(IClient):
    def __init__(self, database=None, role=None):
        self._redis = RmRedis.get_instance(database, role)


class Redis(IRedis):
    CLIENT = Client
