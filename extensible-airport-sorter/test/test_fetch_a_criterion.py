import unittest
from src.fetch_a_criterion import fetch_a_criterion
from src.sorting_criteria.sorting_criteria_name import criteria_to_sort_on as criteria_to_sort_on_name 
from src.sorting_criteria.sorting_criteria_city import criteria_to_sort_on as criteria_to_sort_on_city
from src.sorting_criteria.sorting_criteria_city_and_name import criteria_to_sort_on as criteria_to_sort_on_city_and_name

class Test_FetchACriterion(unittest.TestCase):
   def test_fetch_a_criterion_returns_name_sorting_criteria_function(self):
     self.assertEqual(fetch_a_criterion('name'), criteria_to_sort_on_name)
     
   def test_fetch_a_criterion_returns_city_sorting_criteria_function(self):
     self.assertEqual(fetch_a_criterion('city'), criteria_to_sort_on_city)
     
   def test_fetch_a_criterion_returns_city_and_name_sorting_criteria_functions(self):
      self.assertEqual(fetch_a_criterion('city and name'), criteria_to_sort_on_city_and_name)
      
if __name__ == '__main__':
  unittest.main()
