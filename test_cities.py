import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like 'Santiago, Chile' work?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')