'''from datetime import date
# 1. Get the date
today = date.today()
print(today)

# 2. Breakdown Date data
today = date.today()
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())
# MARKDOWN ```
'''
'''

import datetime

# Convert Date to String
today = datetime.datetime.today()
# format YYYYMMDD
format1 = "%Y%m%d"
# Print Format
s = today.strftime(format1)
print(s)

# Format DD-MON-YYYY
format2 = "%d-%b-%Y"
# Print Format
s = today.strftime(format2)
print(s)

''''''
# Format DD-MON-YYYY HH24:MI:SS
format3 = "%d-%b-%Y %H:%M:%S"
# Print Format
s = today.strftime(format3)
print(s)
# MARKDOWN ```

'''
import datetime


################################################################################
# Convert String to Date
################################################################################
l_date_time_string = "2016-06-24"
l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
print(l_datetime)

# Convert String to Date Time in format; DD-MON-YYYY HH24:MI:SS
l_date_string1 = "2016-06-24 16:00:00"
format4        = "%Y-%m-%d %H:%M:%S"
t1 = datetime.datetime.strptime(l_date_string1, format4)
print("t1", t1)




""" MARKDOWN
## Python time Module: Date Comparisions and Checking
* Below is the demonstration to compare dates
MARKDOWN"""
# MARKDOWN ```
