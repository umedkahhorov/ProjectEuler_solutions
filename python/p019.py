

def leap_year_check(year):
    if (year % 4==0 and year%100 != 0) or (year % 400 ==0):
        return True
    else:
        return False
def compute(year,day_names = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']):
    leap = leap_year_check(year)
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if not leap:
        months[1] = 28  # # Change February to 29 days for leap year
    flattened_days = [day for days_in_month in months for day in range(1,days_in_month+1)]
    weeks = len(flattened_days)//7
    weeksr = len(flattened_days)%7

    # Create a list of day names for the entire year
    days= day_names * weeks
    days = days + days[:weeksr]
    indixes = [index for index, value in enumerate(flattened_days) if value == 1]
    # Count the number of Sundays
    count_sundays = sum(1 for index in indixes if days[index]=='Sun')
    # Determine the starting index for the reordered list of day names
    start_index = day_names.index(days[-1])+1
    reordered_days = day_names[start_index:] + day_names[:start_index]
    return count_sundays,reordered_days

# We simply use Python's built-in date library to compute the answer by brute force.
import datetime

def compute1():
    ans = sum(1
              for y in range(1901,2001)
              for m in range(1,13)
              if datetime.date(y,m,1).weekday()==6)
    return ans

if __name__ == "__main__":
    sundays1900,names = compute(1900)
    out = 0
    for i in range(1901,2001):
        sundays,days= compute(i,names)
        out +=sundays
        names = days
    print (out)
    print (compute1())


