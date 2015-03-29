Contributing
============

Environment Setup
-----------------

Redisext requires installed `Redis <http://redis.io>`_ server.
Tests are using Redis located on *6379* port and db *0*.

Docker Image
------------

Simpliest way to get Redis server instance localy is to use Docker image::

   docker run --name redisext -p 6379:6379 -d redis

.. note::
   This command is bound to ``make redis``.

Docker
------

Check out official Docker documentation available `here <https://docs.docker.com>`_ to get Docker.

OSX Redis Recipe
----------------

Redisext contains helpers to get your Redis server instance as fast as possible.
Pre-requirements:

* Parallels Desktop VM
* Vagrant

To get running redis instance you need to execute:

# cd etc & make
# make

.. note:

   Redisext recipe is only initial setup procedure for Redis server.
   Don't forget to shutdown your container and VM afterall.
   Also this approach requires basic knoledge about Vagrant and Docker
   (for example how to restart your container or VM).
