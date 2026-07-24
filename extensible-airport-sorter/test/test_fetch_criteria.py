import unittest
from src.fetch_criteria import fetch_criteria

class Test_FetchCriteria(unittest.TestCase):
   def test_fetch_criteria_returns_list_with_name_element(self):
     self.assertIn('name', fetch_criteria())
     
   def test_fetch_criteria_returns_list_with_city_and_name_element(self):
     self.assertIn('city and name', fetch_criteria())
      
if __name__ == '__main__':
  unittest.main()
