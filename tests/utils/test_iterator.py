# std
import unittest

# internal
from laz.utils.iterator import Iterator


class TestIter(unittest.TestCase):

    def test_iter(self):
        iterator = Iterator([1, 2, 3])
        self.assertEqual(1, next(iterator).value)
        self.assertEqual(2, next(iterator).value)
        self.assertEqual(3, next(iterator).value)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_is_first(self):
        iterator = Iterator([1, 2, 3])
        self.assertFalse(iterator.is_first)
        self.assertTrue(next(iterator).is_first)
        self.assertFalse(next(iterator).is_first)
        self.assertFalse(next(iterator).is_first)

    def test_is_last(self):
        iterator = Iterator([1, 2, 3])
        self.assertFalse(iterator.is_last)
        self.assertFalse(next(iterator).is_last)
        self.assertFalse(next(iterator).is_last)
        self.assertTrue(next(iterator).is_last)
