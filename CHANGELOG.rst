.. :changelog:

Changelog
---------

1.3.8 (2016-01-08)
++++++++++++++++++

- Add ``contains`` to Pool
- Fix major ``rename`` bug

1.3.7 (2016-01-08)
++++++++++++++++++

- Add ``rename`` to IClient
- Add ``redisext.key.Key`` mixin with ``rename`` method

1.3.6 (2016-01-08)
++++++++++++++++++

- Add ``pipeline`` to IClient

1.3.5 (2016-01-08)
++++++++++++++++++

- Add ``members`` to Pool

1.3.4 (2015-10-09)
++++++++++++++++++

- Add ``randomkey`` to IClient


1.3.3 (2015-09-20)
++++++++++++++++++

- Add ``with_scores`` param

1.3.2 (2015-09-18)
++++++++++++++++++

- Add ``rem`` to SortedSet

1.3.1 (2015-09-17)
++++++++++++++++++

- Fix missed packages

1.3.0 (2015-09-17)
++++++++++++++++++

- Add DSN support

1.2.5 (2015-08-15)
++++++++++++++++++

- Add ``clean_by_score`` to SortedSet


1.2.4 (2015-08-15)
++++++++++++++++++

- Add ``members_by_score`` to SortedSet

1.2.3 (2015-04-19)
++++++++++++++++++

- Add ``items`` method to queue
- Add ``ltrim`` method to abstract redis connection

1.2.2 (2015-04-19)
++++++++++++++++++

- Add ``size`` method to queue

1.2.1 (2015-04-03)
++++++++++++++++++

- Rename ``put`` to ``set`` in ``redisext.hashmap``
- Method ``exists`` method to ``Map``
- Connections re-use
- Add ``Lock``

1.2.0 (2015-04-02)
++++++++++++++++++

- Connection object uses through CONNECTION attribute, instead of inheritance
