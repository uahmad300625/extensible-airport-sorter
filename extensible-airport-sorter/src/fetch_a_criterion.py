from importlib import import_module

def fetch_a_criterion(property_name):
    return import_module(f'src.sorting_criteria.sorting_criteria_{property_name.replace(" ", "_")}').criteria_to_sort_on
