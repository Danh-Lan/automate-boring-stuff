#! python
# date_detection.py - Check valid date

import re 

dateRegex = re.compile(
  r'''
    (0[1-9]|[12][0-9]|30|31) # day
    /
    (0[1-9]|1[0-2])          # month
    /
    ([12][0-9]{3})           # year
    ''', re.VERBOSE)

def check_valid_date(day, month, year):
  if month in [4, 6, 9, 11] and day > 30:
    return False
  
  if (month == 2):
    max_day = 28
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
      max_day = 29
    else:
      max_day = 28
    
    if (day > max_day):
      return False
  
  return True

def main():
  date = '29/02/2020'
  match = dateRegex.fullmatch(date)

  if match is None:
    print(date, 'has invalid format')
    exit()

  day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))

  if (check_valid_date(day, month, year)):
    print(date, 'is valid')
  else:
    print(date, 'is invalid')

if __name__ == "__main__":
  main()
