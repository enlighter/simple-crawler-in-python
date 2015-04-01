# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
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
       in Gregorian calendar, and the first date is not after
       the second."""
  days = 0
  while dateIsBefore(year1,month1,day1,year2,month2,day2):
    year1, month1, day1 = nextDay(year1,month1,day1)
    days += 1
    #print year1
    #print days

  return days

def dateIsBefore(year1, month1, day1, year2, month2, day2):
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
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
#print daysBetweenDates(1900,1,1,1999,12,31)