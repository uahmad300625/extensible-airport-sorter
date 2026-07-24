import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airport_data import airports
from process_airports import process_airports
from fetch_a_criterion import fetch_a_criterion
from fetch_criteria import fetch_criteria

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(criteria):
    print("\nAvailable sorting criteria:")
    
    for index, criterion in enumerate(criteria, start=1):
        print(f'{index}.)  {criterion.title()}')

def get_valid_input_choice(criteria):
    while True:
        try:
            user_choice = input("\nSort the airports by entering a criteria's respective number (or 'q' to quit): ")
            
            if user_choice.lower() == 'q':
                return 'q'
                
            criteria_number = int(user_choice)
            
            if 1 <= criteria_number <= len(criteria):
                return criteria_number - 1 
            else:
                print(f"Please enter a valid number between 1 and {len(criteria)}")
                
        except ValueError:
            print("Please enter a valid number or 'q' to quit")

def sort_airports(airports, criterion):
    if criterion == "nothing (no sorting)":
        return process_airports(airports)
    
    return process_airports(airports, sort_criteria=fetch_a_criterion(criterion))

def display_airports(airports, sort_criterion):
    print(f"\nAirports sorted by: {sort_criterion.title()}\n")
    
    for airport in airports:
        print(f"{airport.iata}, {airport.name}, {airport.city}, "
              f"{airport.state}, {airport.temperature}, {airport.delay}")

def wait_for_user_after_displaying_results():
    print("\nPress Enter to continue...")
    input()

def exit_program_message():
    clear_screen()
    print("Thank you for using the airport sorting program!")

def main():
    criteria = fetch_criteria()
    criteria.append("nothing (no sorting)")

    while True:
        display_menu(criteria)
        user_choice = get_valid_input_choice(criteria)
        
        if user_choice == 'q':
            exit_program_message()
            break
            
        clear_screen()
        
        selected_criterion = criteria[user_choice]
        sorted_airports = sort_airports(airports, selected_criterion)
        display_airports(sorted_airports, selected_criterion)
        
        wait_for_user_after_displaying_results()
        clear_screen()

if __name__ == '__main__':
    main()
