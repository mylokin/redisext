Basics
======

Client
------

Redisext uses `Redis <https://pypi.python.org/pypi/redis/>`_ package to execute
raw Redis commands. But it isn't bound to that package because there is abstract
layer that helps to separate Redisext algorithms from Redis client library.

Connection
----------

Redisext do some connections management. It's using most simple model:

#. Open connection on command execution
#. Close connection after command execution

Thus bare Redisext couldn't be used for high-loaded applications, but there is
easy way to solve this problem - your own client with connections pool support :)

Model
-----

Redisext algorithms are concluded into models. Models are implementations of
widely used and well known data structures. Redisext consist of:

* :class:`redisext.counter.Counter`
* :class:`redisext.hashmap.Map`
* :class:`redisext.pool.Pool`
* :class:`redisext.queue.Queue`
* :class:`redisext.stack.Stack`
* ...

This is only part of all awailable models. Some of them undocumented, so you
need to go and check out `sources <https://github.com/mylokin/redisext>`_.

Keys
----

Mostly models suited to work with Redis keys, but sometimes is much more
convenient to predefine key and work with model that behaves like a singleton.
To do that use ``KEY`` attribute::

   class Visitors(Connection, redisext.counter.Counter):
       SERIALIZER = redisext.serializer.Numeric

   class SiteVisitors(Visitors):
       KEY = 'site'

Example::

   >>> SiteVisitors().incr()
   1
   >>> Visitors('site').get()
   1

Serializers
-----------

Redisext have to solve data encoding problem, because Redis support only simple
data structures. Thus you can use your model without serializer and work using
data types supported by you client library or you can use one of this:

* :class:`redisext.serializer.JSON`
* :class:`redisext.serializer.String`
* :class:`redisext.serializer.Numeric`
* :class:`redisext.serializer.Pickle`

.. note::

   Yes, there is no float type - because you don't need it.
