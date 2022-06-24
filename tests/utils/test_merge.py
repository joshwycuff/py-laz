# std
import unittest

# internal
from laz.utils.merge import merge
from laz.utils.errors import LazTypeError


class TestMerge(unittest.TestCase):

    def test_non_matching_types(self):
        with self.assertRaises(LazTypeError):
            merge({}, [])


class TestMergeLists(unittest.TestCase):

    def test_same_length(self):
        left = [1, 2]
        right = [3, 4]
        merged = merge(left, right)
        self.assertEqual([3, 4], merged)

    def test_left_longer(self):
        left = [1, 2, 3]
        right = [4, 5]
        merged = merge(left, right)
        self.assertEqual([4, 5, 3], merged)

    def test_right_longer(self):
        left = [1, 2]
        right = [3, 4, 5]
        merged = merge(left, right)
        self.assertEqual([3, 4, 5], merged)


class TestMergeDicts(unittest.TestCase):

    def test_dicts_same_keys(self):
        left = {'x': 1, 'y': 2}
        right = {'x': 3, 'y': 4}
        merged = merge(left, right)
        self.assertEqual({'x': 3, 'y': 4}, merged)

    def test_dicts_overlapping_keys(self):
        left = {'x': 1, 'y': 2}
        right = {'y': 3, 'z': 4}
        merged = merge(left, right)
        self.assertEqual({'x': 1, 'y': 3, 'z': 4}, merged)


class TestMergeDeep(unittest.TestCase):

    def test_deep(self):
        left = {'a': 1, 'b': [2], 'c': {'d': 3}}
        right = {'b': [4, 5], 'c': {'d': None, 'e': 6, 'f': [7]}}
        merged = merge(left, right)
        self.assertEqual({'a': 1, 'b': [4, 5], 'c': {'d': 3, 'e': 6, 'f': [7]}}, merged)
