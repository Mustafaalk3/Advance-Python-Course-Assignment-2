'''Importing modules'''
from datetime import datetime

def find_day_of_week(date_str: str) -> str:
    """
    Given a date in the string format 'YYYY-MM-DD', This function will return the day of the week.
    """
    date = datetime.strptime(date_str, "%Y-%m-%d")
    day_of_week = date.strftime("%A")

    if day_of_week in ["Saturday", "Sunday"]:
        return f"Today is {day_of_week}. Enjoy your weekend!"
    else:
        return f"Today is {day_of_week}"

# Example Test Cases
print(f"{find_day_of_week("2024-06-27")}")
# Input: "2024-06-27"
# Output: "Thursday"

# Input: "2024-01-01"
print(f"{find_day_of_week("2024-01-07")}")
# Output: "Monday"