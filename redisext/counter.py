'''
Counter
-------

Model allows to build counters in a minute. For example::

   import redisext.backend.redis
   import redisext.counter
   import redisext.serializer

   class Connection(redisext.backend.redis.Connection):
       MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}

   class Visitors(Connection, redisext.Counter):
       SERIALIZER = redisext.serializer.Numeric


This is it! You can start using it. Example of mythical frontpage view::

   def frontpage():
       visitors_counter = Visitors('fronpage')
       visitors_counter.increment()
       context = {
           'visitors': visitors_counter.get()
       }
       return context


.. note::
   See details about connections and serializers.

Counter API
-----------

.. autoclass:: Counter
   :members:

'''
from __future__ import absolute_import

import redisext.models.abc


class Counter(redisext.models.abc.Model):
    def increment(self):
        ''' Increment counter by 1.

        :returns:
        :rtype: int
        '''
        value = self.connect_to_master().incr(self.key)
        return self.decode(value)

    def get(self):
        ''' Get counter's value.

        :returns: counter's value
        :rtype: int
        '''
        value = self.connect_to_slave().get(self.key)
        return self.decode(value)
