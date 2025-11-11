import numpy as np
import re
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$") # regular expression pattern for YYYY-MM-DD format ensures 4 digits-2 digits-2 digits (integers only)

def calculate_duration_in_days():
    """
    Calculate the duration in days between two dates.

    Returns:
    int: The duration in days between the two dates.
    """
    today = np.datetime64('today', 'D')