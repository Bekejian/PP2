import time
import math

num = float(input()) 
delay = int(input())  

time.sleep(delay / 1000)  

sqrt_value = math.sqrt(num)

print(f"Square root of {num} after {delay} milliseconds is {sqrt_value}")
