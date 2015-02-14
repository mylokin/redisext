import json
import cPickle as pickle


class ISerializable(object):
    pass


class JSON(ISerializable):
    @classmethod
    def encode(cls, item):
        return json.dumps(item)

    @classmethod
    def decode(cls, item):
        return json.loads(item)


class String(ISerializable):
    @classmethod
    def encode(cls, item):
        return str(item)

    @classmethod
    def decode(cls, item):
        return item


class Numeric(ISerializable):
    @classmethod
    def encode(cls, item):
        return int(item)

    @classmethod
    def decode(cls, item):
        return int(item)


class Pickle(ISerializable):
    @classmethod
    def encode(cls, item):
        return pickle.dumps(item)

    @classmethod
    def decode(cls, item):
        return pickle.loads(item)
