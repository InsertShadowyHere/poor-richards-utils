"""
This file is used to find the time between now and a given date, along with other utilities I might add later.
Using a website feels lame.
"""

import datetime

#x = datetime.datetime(int(input("What year? ")), int(input("What month? ")), int(input("What day? ")))
#temp
x = datetime.date(2025,11,1)
now = datetime.date.today()
til = (x - now)
# rough
# print(f"You have {til//30} months, {(til%30)//7} weeks, and {(til%30)%7} days until {x.strftime('%B %d, %Y')}.")

print(f"You have {til.days//7} weeks and {til.days%7} days until {x.strftime('%B %d, %Y')}.")
