from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Household


class HouseholdModelTests(TestCase):
    def test_create_household(self):
        h = Household.objects.create(name="Test House")
        self.assertEqual(h.name, "Test House")
        self.assertIsNotNone(h.created_at)

    def test_str_returns_name(self):
        h = Household.objects.create(name="My Place")
        self.assertEqual(str(h), "My Place")

    def test_name_max_length_enforced(self):
        h = Household(name="x" * 151)
        with self.assertRaises(ValidationError):
            h.full_clean()

    def test_name_required(self):
        h = Household(name="")
        with self.assertRaises(ValidationError):
            h.full_clean()

    def test_multiple_households_coexist(self):
        h1 = Household.objects.create(name="House A")
        h2 = Household.objects.create(name="House B")
        self.assertEqual(Household.objects.count(), 2)
        self.assertNotEqual(h1.id, h2.id)
