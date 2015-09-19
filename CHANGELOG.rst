.. :changelog:

Changelog
---------

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
