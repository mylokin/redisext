from __future__ import absolute_import

import json
import cPickle as pickle


class ISerializer(object):
    pass


class JSON(ISerializer):
    @staticmethod
    def encode(item):
        return json.dumps(item)

    @staticmethod
    def decode(item):
        return json.loads(item)


class String(ISerializer):
    @staticmethod
    def encode(item):
        return str(item)

    @staticmethod
    def decode(item):
        return item


class Numeric(ISerializer):
    @staticmethod
    def encode(item):
        return int(item)

    @staticmethod
    def decode(item):
        return int(item)


class Pickle(ISerializer):
    @staticmethod
    def encode(item):
        return pickle.dumps(item)

    @staticmethod
    def decode(item):
        return pickle.loads(item)
