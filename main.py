from get_car_info import get_car_info
from format_for_database import format_for_database
from generate_car_numbers import generate_car_numbers
import time
from random import randint

def main():
    car_numbers = generate_car_numbers()  # This will generate a large number of car numbers

    for car_number in car_numbers:
        car_info = get_car_info(car_number)
        # Pass car_number to format_for_database function
        car_data_for_db = format_for_database(car_info, car_number)  
        
        if car_data_for_db:
            # Database insertion or further processing here
            print(car_data_for_db)  # Placeholder for actual action
        else:
            # Handle cases where there is no data or an error occurred differently, if needed
            print(f"No data or an error occurred for car number: {car_number}")

        # Randomized delay between requests
        time.sleep(randint(2, 5))

if __name__ == "__main__":
    main()

