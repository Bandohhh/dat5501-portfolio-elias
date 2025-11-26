import numpy as np
import re

# Regular expression pattern for validating YYYY-MM-DD format
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def calculate_duration():
    """
    Calculate the duration between two dates, with an option to view results
    in days, weeks, or months.

    Returns:
        str: A formatted message showing the duration.
    """
    today = np.datetime64('today', 'D')

    # --- Get valid start date ---
    while True:
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")

        if not date_pattern.match(start_date_str):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            continue

        try:
            start_date = np.datetime64(start_date_str, 'D')
            break
        except ValueError:
            print("❌ Invalid date value. Please check and re-enter.")

    # --- Get valid end date ---
    while True:
        end_date_str = input(f"Enter the end date (YYYY-MM-DD) or press Enter for today [{today}]: ") or str(today)

        if not date_pattern.match(end_date_str):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            continue

        try:
            end_date = np.datetime64(end_date_str, 'D')
            break
        except ValueError:
            print("❌ Invalid date value. Please check and re-enter.")

    # --- Calculate duration in days ---
    duration_days = (end_date - start_date).astype(int)

    # --- Allow user to choose unit ---
    while True:
        unit = input("View duration in (d)ays, (w)eeks, or (m)onths? [d]: ").lower() or "d"

        if unit not in ("d", "w", "m"):
            print("❌ Invalid choice. Please enter 'd', 'w', or 'm'.")
            continue

        if unit == "w":
            duration_value = round(duration_days / 7, 2)
            unit_name = "weeks"
        elif unit == "m":
            duration_value = round(duration_days / 30.44, 2)  # average month length
            unit_name = "months"
        else:
            duration_value = duration_days
            unit_name = "days"
        break

    message = f"✅ Duration between {start_date} and {end_date} is {duration_value} {unit_name}."
    return message


# Example usage
if __name__ == "__main__":
    print(calculate_duration())
