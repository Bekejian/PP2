# Write a Python program to drop microseconds from datetime.

from datetime import datetime
today=datetime.now()
new_day=today.replace(microsecond=0)
print(f"Today: {today}")
print(f'After changes: {new_day}')


# The .replace() method in Python's datetime module creates a new datetime object 
# with specified modifications while keeping the rest of the values unchanged.