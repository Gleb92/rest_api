import unittest
import main
import requests

test_data = {}
test_data = main.select_all_info_country("Albania")
test_data = test_data["country_name"]

test_data_countries = main.select_all_info()

test_symbol =main.select_all_country_with_starts("Z")

test_population = main.select_all_country_by_population("1000000000")


class TestStringMethods(unittest.TestCase):

    def test_country_name(self):
      self.assertEqual('Albania', test_data)

    def test_duckduckgo_instant_answer_api_search(self):
    # Arrange
        url = 'https://restcountries.eu/rest/v2/all'

        response = requests.get(url)
        assert response.status_code == 200

    def test_len_all_date(self):
        self.assertIn("Albania", test_data_countries)

    def test_assertIn_name(self):
        self.assertIn("Z", test_symbol)

    def test_assertIn_population(self):
        self.assertIn("Chine", test_population)
        
if __name__ == '__main__':
    unittest.main()
 

