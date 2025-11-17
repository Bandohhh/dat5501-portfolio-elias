'''import numpy as np
import re
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$") # regular expression pattern for YYYY-MM-DD format ensures 4 digits-2 digits-2 digits (integers only)

def calculate_duration_in_days():
    """
    Calculate the duration in days between two dates.

    Returns:
    int: The duration in days between the two dates.
    """
    today = np.datetime64('today', 'D')
    while True:
    # Loop until valid start date is entered
        start_date_str = input("Please enter the start date (YYYY-MM-DD): ")
        
        if not date_pattern.match(start_date_str): # Validate start date format using regex
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            continue

        try:
            # Validate date values
            start_date = np.datetime64(start_date_str, 'D')
            
            # Exit loop if start date is valid
            break
        
        except ValueError: # Catch invalid date values
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")


        while True:
    # Loop until valid end date is entered
          end_date_str = input(f"Please enter the end date (YYYY-MM-DD) or press enter to use today's date [{today}]: ") or str(today) # Default to today's date if input is empty/user presses enter
        
        if not date_pattern.match(end_date_str): # Validate end date format using regex
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            continue

        try:

            # Validate date format
            end_date = np.datetime64(end_date_str, 'D')
            
            # Exit loop if end date is valid
            break

        except ValueError: # Catch invalid date format
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

    # Calculate and return duration in days
    duration = (end_date - start_date).astype(int) 
    return duration

# Example usage
print(calculate_duration_in_days())'''