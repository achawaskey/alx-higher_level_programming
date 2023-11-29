#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
thestring = "Last digit of {} is {}".format(number, lastdigit)
if last digit > 5:
    print("last digit of 98 is 8 and is greater than 5")
elif last digit == 0:
    print("last digit of 0 is 0 and is 0")
elif last digit < 6:
    print("last digit of -98 is 8 and is less than 6 and not 0")
