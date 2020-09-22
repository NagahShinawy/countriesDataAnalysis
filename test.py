# Python code to demonstrate working of unittest
import unittest
from countriesDataAnalysis import get_countries_data

countries_df = get_countries_data()


class TestCountriesAPI(unittest.TestCase):

    rows = countries_df.shape[0]

    def test_existing_data(self):
        self.assertGreater(self.rows, 0)

    def test_numberof_countries(self):
        self.assertEqual(self.rows, 200)


if __name__ == '__main__':
    unittest.main()
