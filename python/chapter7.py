import modules

print ('Area of trapeza is: ', modules.trapeza(12, 14, 18))

import math
print(math.__name__)
print(__name__)

help(modules)

import calendar
import arrow

birth = arrow.get(2025, 3, 12)
birth.humanize()

print('Today is: ', calendar.SATURDAY)