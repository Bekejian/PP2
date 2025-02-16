# Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime,timedelta
today=datetime.now()
tm=today+timedelta(days=1)
ys=today-timedelta(days=1)
print(f"昨天: {ys.strftime("%Y-%m-%d")}")
print(f"今天: {today.strftime('%Y-%m-%d')}")
print(f"明天: {tm.strftime('%Y-%m-%d')}")