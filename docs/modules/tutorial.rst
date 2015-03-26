Tutorial
========

Counter Model allows you to build counters in a minute. For example::

   import redisext.backend.redis
   import redisext.counter
   import redisext.serializer

   class Connection(redisext.backend.redis.Connection):
       MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}

   class Visitors(Connection, redisext.counter.Counter):
       SERIALIZER = redisext.serializer.Numeric


This is it! You can start using it. Example of mythical frontpage view::

   def frontpage():
       visitors_counter = Visitors('fronpage')
       visitors_counter.incr()
       context = {
           'visitors': visitors_counter.get()
       }
       return context

.. note::

   Details on :class:`redisext.counter.Counter`.
