"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
# Plan:
# User types 14_cal.py [month] [year]
# Read the argument values
# Check if they are valid
# Default to current month & year
# 1 arg should set the month
# 2 args should set the month and year
# Otherwise, print error and usages message
# Print calendar for given month and year

import sys
import calendar
                      ## datetime object
from datetime import datetime

## 1. Test to see if args are printing to the terminal first
args = sys.argv
# print(args)

# Read the argument values
# Check if they are valid

# 2. Default to current month & year
month = datetime.now().month
year = datetime.now().year

# if only filename is passed in, pass
if len(args) == 1:
  pass
# filename + 1 input should set the month
if len(args) == 2:
  month = int(args[1])
  # print error message if not 1-12

# filename + 2 inputs should set the month and year
# Month will be the first arg
elif len(args) == 3:
  month = int(args[1])
  year = int(args[2])

# Otherwise, print error message
else:
  print("Error: Should be in format '14_cal.py [month] [year]'")
  exit(0)

if month < 1 or month > 12:
  print('Error: Invalid month')
  exit(0)

# Print calendar for given month and year
# Test before adding calendar --> print(f'Calendar: {month} - {year}')
print(calendar.month(year, month))

## Alternative - 
# tc = calendar.TextCalendar()
# tc.prmonth(year, month)

