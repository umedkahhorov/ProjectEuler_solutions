def leap_year_check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def compute(year, day_names=['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']):
    leap = leap_year_check(year)
    if leap:
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    flattened_days = [day for days_in_month in months for day in range(1, days_in_month + 1)]
    weeks = len(flattened_days) // 7
    weeksr = len(flattened_days) % 7
    days = day_names * weeks
    days = days + days[:weeksr]
    indixes = [index for index, value in enumerate(flattened_days) if value == 1]
    count_sundays = sum(1 for index in indixes if days[index] == 'Sun')
    start_index = day_names.index(days[-1])
    reordered_days = day_names[start_index:] + day_names[:start_index]
    return count_sundays, reordered_days

if __name__ == "__main__":
    sundays1900, names = compute(1900)
    out = sundays1900  # Initialize with the correct count for 1900
    for i in range(1901, 2001):  # Starting from 1901
        sundays, days = compute(i, names)
        out += sundays
        names = days
    print(out)
