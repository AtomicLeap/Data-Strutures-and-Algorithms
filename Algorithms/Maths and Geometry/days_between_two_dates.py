# 1360. Number of Days Between Two Dates

# https://leetcode.com/problems/number-of-days-between-two-dates/description/

# Key Idea:
# Convert each date into “number of days since a fixed origin” 
# (e.g., 1971-01-01), then take the absolute difference.

# This avoids libraries and works in O(1) time.

"""
# Rules to Handle

Leap years:
A year is a leap year if:

1. divisible by 400, or
2. divisible by 4 but not by 100

Month lengths depend on leap year status.
"""

def days_between_dates(date1: str, date2: str) -> int:
    def is_leap(year: int) -> bool:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def days_before_year(year: int) -> int:
        days = 0
        for y in range(1971, year):
            days += 366 if is_leap(y) else 365
        return days

    def days_before_month(year: int, month: int) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if is_leap(year):
            month_days[1] = 29
        return sum(month_days[:month - 1])

    def days_from_origin(date: str) -> int:
        y, m, d = map(int, date.split('-'))
        return (
            days_before_year(y) +
            days_before_month(y, m) +
            d
        )

    return abs(days_from_origin(date1) - days_from_origin(date2))

# O(k) - Time complexity
# O(1) - Space complexity


print(days_between_dates("2019-06-29", "2019-06-30")) # 1
print(days_between_dates("2020-01-15", "2019-12-31")) # 15
