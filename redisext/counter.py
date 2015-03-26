'''
Counter
-------

.. autoclass:: Counter
   :members:

Example of unread messages counter::

   import redisext.backend.redis
   import redisext.counter
   import redisext.serializer

   class Connection(redisext.backend.redis.Connection):
       MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}

   class Unread(Connection, redisext.counter.Counter):
       SERIALIZER = redisext.serializer.Numeric

could be used like::

   >>> unread = Unread('messages')
   >>> unread.get()
   >>> unread.incr()
   1
   >>> unread.incr(5)
   6
   >>> unread.get()
'''
from __future__ import absolute_import

import redisext.models.abc


class Counter(redisext.models.abc.Model):
    def get(self):
        ''' Get counter's value.

        :returns: counter's value
        :rtype: int
        '''
        value = self.connect_to_slave().get(self.key)
        return self.decode(value)

    def incr(self, value=1):
        ''' Increment counter by `value`.

        :param value: int -- value to add

        :returns: counter's value
        :rtype: int
        '''
        value = self.connect_to_master().incr(self.key, value)
        return self.decode(value)
