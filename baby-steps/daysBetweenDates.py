# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeapYear(year):
  if (year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ) ):
    return True
  return False

def daysInMonth(year, month):
  """ Returns the no. of days in a given month in a given year """
  ## jan, feb, mar, apr, may, jun, july, august, september, october, november, december ##
  ## 01    02   03    04  05    06  07    08      09        10          11      12      ##
  ##  31    28   31   30  31    30  31    31      30        31          30      31      ##
  months = { 1 : 31,
             2 : 28,
             3 : 31,
             4 : 30,
             5 : 31,
             6 : 30,
             7 : 31,
             8 : 31,
             9 : 30,
             10 : 31,
             11 : 30,
             12 : 31 }

  if isLeapYear(year):
    months[2] = 29

  return months[month]

#print daysInMonth(2015, 1)
#print daysInMonth(2015, 6)
#print daysInMonth(2015, 2)
#print daysInMonth(2015, 11)

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    """
    # YOUR CODE HERE
    if day < daysInMonth(year, month):
      return year, month, day+1
    else:
      if month < 12:
        return year, month+1, 1
      else:
        return year+1, 1, 1

    return year, month, day

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
  # program defensively! Add an assertion if the input is not valid!
  # ensure second date is not before the first date
  # equal dates should not raise assertionerror
  assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
  days = 0
  while dateIsBefore(year1,month1,day1,year2,month2,day2):
    year1, month1, day1 = nextDay(year1,month1,day1)
    days += 1
    #print year1
    #print days

  return days

def dateIsBefore(year1, month1, day1, year2, month2, day2):
  """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
  if year1 < year2:
    #print year1," less than ",year2
    return True
  if year1 == year2:
    if month1 < month2:
      #print month1," less than ",month2
      return True
    if month1 == month2:
      return day1 < day2
  return False

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    for (args, answer) in test_cases:
      try:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
      except AssertionError:
        if answer == "AssertionError":
          print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
        else:
          print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)

test()
#print daysBetweenDates(1900,1,1,1999,12,31)