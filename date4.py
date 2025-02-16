# Write a Python program to calculate two date difference in seconds.

from datetime import datetime,timedelta
First_date=datetime(2005,12,21,12,21,12)
Second_date=datetime(2007,11,21,8,7,6)
dif=abs((First_date-Second_date).total_seconds())
print(f'the difference between {First_date} and {Second_date} is {dif}')
