from __future__ import absolute_import


class Model(object):
    KEY = None
    CONNECTION = None
    CONNECTION_REUSE = True

    def __init__(self, key=None):
        self.key = key or getattr(self, 'KEY', None)

        self._connection = None
        self._master = None
        self._slave = None

    @classmethod
    def decode(cls, value):
        serializer = getattr(cls, 'SERIALIZER', None)
        if value and serializer:
            return serializer.decode(value)
        else:
            return value

    @classmethod
    def encode(cls, value):
        serializer = getattr(cls, 'SERIALIZER', None)
        if value and serializer:
            return serializer.encode(value)
        else:
            return value

    @property
    def connection(self):
        if not self._connection:
            self._connection = self.CONNECTION
        return self._connection

    def connect_to_master(self):
        if not self.CONNECTION_REUSE:
            return self.connection.connect_to_master()
        if not self._master:
            self._master = self.connection.connect_to_master()
        return self._master

    def connect_to_slave(self):
        if not self.CONNECTION_REUSE:
            return self.connection.connect_to_slave()
        if not self._slave:
            self._slave = self.connection.connect_to_slave()
        return self._slave
