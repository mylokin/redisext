Examples
========

Counter
-------

Example of unread messages counter::

   class Unread(redisext.counter.Counter):
       CONNECTION = Connection
       SERIALIZER = redisext.serializer.Numeric

could be used like::

   >>> unread = Unread('messages')
   >>> unread.get()  # key does not exist
   >>> unread.incr()
   1
   >>> unread.incr(5)
   6
   >>> unread.get()
   6

HashMap
-------

Map could be used for simple and direct key's value manipulations.
For example storing Twitter's username::

   class TwitterUsername(redisext.hashmap.Map):
       CONNECTION = Connection
       SERIALIZER = redisext.serializer.String

and use-case::

   >>> TwitterUsername(1).put('mylokin')
   True
   >>> TwitterUsername(1).get()
   u'mylokin'

Map also could be used for cache purposes::

   class Cache(redisext.hashmap.Map):
       CONNECTION = Connection
       SERIALIZER = redisext.serializer.Pickle

use-case example for cache::

   >>> cache = Cache('hash')
   >>> cache.put({'result': 'of', 'cpu intensive': 'calculations'})
   True
   >>> cache.get()
   {'cpu intensive': 'calculations', 'result': 'of'}

.. note::

   Also don't forget to check :class:`redisext.hashmap.HashMap` if you need
   to store more complicated data structures.

Pool
----

The simpliest example of pool usage is token pool::

   class TokenPool(redisext.pool.Pool):
      CONNECTION = Connection
      SERIALIZER = redisext.serializer.String

and this pool could be used like::

   >>> facebook = TokenPool('facebook')
   >>> facebook.push('fb1')
   True
   >>> facebook.push('fb1')
   False
   >>> facebook.push('fb2')
   True
   >>> facebook.pop()
   u'fb1'
   >>> facebook.pop()
   u'fb2'
   >>> facebook.pop()
   >>>

SortedSet
---------

For your special needs check :class:`redisext.pool.SortedSet`.

Queue
-----

Right, task queue::

   class Task(redisext.queue.Queue):
       CONNECTION = Connection
       SERIALIZER = redisext.serializer.Pickle

and it's as simple as looks::

   >>> task_queue = Task('data_processing')
   >>> task_queue.pop()
   >>> task_queue.push({'task': 't1'})
   1L
   >>> task_queue.push({'task': 't2'})
   2L
   >>> task_queue.push({'task': 't3'})
   3L
   >>> task_queue.pop()
   {'task': 't1'}
   >>> task_queue.pop()
   {'task': 't2'}
   >>> task_queue.pop()
   {'task': 't3'}
   >>> task_queue.pop()
   >>>

Here is priority queue as well :class:`redisext.queue.PriorityQueue`.

Lock
----

Lock based on Redis keys existence::

   class TaskLock(redisext.lock.Lock):
       CONNECTION = fixture.Connection

usage::

   >>> TaskLock('task1').acquire()
   True
   >>> TaskLock('task1').acquire()
   False
   >>> TaskLock('task1').release()
   True
   >>> TaskLock('task1').release()
   False

.. note::

   Imports section is intentionaly skiped, but for the order it is listed below::

      import redisext.backend.redis

      class Connection(redisext.backend.redis.Connection):
          MASTER = {'host': 'localhost', 'port': 6379, 'db': 0}
