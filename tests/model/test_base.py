# std
import unittest

# internal
from laz.model.base import BaseObject


class TestBaseObject(unittest.TestCase):

    def test_stack_push(self):
        obj = BaseObject('name')
        with self.subTest('Empty data'):
            self.assertEqual({}, obj.data)
        obj.push({'x': 1})
        with self.subTest('Pushed data'):
            self.assertEqual({'x': 1}, obj.data)
        obj.pop()
        with self.subTest('Popped data'):
            self.assertEqual({}, obj.data)
