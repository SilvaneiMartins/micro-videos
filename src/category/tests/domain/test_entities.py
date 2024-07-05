import unittest

from datetime import datetime
from category.domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        category = Category('Movie')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, '')
        self.assertTrue(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)
