# Write a Python program to subtract five days from current date.

from datetime import datetime,timedelta
today=datetime.now()
new_date=today-timedelta(days=5)
print(f"Today: {today.strftime('%Y-%m-%d-%H-%M-%S')}")
print(f"Five days ago: {new_date.strftime('%Y-%m-%d')}")
