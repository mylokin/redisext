'''
Counter
^^^^^^^

.. autoclass:: Counter
   :members:

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

    def increment(self):
        ''' Increment counter by 1.

        :returns: counter's value
        :rtype: int
        '''
        value = self.connect_to_master().incr(self.key)
        return self.decode(value)
