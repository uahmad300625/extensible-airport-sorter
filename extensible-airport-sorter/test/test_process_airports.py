import unittest
from src.process_airports import process_airports
from src.airport import Airport
from src.sorting_criteria.sorting_criteria_iata import criteria_to_sort_on as criteria_to_sort_on_iata
from src.sorting_criteria.sorting_criteria_city import criteria_to_sort_on as criteria_to_sort_on_city
from src.sorting_criteria.sorting_criteria_name import criteria_to_sort_on as criteria_to_sort_on_name
from src.sorting_criteria.sorting_criteria_delay import criteria_to_sort_on as criteria_to_sort_on_delay
from src.sorting_criteria.sorting_criteria_state import criteria_to_sort_on as criteria_to_sort_on_state
from src.sorting_criteria.sorting_criteria_temperature import criteria_to_sort_on as criteria_to_sort_on_temperature
from src.sorting_criteria.sorting_criteria_city_and_name import criteria_to_sort_on as criteria_to_sort_on_city_and_name

class Test_ProcessAirports(unittest.TestCase):
    def setUp(self):
        self.iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, True)
        self.ord = Airport("ORD", "O'HARE INTERNATIONAL", "Chicago", "IL", 62, True)
        self.mdw = Airport("MDW", "MIDWAY INTERNATIONAL", "Chicago", "IL", 60, False)

        self.airports = [self.iad, self.ord, self.mdw]
    
    def test_canary(self):
        self.assertTrue(True)
        
    def test_take_empty_list_return_empty_list(self):
        self.assertEqual(process_airports([]), [])

    def test_list_with_one_aiport_and_returns_list_as_is(self): 
        airports = [self.iad]
        
        self.assertEqual(process_airports(airports), airports)

    def test_list_with_two_aiports_and_returns_list_as_is(self):
        airports = [self.iad, self.ord]

        self.assertEqual(process_airports(airports), airports)

    def test_list_with_three_aiports_and_returns_list_as_is(self): 
        airports = [self.iad, self.ord, self.mdw]

        self.assertEqual(process_airports(airports), airports)
    
    def test_sort_two_airports_by_IATA_code(self):
        self.assertEqual(process_airports([self.ord, self.iad], sort_criteria=criteria_to_sort_on_iata), [self.iad, self.ord])
        
    def test_sort_three_airports_by_Name(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_name), [self.iad, self.mdw, self.ord])
        
    def test_sort_three_airports_by_City(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_city), [self.ord, self.mdw, self.iad])
        
    def test_sort_three_airports_by_State(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_state), [self.iad, self.ord, self.mdw])
        
    def test_sort_three_airports_by_Delay(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_delay), [self.mdw, self.iad, self.ord])
        
    def test_sort_three_airports_by_Temperature(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_temperature), [self.mdw, self.ord, self.iad])

    def test_sort_three_airports_by_city_and_name(self):
        self.assertEqual(process_airports(self.airports, sort_criteria=criteria_to_sort_on_city_and_name), [self.mdw, self.ord, self.iad])
    
    def test_take_one_aiport_with_name_in_lowercase_and_return_name_in_uppercase(self):
        iah = Airport("IAH", "george bush intercont.", "Houston", "TX", 82, True)
        
        result = process_airports([iah])

        self.assertEqual(iah.name, "george bush intercont.")
        self.assertEqual(result[0].name, "GEORGE BUSH INTERCONT.")

if __name__ == '__main__':
  unittest.main()
