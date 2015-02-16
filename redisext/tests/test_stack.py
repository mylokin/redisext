from __future__ import absolute_import

import redisext.serializer
import redisext.stack
import redisext.tests.fixture as fixture


class StackTestCase(fixture.TestCase):
    def _stack(self, stack, data, expect=None):
        for item in data:
            stack.push(item)
        expect = expect or reversed(data)
        for item in expect:
            self.assertEqual(item, stack.pop())


class RawStack(fixture.Connection, redisext.stack.Stack):
    KEY = 'raw_stack'


class RawStackTestCase(StackTestCase):
    def setUp(self):
        self.raw_stack = RawStack()

    def test_rawstack(self):
        data = ['1', '2', '3']
        self._stack(self.raw_stack, data)

    def test_different_types_for_raw_stack(self):
        data = [1, '2', '3']
        expect = reversed(['1', '2', '3'])
        self._stack(self.raw_stack, data, expect)

    def test_empty_for_raw_stack(self):
        self.assertIsNone(self.raw_stack.pop())


class JSONStack(fixture.Connection, redisext.stack.Stack):
    KEY = 'json_stack'
    SERIALIZER = redisext.serializer.JSON


class JsonStackTestCase(StackTestCase):
    def setUp(self):
        self.json_stack = JSONStack()

    def test_jsonstack(self):
        data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 'e'}]
        self._stack(self.json_stack, data)

    def test_empty_for_json_stack(self):
        self.assertIsNone(self.json_stack.pop())


class StringStack(fixture.Connection, redisext.stack.Stack):
    KEY = 'string_stack'
    SERIALIZER = redisext.serializer.String


class StringStackTestCase(StackTestCase):
    def setUp(self):
        self.string_stack = StringStack()

    def test_string_stack(self):
        data = ['abc', 'qwe']
        self._stack(self.string_stack, data)

    def test_empty_for_string_stack(self):
        self.assertIsNone(self.string_stack.pop())


class DecimalStack(fixture.Connection, redisext.stack.Stack):
    KEY = 'decimal_stack'
    SERIALIZER = redisext.serializer.Numeric


class DecimalStackTestCase(StackTestCase):
    def setUp(self):
        self.decimal_stack = DecimalStack()

    def test_decimal_stack(self):
        data = [1, 2, 3]
        self._stack(self.decimal_stack, data)

    def test_empty_for_decimal_stack(self):
        self.assertIsNone(self.decimal_stack.pop())


class PickleStack(fixture.Connection, redisext.stack.Stack):
    KEY = 'stack'
    SERIALIZER = redisext.serializer.Pickle


class PickleStackTestCase(StackTestCase):
    def setUp(self):
        self.pickle_stack = PickleStack()

    def test_pickle_stack(self):
        data = [1, 'a', [1, 2, 3], (1, 2, 3), {'a': 'b'}]
        self._stack(self.pickle_stack, data)

    def test_empty_for_pickle_stack(self):
        self.assertIsNone(self.pickle_stack.pop())


class KeyPickleStack(fixture.Connection, redisext.stack.Stack):
    SERIALIZER = redisext.serializer.Pickle


class KeyStackTestCase(fixture.KeyTestCase):
    STORAGE = KeyPickleStack
