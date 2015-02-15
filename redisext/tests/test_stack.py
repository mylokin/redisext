from __future__ import absolute_import

import redisext.serializer
import redisext.stack
import redisext.tests.fixture as fixture


class StackTestCase(fixture.TestCase):
    def _stack(self, Stack, data, expect=None):
        for item in data:
            Stack.push(item)
        expect = expect or reversed(data)
        for item in expect:
            self.assertEqual(item, Stack.pop())


class RawStack(fixture.Redis,
               redisext.stack.Stack):
    KEY = 'raw_stack'


class RawStackTestCase(StackTestCase):
    def test_rawstack(self):
        data = ['1', '2', '3']
        self._stack(RawStack, data)

    def test_different_types_for_raw_stack(self):
        data = [1, '2', '3']
        expect = reversed(['1', '2', '3'])
        self._stack(RawStack, data, expect)

    def test_empty_for_raw_stack(self):
        self.assertIsNone(RawStack.pop())


class JSONStack(fixture.Redis,
                redisext.stack.Stack,
                redisext.serializer.JSON):
    KEY = 'json_stack'


class JsonStackTestCase(StackTestCase):
    def test_jsonstack(self):
        data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 'e'}]
        self._stack(JSONStack, data)

    def test_empty_for_json_stack(self):
        self.assertIsNone(JSONStack.pop())


class StringStack(fixture.Redis,
                  redisext.stack.Stack,
                  redisext.serializer.String):
    KEY = 'string_stack'


class StringStackTestCase(StackTestCase):
    def test_string_stack(self):
        data = ['abc', 'qwe']
        self._stack(StringStack, data)

    def test_empty_for_string_stack(self):
        self.assertIsNone(StringStack.pop())


class DecimalStack(fixture.Redis,
                   redisext.stack.Stack,
                   redisext.serializer.Numeric):
    KEY = 'decimal_stack'


class DecimalStackTestCase(StackTestCase):
    def test_decimal_stack(self):
        data = [1, 2, 3]
        self._stack(DecimalStack, data)

    def test_empty_for_decimal_stack(self):
        self.assertIsNone(DecimalStack.pop())


class PickleStack(fixture.Redis,
                  redisext.stack.Stack,
                  redisext.serializer.Pickle):
    KEY = 'stack'


class PickleStackTestCase(StackTestCase):
    def test_pickle_stack(self):
        data = [1, 'a', [1, 2, 3], (1, 2, 3), {'a': 'b'}]
        self._stack(PickleStack, data)

    def test_empty_for_pickle_stack(self):
        self.assertIsNone(PickleStack.pop())


class KeyPickleStack(fixture.Redis,
                     redisext.stack.Stack,
                     redisext.serializer.Pickle):
    pass


class KeyStackTestCase(fixture.KeyTestCase):
    STORAGE = KeyPickleStack
