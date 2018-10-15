from datetime import date, timedelta
from collections import Counter
import calendar

def most_frequent_days(year):
    result = []
    step = timedelta(days=1)
    year_start = date(year, 1, 1)
    year_end = date(year, 12, 31)

    days_list = [year_start.weekday()]
    while year_start.weekday() != 6:
        year_start += step
        days_list += year_start.weekday(),

    days_list += year_end.weekday(),
    while year_end.weekday() != 0:
        year_end -= step
        days_list += year_end.weekday(),

    days_dict = Counter(days_list).most_common()
    for day in [k for k,v in sorted(days_dict) if v == days_dict[0][1]]:
        result += calendar.day_name[day],

    return result

print(most_frequent_days(328))
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert most_frequent_days(2399) ==  ['Friday'], "1st example"
#     assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
#     assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
#     assert most_frequent_days(2909) == ['Tuesday'], "4th example"